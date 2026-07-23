import { Award, CheckCircle2, Flame, Trophy } from "lucide-react";
import { useEffect, useState } from "react";
import ProgressBar from "../components/ProgressBar";
import StatCard from "../components/StatCard";
import { api } from "../services/api";

export default function Progress() {
  const [progress, setProgress] = useState(null);

  useEffect(() => {
    api.getProgress().then(setProgress);
  }, []);

  if (!progress) return <div className="loading-card">Loading progress...</div>;

  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">CHARACTER SHEET</span>
        <h1>Your progress</h1>
        <p>Track consistency, competence, and the person you are becoming.</p>
      </header>

      <section className="stats-grid">
        <StatCard icon={Flame} label="Level" value={progress.level} helper={`${progress.xp} XP`} />
        <StatCard icon={CheckCircle2} label="Complete" value={`${progress.percent}%`} helper={`${progress.completed_count} lessons`} />
        <StatCard icon={Trophy} label="Quizzes" value={progress.quiz_results.length} helper="Attempts recorded" />
        <StatCard icon={Award} label="Achievements" value={progress.achievements.length} helper="Unlocked" />
      </section>

      <section className="panel">
        <div className="panel-heading">
          <div>
            <span className="eyebrow">LEVEL PROGRESS</span>
            <h2>{progress.xp} / {progress.next_level_xp} XP</h2>
          </div>
        </div>
        <ProgressBar value={(progress.xp / progress.next_level_xp) * 100} />
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
                <div className="achievement-icon"><Award size={22} /></div>
                <strong>{achievement.title}</strong>
                <p>{achievement.description}</p>
                <small>+{achievement.xp} XP</small>
              </article>
            ))}
          </div>
        ) : (
          <p>Complete your first lesson to unlock an achievement.</p>
        )}
      </section>
    </div>
  );
}
