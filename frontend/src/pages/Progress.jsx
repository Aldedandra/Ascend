import {
  Award,
  BookOpenCheck,
  CheckCircle2,
  Flame,
  Play,
  Trophy,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import ProgressBar from "../components/ProgressBar";
import StatCard from "../components/StatCard";
import { api } from "../services/api";

export default function Progress() {
  const [progress, setProgress] = useState(null);
  const [modules, setModules] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([api.getProgress(), api.getModules()])
      .then(([progressData, moduleData]) => {
        setProgress(progressData);
        setModules(moduleData);
      })
      .catch((err) => {
        setError(err.message);
      });
  }, []);

  const currentLesson = useMemo(() => {
    if (!progress) return null;

    const completed = new Set(progress.completed_lessons || []);

    for (const module of modules) {
      for (const lesson of module.lessons || []) {
        if (!completed.has(lesson.id)) {
          return {
            ...lesson,
            moduleNumber: module.number,
            moduleTitle: module.title,
          };
        }
      }
    }

    return null;
  }, [modules, progress]);

  const passedQuizCount = useMemo(() => {
    if (!progress) return 0;

    const passedLessons = new Set(
      progress.quiz_results
        .filter((result) => result.total > 0 && result.score / result.total >= 0.8)
        .map((result) => result.lesson_id)
    );

    return passedLessons.size;
  }, [progress]);

  if (error) {
    return (
      <div className="error-card">
        Unable to load progress: {error}
      </div>
    );
  }

  if (!progress) {
    return <div className="loading-card">Loading progress...</div>;
  }

  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">CHARACTER SHEET</span>
        <h1>Your progress</h1>
        <p>Track consistency, competence, and the person you are becoming.</p>
      </header>

      <section className="stats-grid">
        <StatCard
          icon={Flame}
          label="Level"
          value={progress.level}
          helper={`${progress.xp} XP earned`}
        />

        <StatCard
          icon={CheckCircle2}
          label="Lessons complete"
          value={`${progress.completed_count}/${progress.total_lessons}`}
          helper={`${progress.percent}% overall`}
        />

        <StatCard
          icon={Trophy}
          label="Quizzes passed"
          value={passedQuizCount}
          helper={`${progress.quiz_results.length} attempts recorded`}
        />

        <StatCard
          icon={Award}
          label="Achievements"
          value={progress.achievements.length}
          helper="Milestones unlocked"
        />
      </section>

      <section className="panel">
        <div className="panel-heading">
          <div>
            <span className="eyebrow">CURRENT JOURNEY</span>

            {currentLesson ? (
              <>
                <h2>
                  Module {currentLesson.moduleNumber}: {currentLesson.moduleTitle}
                </h2>
                <p>
                  Next lesson: {currentLesson.title}
                </p>
              </>
            ) : (
              <>
                <h2>All available lessons complete</h2>
                <p>Your next module will appear here when it is released.</p>
              </>
            )}
          </div>

          {currentLesson && (
            <Link
              className="secondary-button"
              to={`/lessons/${currentLesson.id}`}
            >
              <Play size={17} />
              Continue
            </Link>
          )}
        </div>

        <ProgressBar value={progress.percent} />
      </section>

      <section className="panel">
        <div className="panel-heading">
          <div>
            <span className="eyebrow">LEVEL PROGRESS</span>
            <h2>
              {progress.xp} / {progress.next_level_xp} XP
            </h2>
          </div>
        </div>

        <ProgressBar
          value={(progress.xp / progress.next_level_xp) * 100}
        />
      </section>

      <section className="panel">
        <div className="panel-heading">
          <div>
            <span className="eyebrow">ACHIEVEMENTS</span>
            <h2>Milestones unlocked</h2>
          </div>
        </div>

        {progress.achievements.length ? (
          <div className="achievement-grid">
            {progress.achievements.map((achievement) => (
              <article className="achievement-card" key={achievement.id}>
                <div className="achievement-icon">
                  <Award size={22} />
                </div>

                <strong>{achievement.title}</strong>
                <p>{achievement.description}</p>
                <small>+{achievement.xp} XP</small>
              </article>
            ))}
          </div>
        ) : (
          <div>
            <BookOpenCheck size={22} />
            <p>Complete your first lesson to unlock an achievement.</p>
          </div>
        )}
      </section>
    </div>
  );
}