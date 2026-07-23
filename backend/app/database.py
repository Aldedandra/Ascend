import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = os.getenv("JOURNEY_DB_PATH", "/data/journey.db")


def ensure_parent_directory() -> None:
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


@contextmanager
def get_connection():
    ensure_parent_directory()
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_database() -> None:
    with get_connection() as connection:
        connection.executescript(
            '''
            CREATE TABLE IF NOT EXISTS progress (
                lesson_id TEXT PRIMARY KEY,
                completed INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT
            );

            CREATE TABLE IF NOT EXISTS quiz_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                submitted_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS achievements (
                achievement_id TEXT PRIMARY KEY,
                unlocked_at TEXT NOT NULL
            );
            '''
        )
