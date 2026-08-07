import {
  ArrowRight,
  BookOpenCheck,
  CheckCircle2,
  Headphones,
  Mountain,
  Presentation,
  Sparkles,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import ContinueLearningCard from "../components/dashboard/ContinueLearningCard";
import ProgressBar from "../components/ProgressBar";
import { WORKSHOP_SESSIONS } from "../data/workshopData";
import { api } from "../services/api";
import { getLearningSession } from "../services/learningSession";

function getGreeting() {
  const hour = new Date().getHours();
  if (hour < 12) return "Good morning";
  if (hour < 18) return "Good afternoon";
  return "Good evening";
}

function getSuggestedStep(session) {
  const activeTab = session?.activeTab || "lesson";
  if (activeTab === "audio") return "Continue your audio lesson";
  if (activeTab === "lab") return "Continue the hands-on lab";
  if (activeTab === "quiz") return "Finish the knowledge check";
  if (activeTab === "reflection") return "Finish your reflection";
  return "Continue your current lesson";
}

export default function Dashboard() {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState(null);
  const [learningSession, setLearningSession] = useState(() => getLearningSession());
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([api.getModules(), api.getProgress()])
      .then(([moduleData, progressData]) => {
        setModules(moduleData);
        setProgress(progressData);
      })
      .catch((err) => setError(err.message));
  }, []);

  useEffect(() => {
    const refreshSession = () => setLearningSession(getLearningSession());
    window.addEventListener("focus", refreshSession);
    document.addEventListener("visibilitychange", refreshSession);
    return () => {
      window.removeEventListener("focus", refreshSession);
      document.removeEventListener("visibilitychange", refreshSession);
    };
  }, []);

  const currentLesson = useMemo(() => {
    const flattenedLessons = modules.flatMap((module) =>
      (module.lessons || []).map((lesson) => ({
        ...lesson,
        moduleTitle: module.title,
        moduleNumber: module.number,
      }))
    );

    const savedLesson = flattenedLessons.find(
      (lesson) => String(lesson.id) === String(learningSession.lessonId)
    );

    if (savedLesson) return savedLesson;

    const completed = new Set((progress?.completed_lessons || []).map(String));
    return (
      flattenedLessons.find((lesson) => !completed.has(String(lesson.id))) ||
      flattenedLessons[0]
    );
  }, [learningSession.lessonId, modules, progress]);

  const latestWorkshop = WORKSHOP_SESSIONS.at(-1);
  const nextModule = modules.find((module) => module.status === "active") || modules[0];

  if (error) return <div className="error-card">{error}</div>;
  if (!progress) return <div className="loading-card">Preparing your ascent...</div>;

  return (
    <div className="page-stack dashboard-v2">
      <section className="dashboard-welcome">
        <div>
          <span className="eyebrow">{getGreeting()}, Bryant</span>
          <h1>What&apos;s your next step?</h1>
          <p>
            Ascend remembers where you stopped so you can spend your time learning instead of finding your place.
          </p>
        </div>
        <div className="dashboard-altitude">
          <span>{progress.percent}%</span>
          <small>Journey complete</small>
        </div>
      </section>

      <section className="dashboard-primary-grid">
        <ContinueLearningCard lesson={currentLesson} session={learningSession} />

        <article className="today-climb-card">
          <div className="today-climb-heading">
            <span className="today-climb-icon"><Sparkles size={19} /></span>
            <div>
              <span className="eyebrow">TODAY&apos;S CLIMB</span>
              <h2>Keep the momentum.</h2>
            </div>
          </div>

          <div className="today-climb-list">
            <div className="today-climb-step active">
              <span>1</span>
              <div>
                <strong>{getSuggestedStep(learningSession)}</strong>
                <small>{currentLesson?.title}</small>
              </div>
            </div>
            <div className="today-climb-step">
              <span>2</span>
              <div>
                <strong>Practice what you learned</strong>
                <small>Use the lesson lab when you are ready.</small>
              </div>
            </div>
            <div className="today-climb-step">
              <span>3</span>
              <div>
                <strong>Capture the takeaway</strong>
                <small>Reflection turns a lesson into something you can explain.</small>
              </div>
            </div>
          </div>

          <Link className="text-link-arrow" to={currentLesson ? `/lessons/${currentLesson.id}` : "/modules"}>
            Open today&apos;s lesson <ArrowRight size={16} />
          </Link>
        </article>
      </section>

      <section className="dashboard-overview-grid">
        <article className="panel ascent-overview-card">
          <div className="panel-heading compact-heading">
            <div>
              <span className="eyebrow">YOUR ASCENT</span>
              <h2>Journey progress</h2>
            </div>
            <strong className="progress-number">{progress.percent}%</strong>
          </div>
          <ProgressBar value={progress.percent} />

          <div className="ascent-metrics">
            <div>
              <Mountain size={18} />
              <span>Level</span>
              <strong>{progress.level}</strong>
            </div>
            <div>
              <BookOpenCheck size={18} />
              <span>Lessons</span>
              <strong>{progress.completed_count}/{progress.total_lessons}</strong>
            </div>
            <div>
              <Headphones size={18} />
              <span>XP</span>
              <strong>{progress.xp}</strong>
            </div>
          </div>

          {nextModule && (
            <div className="current-module-row">
              <span className="module-dot active" />
              <div>
                <small>Current focus</small>
                <strong>Module {nextModule.number}: {nextModule.title}</strong>
              </div>
              <Link to="/modules" aria-label="View Journey"><ArrowRight size={18} /></Link>
            </div>
          )}
        </article>

        <article className="panel workshop-preview-card">
          <div className="workshop-preview-icon"><Presentation size={22} /></div>
          <span className="eyebrow">DEVOPS WORKSHOP</span>
          <h2>{latestWorkshop?.title || "Real-world learning"}</h2>
          <p>
            {latestWorkshop?.summary || "Connect your weekly mentoring sessions to the concepts you are learning in The Journey."}
          </p>
          {latestWorkshop && (
            <div className="workshop-preview-meta">
              <span>Session {latestWorkshop.number}</span>
              <span>{latestWorkshop.date}</span>
            </div>
          )}
          <Link className="secondary-button" to={latestWorkshop ? `/workshop/sessions/${latestWorkshop.id}` : "/workshop"}>
            Review workshop <ArrowRight size={16} />
          </Link>
        </article>
      </section>

      <section className="learning-spaces-row">
        <Link className="learning-space-card journey-space" to="/modules">
          <BookOpenCheck size={22} />
          <div>
            <span className="eyebrow">THE JOURNEY</span>
            <strong>Structured DevOps curriculum</strong>
            <p>Learn the fundamentals in an intentional sequence.</p>
          </div>
          <ArrowRight size={18} />
        </Link>

        <Link className="learning-space-card workshop-space" to="/workshop">
          <Presentation size={22} />
          <div>
            <span className="eyebrow">DEVOPS WORKSHOP</span>
            <strong>Real-world mentoring</strong>
            <p>Review sessions, practice labs, and prepare questions.</p>
          </div>
          <ArrowRight size={18} />
        </Link>
      </section>

      <section className="panel climb-principle dashboard-principle">
        <CheckCircle2 size={22} />
        <div>
          <span className="eyebrow">ASCEND PRINCIPLE</span>
          <strong>You do not need to finish the mountain today. You only need the next deliberate step.</strong>
        </div>
      </section>
    </div>
  );
}
