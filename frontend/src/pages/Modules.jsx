import { CheckCircle2, ChevronDown, ChevronRight, ChevronUp, LockKeyhole } from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../services/api";

export default function Modules() {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState({ completed_lessons: [] });
  const [collapsedModules, setCollapsedModules] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("ascend-collapsed-modules") || "{}");
    } catch {
      return {};
    }
  });

  useEffect(() => {
    Promise.all([api.getModules(), api.getProgress()]).then(([m, p]) => {
      setModules(m);
      setProgress(p);
    });
  }, []);

  const toggleModule = (moduleId) => {
    setCollapsedModules((current) => {
      const next = { ...current, [moduleId]: !current[moduleId] };
      localStorage.setItem("ascend-collapsed-modules", JSON.stringify(next));
      return next;
    });
  };

  const completed = new Set(progress.completed_lessons || []);

  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">CURRICULUM</span>
        <h1>Modules</h1>
        <p>Listen, learn, build, break, fix, review, and reflect.</p>
      </header>

      <div className="module-list">
        {modules.map((module) => {
          const lessonIds = (module.lessons || []).map((lesson) => lesson.id);
          const completedCount = lessonIds.filter((id) => completed.has(id)).length;
          const locked = module.status === "locked";
          const collapsed = Boolean(collapsedModules[module.id]);

          return (
            <article className={`module-card ${locked ? "locked" : ""} ${collapsed ? "collapsed" : ""}`} key={module.id}>
              <div className="module-number">{String(module.number).padStart(2, "0")}</div>
              <div className="module-card-content">
                <div className="module-card-title">
                  <div>
                    <span className="eyebrow">{locked ? "PLANNED" : "ACTIVE"}</span>
                    <h2>{module.title}</h2>
                  </div>
                  <div className="module-card-actions">
                    {locked ? <LockKeyhole size={20} /> : <CheckCircle2 size={20} />}
                    <button
                      type="button"
                      className="module-collapse-button"
                      onClick={() => toggleModule(module.id)}
                      aria-expanded={!collapsed}
                      aria-label={`${collapsed ? "Expand" : "Collapse"} ${module.title}`}
                      title={`${collapsed ? "Expand" : "Collapse"} module`}
                    >
                      {collapsed ? <ChevronDown size={20} /> : <ChevronUp size={20} />}
                    </button>
                  </div>
                </div>
                <p>{module.subtitle}</p>

                {!locked && !collapsed && (
                  <div className="lesson-list">
                    {module.lessons.map((lesson) => (
                      <Link className="lesson-row" to={`/lessons/${lesson.id}`} key={lesson.id}>
                        <span className={`lesson-check ${completed.has(lesson.id) ? "done" : ""}`}>
                          {completed.has(lesson.id) ? "✓" : lesson.id}
                        </span>
                        <div>
                          <strong>{lesson.title}</strong>
                          <small>{lesson.summary}</small>
                        </div>
                        <ChevronRight size={18} />
                      </Link>
                    ))}
                  </div>
                )}

                {!collapsed && (
                  <small>
                    {lessonIds.length
                      ? `${completedCount} of ${lessonIds.length} lessons completed`
                      : "Content unlocks as the journey progresses"}
                  </small>
                )}
              </div>
            </article>
          );
        })}
      </div>
    </div>
  );
}
