import { BookOpen, Clock3, Headphones, Play } from "lucide-react";
import { Link } from "react-router-dom";
import { describeLastOpened } from "../../services/learningSession";

const TAB_LABELS = {
  lesson: "Lesson",
  audio: "Audio",
  lab: "Lab",
  quiz: "Quiz",
  reflection: "Reflection",
};

const RESUME_ACTIONS = {
  lesson: "Continue lesson",
  audio: "Continue listening",
  lab: "Continue lab",
  quiz: "Continue quiz",
  reflection: "Continue reflection",
};

export default function ContinueLearningCard({ lesson, session }) {
  if (!lesson) return null;

  const savedLesson = String(session?.lessonId ?? "") === String(lesson.id);
  const activeTab = savedLesson ? session.activeTab || "lesson" : "lesson";
  const audioProgress = savedLesson ? Math.round(session.audioProgress || 0) : 0;

  const lastOpened = savedLesson
    ? describeLastOpened(session.lastOpenedAt)
    : "Your next lesson";

  const resumeLabel = TAB_LABELS[activeTab] || "Lesson";

  const resumeDetail =
    activeTab === "audio" && audioProgress > 0
      ? `${audioProgress}% listened`
      : activeTab === "lesson"
        ? "In progress"
        : resumeLabel;

  const actionLabel = savedLesson
    ? RESUME_ACTIONS[activeTab] || "Resume learning"
    : "Start lesson";

  return (
    <article className="continue-climb-card">
      <div className="continue-climb-topline">
        <span className="eyebrow">CONTINUE YOUR CLIMB</span>
        <span className="continue-module-pill">
          Module {lesson.moduleNumber ?? "—"}
        </span>
      </div>

      <div className="continue-climb-main">
        <div className="continue-climb-copy">
          <span className="continue-climb-module">
            {lesson.moduleTitle}
          </span>
          <h2>{lesson.title}</h2>
          <p>{lesson.summary}</p>
        </div>

        <div className="continue-climb-resume">
          <span className="continue-resume-icon" aria-hidden="true">
            {activeTab === "audio"
              ? <Headphones size={22} />
              : <BookOpen size={22} />}
          </span>

          <div>
            <small>Resume from</small>
            <strong>{resumeDetail}</strong>
          </div>

          <span className="continue-last-opened">
            <Clock3 size={14} /> {lastOpened}
          </span>
        </div>

        {activeTab === "audio" && audioProgress > 0 && (
          <div className="continue-audio-block">
            <div className="continue-audio-meta">
              <span>Audio progress</span>
              <strong>{audioProgress}%</strong>
            </div>

            <div
              className="continue-audio-progress"
              aria-label={`${audioProgress}% listened`}
            >
              <div style={{ width: `${Math.min(audioProgress, 100)}%` }} />
            </div>
          </div>
        )}

        <div className="continue-climb-footer">
          <div className="lesson-context continue-context">
            <span>{lesson.duration_minutes || 0} min</span>
            <span>+{lesson.xp || 0} XP</span>
          </div>

          <Link
            className="primary-button continue-climb-button"
            to={`/lessons/${lesson.id}`}
          >
            <Play size={17} /> {actionLabel}
          </Link>
        </div>
      </div>
    </article>
  );
}