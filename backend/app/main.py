import json
import os
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .content import ACHIEVEMENTS, MODULES
from .database import get_connection, initialize_database
from .schemas import JournalCreate, ProgressUpdate, QuizSubmission

app = FastAPI(title="The Journey API", version="1.0.0")

origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000"
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    initialize_database()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def find_lesson(lesson_id: str) -> dict[str, Any]:
    for module in MODULES:
        for lesson in module["lessons"]:
            if lesson["id"] == lesson_id:
                return lesson
    raise HTTPException(status_code=404, detail="Lesson not found")


def completed_lessons() -> set[str]:
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT lesson_id FROM progress WHERE completed = 1"
        ).fetchall()
    return {row["lesson_id"] for row in rows}


def unlock_achievement(achievement_id: str) -> None:
    with get_connection() as connection:
        connection.execute(
            "INSERT OR IGNORE INTO achievements (achievement_id, unlocked_at) VALUES (?, ?)",
            (achievement_id, utc_now()),
        )


def evaluate_achievements() -> None:
    completed = completed_lessons()
    if completed:
        unlock_achievement("first-step")
    if "0-3" in completed:
        unlock_achievement("conversation-mapper")

    module_zero_ids = {
        lesson["id"]
        for module in MODULES
        if module["id"] == "module-0"
        for lesson in module["lessons"]
    }
    if module_zero_ids and module_zero_ids.issubset(completed):
        unlock_achievement("module-zero")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/modules")
def get_modules() -> list[dict[str, Any]]:
    return MODULES


@app.get("/api/lessons/{lesson_id}")
def get_lesson(lesson_id: str) -> dict[str, Any]:
    lesson = find_lesson(lesson_id)
    with get_connection() as connection:
        row = connection.execute(
            "SELECT completed, completed_at FROM progress WHERE lesson_id = ?",
            (lesson_id,),
        ).fetchone()
    return {
        **lesson,
        "completed": bool(row["completed"]) if row else False,
        "completed_at": row["completed_at"] if row else None,
    }


@app.get("/api/progress")
def get_progress() -> dict[str, Any]:
    evaluate_achievements()
    total_lessons = sum(len(module["lessons"]) for module in MODULES)
    completed = completed_lessons()

    with get_connection() as connection:
        quiz_rows = connection.execute(
            "SELECT lesson_id, score, total, submitted_at FROM quiz_results ORDER BY id DESC"
        ).fetchall()
        achievement_rows = connection.execute(
            "SELECT achievement_id, unlocked_at FROM achievements"
        ).fetchall()

    unlocked_map = {row["achievement_id"]: row["unlocked_at"] for row in achievement_rows}
    unlocked_achievements = [
        {**achievement, "unlocked_at": unlocked_map[achievement["id"]]}
        for achievement in ACHIEVEMENTS
        if achievement["id"] in unlocked_map
    ]

    lesson_xp = sum(
        lesson.get("xp", 0)
        for module in MODULES
        for lesson in module["lessons"]
        if lesson["id"] in completed
    )
    achievement_xp = sum(item["xp"] for item in unlocked_achievements)
    xp = lesson_xp + achievement_xp
    level = max(1, xp // 100 + 1)

    return {
        "completed_lessons": sorted(completed),
        "completed_count": len(completed),
        "total_lessons": total_lessons,
        "percent": round((len(completed) / total_lessons) * 100) if total_lessons else 0,
        "xp": xp,
        "level": level,
        "next_level_xp": level * 100,
        "quiz_results": [dict(row) for row in quiz_rows],
        "achievements": unlocked_achievements,
    }


@app.put("/api/progress/{lesson_id}")
def update_progress(lesson_id: str, update: ProgressUpdate) -> dict[str, Any]:
    find_lesson(lesson_id)
    completed_at = utc_now() if update.completed else None
    with get_connection() as connection:
        connection.execute(
            '''
            INSERT INTO progress (lesson_id, completed, completed_at)
            VALUES (?, ?, ?)
            ON CONFLICT(lesson_id) DO UPDATE SET
                completed = excluded.completed,
                completed_at = excluded.completed_at
            ''',
            (lesson_id, int(update.completed), completed_at),
        )
    evaluate_achievements()
    return {"lesson_id": lesson_id, "completed": update.completed, "completed_at": completed_at}


@app.post("/api/quizzes/{lesson_id}")
def submit_quiz(lesson_id: str, submission: QuizSubmission) -> dict[str, Any]:
    lesson = find_lesson(lesson_id)
    questions = lesson.get("quiz", [])
    if len(submission.answers) != len(questions):
        raise HTTPException(status_code=400, detail="Answer every question before submitting.")

    score = sum(
        1
        for index, answer in enumerate(submission.answers)
        if answer == questions[index]["correct"]
    )

    with get_connection() as connection:
        connection.execute(
            "INSERT INTO quiz_results (lesson_id, score, total, submitted_at) VALUES (?, ?, ?, ?)",
            (lesson_id, score, len(questions), utc_now()),
        )

    return {"score": score, "total": len(questions)}


@app.get("/api/journal")
def list_journal() -> list[dict[str, Any]]:
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, body, created_at FROM journal_entries ORDER BY id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


@app.post("/api/journal")
def create_journal(entry: JournalCreate) -> dict[str, Any]:
    created_at = utc_now()
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO journal_entries (title, body, created_at) VALUES (?, ?, ?)",
            (entry.title.strip(), entry.body.strip(), created_at),
        )
        entry_id = cursor.lastrowid
    return {
        "id": entry_id,
        "title": entry.title.strip(),
        "body": entry.body.strip(),
        "created_at": created_at,
    }


@app.delete("/api/journal/{entry_id}")
def delete_journal(entry_id: int) -> dict[str, bool]:
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM journal_entries WHERE id = ?",
            (entry_id,),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Journal entry not found")
    return {"deleted": True}
