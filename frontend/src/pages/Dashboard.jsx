import {
  Award,
  BookOpenCheck,
  CheckCircle2,
  FlaskConical,
  Headphones,
  Mountain,
  Play,
  Presentation,
  ScrollText,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import AscendLogo from "../components/AscendLogo";
import ProgressBar from "../components/ProgressBar";
import StatCard from "../components/StatCard";
import { api } from "../services/api";

function getGreeting() {
  const hour = new Date().getHours();
  if (hour < 12) return "Good morning";
  if (hour < 18) return "Good afternoon";
  return "Good evening";
}

export default function Dashboard() {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([api.getModules(), api.getProgress()])
      .then(([moduleData, progressData]) => {
        setModules(moduleData);
        setProgress(progressData);
      })
      .catch((err) => setError(err.message));
  }, []);

  const currentLesson = useMemo(() => {
    const completed = new Set(progress?.completed_lessons || []);
    for (const module of modules) {
      for (const lesson of module.lessons || []) {
        if (!completed.has(lesson.id)) return { ...lesson, moduleTitle: module.title, moduleNumber: module.number };
      }
    }
    return modules[0]?.lessons?.[0];
  }, [modules, progress]);

  if (error) return <div className="error-card">{error}</div>;
  if (!progress) return <div className="loading-card">Preparing your ascent...</div>;

  return (
    <div className="page-stack">
      <section className="hero-panel ascend-hero">
        <div className="hero-copy">
          <span className="eyebrow">{getGreeting()}, Bryant</span>
          <h1>Keep Climbing.</h1>
          <p>
            Every lesson, lab, workshop, and reflection is another step toward the engineer you are becoming.
          </p>
        </div>
        <div className="mountain-visual" aria-hidden="true">
          <div className="altitude-line altitude-one" />
          <div className="altitude-line altitude-two" />
          <div className="altitude-line altitude-three" />
          <AscendLogo />
          <span>{progress.percent}% ASCENDED</span>
        </div>

        {currentLesson && (
          <div className="hero-actions">
            <Link className="primary-button" to={`/lessons/${currentLesson.id}`}>
              <Play size={18} />
              Continue learning
            </Link>
            <Link className="secondary-button" to="/modules">
              View journey
            </Link>
          </div>
        )}
      </section>

      <section className="stats-grid">
        <StatCard icon={Mountain} label="Current level" value={progress.level} helper={`${progress.xp} XP earned`} />
        <StatCard icon={BookOpenCheck} label="Lessons complete" value={`${progress.completed_count}/${progress.total_lessons}`} helper={`${progress.percent}% overall`} />
        <StatCard icon={Award} label="Achievements" value={progress.achievements.length} helper="Milestones unlocked" />
        <StatCard icon={Headphones} label="Available lessons" value={progress.total_lessons} helper="Read, listen, build" />
      </section>

      <section className="content-grid dashboard-grid">
        <article className="panel continue-panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">NEXT STEP</span>
              <h2>{currentLesson?.title || "Available journey complete"}</h2>
            </div>
            <span className="status-pill">Module {currentLesson?.moduleNumber ?? "—"}</span>
          </div>
          <p>{currentLesson?.summary}</p>
          <div className="lesson-context">
            <span>{currentLesson?.moduleTitle}</span>
            <span>{currentLesson?.duration_minutes || 0} min</span>
            <span>+{currentLesson?.xp || 0} XP</span>
          </div>
          {currentLesson && <Link className="primary-button" to={`/lessons/${currentLesson.id}`}><Play size={17} /> Resume lesson</Link>}
        </article>

        <article className="panel progress-panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">YOUR ASCENT</span>
              <h2>Overall journey</h2>
            </div>
            <strong className="progress-number">{progress.percent}%</strong>
          </div>
          <ProgressBar value={progress.percent} />
          <div className="roadmap-list">
            {modules.slice(0, 4).map((module) => (
              <div className="roadmap-row" key={module.id}>
                <span className={`module-dot ${module.status}`} />
                <div>
                  <strong>Module {module.number}: {module.title}</strong>
                  <small>{module.subtitle}</small>
                </div>
              </div>
            ))}
          </div>
        </article>
      </section>

      <section className="platform-grid">
        <Link className="platform-card active-platform" to="/modules">
          <BookOpenCheck size={22} /><span className="eyebrow">JOURNEY</span><strong>Structured curriculum</strong><p>Follow your DevOps learning path.</p>
        </Link>
        <Link className="platform-card" to="/workshop">
          <Presentation size={22} /><span className="eyebrow">WORKSHOP</span><strong>Learn from Travis</strong><p>Connect meetings to lessons and actions.</p>
        </Link>
        <Link className="platform-card" to="/labs">
          <FlaskConical size={22} /><span className="eyebrow">LABS</span><strong>Build and troubleshoot</strong><p>Turn knowledge into repeatable skill.</p>
        </Link>
        <Link className="platform-card" to="/handbook">
          <ScrollText size={22} /><span className="eyebrow">HANDBOOK</span><strong>Keep what you learn</strong><p>Create your engineering reference.</p>
        </Link>
      </section>

      <section className="panel climb-principle">
        <CheckCircle2 size={22} />
        <div><span className="eyebrow">TODAY'S PRINCIPLE</span><strong>You do not need to reach the summit today. You only need to take the next step.</strong></div>
      </section>
    </div>
  );
}
