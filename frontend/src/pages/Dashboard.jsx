import {
  Award,
  BookOpenCheck,
  Flame,
  Headphones,
  Play,
  Sparkles,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import ProgressBar from "../components/ProgressBar";
import StatCard from "../components/StatCard";
import { api } from "../services/api";

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
        if (!completed.has(lesson.id)) return lesson;
      }
    }
    return modules[0]?.lessons?.[0];
  }, [modules, progress]);

  if (error) return <div className="error-card">{error}</div>;
  if (!progress) return <div className="loading-card">Loading your journey...</div>;

  return (
    <div className="page-stack">
      <section className="hero-panel">
        <div className="hero-copy">
          <span className="eyebrow">WELCOME BACK, SYSTEMS EXPLORER</span>
          <h1>Be ready. Keep becoming.</h1>
          <p>
            Your past explains you. It does not define you. Today&apos;s work builds
            tomorrow&apos;s confidence.
          </p>
          {currentLesson && (
            <Link className="primary-button" to={`/lessons/${currentLesson.id}`}>
              <Play size={18} />
              Continue {currentLesson.title}
            </Link>
          )}
        </div>
        <div className="hero-orbit" aria-hidden="true">
          <div className="orbit-ring orbit-one" />
          <div className="orbit-ring orbit-two" />
          <Sparkles size={36} />
        </div>
      </section>

      <section className="stats-grid">
        <StatCard
          icon={Flame}
          label="Current level"
          value={progress.level}
          helper={`${progress.xp} XP earned`}
        />
        <StatCard
          icon={BookOpenCheck}
          label="Lessons complete"
          value={`${progress.completed_count}/${progress.total_lessons}`}
          helper={`${progress.percent}% overall`}
        />
        <StatCard
          icon={Award}
          label="Achievements"
          value={progress.achievements.length}
          helper="Milestones unlocked"
        />
        <StatCard
          icon={Headphones}
          label="Audio lessons"
          value={modules[0]?.lessons?.length || 0}
          helper="Ready to listen"
        />
      </section>

      <section className="content-grid two-column">
        <article className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">ROADMAP</span>
              <h2>Your journey</h2>
            </div>
            <Link to="/modules">View all</Link>
          </div>
          <ProgressBar value={progress.percent} />
          <div className="roadmap-list">
            {modules.slice(0, 5).map((module) => (
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

        <article className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">CURRENT OBJECTIVE</span>
              <h2>{currentLesson?.title || "Journey complete"}</h2>
            </div>
          </div>
          <p>{currentLesson?.summary}</p>
          <div className="quest-list">
            <div><BookOpenCheck size={18} /> Read the lesson</div>
            <div><Headphones size={18} /> Listen to the audio script</div>
            <div><Flame size={18} /> Complete the lab</div>
            <div><Award size={18} /> Pass the quiz and reflect</div>
          </div>
        </article>
      </section>
    </div>
  );
}
