import {
  ArrowRight,
  BookOpenCheck,
  Check,
  CircleDot,
  Compass,
  Flag,
  Mountain,
  Route,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import JourneyTrail from "../components/journey/JourneyTrail";
import { ascendExtensions, journeyRoadmap } from "../data/journeyRoadmap";
import { api } from "../services/api";
import "../styles/journey-map.css";

function moduleProgress(module, completed) {
  const lessons = module?.lessons || [];
  if (!lessons.length) return 0;
  const finished = lessons.filter((lesson) => completed.has(lesson.id)).length;
  return Math.round((finished / lessons.length) * 100);
}

function firstIncompleteLesson(module, completed) {
  return module?.lessons?.find((lesson) => !completed.has(lesson.id)) || module?.lessons?.[0] || null;
}

export default function Modules() {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState({ completed_lessons: [] });
  const [selectedId, setSelectedId] = useState("linux");

  useEffect(() => {
    Promise.all([api.getModules(), api.getProgress()]).then(([m, p]) => {
      setModules(m);
      setProgress(p);
    });
  }, []);

  const completed = useMemo(
    () => new Set(progress.completed_lessons || []),
    [progress.completed_lessons]
  );

  const moduleById = useMemo(
    () => new Map(modules.map((module) => [String(module.id), module])),
    [modules]
  );

  const foundation = moduleById.get("module-0");
  const foundationPercent = moduleProgress(foundation, completed);
  const foundationNextLesson = firstIncompleteLesson(foundation, completed);

  const roadmapSteps = useMemo(() => {
    const raw = journeyRoadmap.map((step) => {
      const module = step.moduleId ? moduleById.get(step.moduleId) : null;
      const percent = moduleProgress(module, completed);
      const complete = Boolean(module?.lessons?.length) && percent === 100;
      return { ...step, module, percent, complete };
    });

    const firstIncompleteIndex = raw.findIndex((step) => !step.complete);

    return raw.map((step, index) => {
      let state = "planned";
      if (step.complete) state = "complete";
      else if (foundationPercent === 100 && index === firstIncompleteIndex) state = "current";
      else if (foundationPercent < 100 && index === 0) state = "next";
      return { ...step, state };
    });
  }, [moduleById, completed, foundationPercent]);

  const completedMilestones = roadmapSteps.filter((step) => step.state === "complete").length;
  const selected = roadmapSteps.find((step) => step.id === selectedId) || roadmapSteps[0];
  const selectedLesson = firstIncompleteLesson(selected?.module, completed);

  return (
    <div className="page-stack journey-v2-page">
      <header className="journey-v2-hero">
        <div>
          <span className="eyebrow">THE JOURNEY</span>
          <h1>See the mountain. Climb the next step.</h1>
          <p>
            This is your DevOps roadmap, based on the learning path Travis shared and
            connected to the lessons, labs, workshops, and projects you complete in Ascend.
          </p>
        </div>
        <div className="journey-v2-summary">
          <Route size={21} />
          <strong>{completedMilestones}/11</strong>
          <span>roadmap milestones</span>
        </div>
      </header>

      <section className={`basecamp-v2 ${foundationPercent === 100 ? "complete" : "current"}`}>
        <div className="basecamp-v2-icon"><Mountain size={26} /></div>
        <div className="basecamp-v2-copy">
          <div className="basecamp-v2-topline">
            <span className="eyebrow">BASE CAMP · MODULE 0</span>
            <span className="basecamp-state">
              {foundationPercent === 100 ? <Check size={14} /> : <CircleDot size={14} />}
              {foundationPercent === 100 ? "Foundation complete" : "You are here"}
            </span>
          </div>
          <h2>{foundation?.title || "DevOps Foundations and Systems Thinking"}</h2>
          <p>{foundation?.subtitle || "Build the mindset before learning the tools."}</p>
          <div className="basecamp-v2-progress">
            <div className="progress-track">
              <div className="progress-fill" style={{ width: `${foundationPercent}%` }} />
            </div>
            <strong>{foundationPercent}%</strong>
          </div>
        </div>
        {foundationNextLesson && (
          <Link className="button primary basecamp-v2-action" to={`/lessons/${foundationNextLesson.id}`}>
            {foundationPercent > 0 ? "Continue Base Camp" : "Start Base Camp"}
            <ArrowRight size={17} />
          </Link>
        )}
      </section>

      <section className="journey-v2-shell">
        <div className="journey-v2-heading">
          <div>
            <span className="eyebrow">YOUR DEVOPS ROADMAP</span>
            <h2>The trail ahead</h2>
            <p>Tap any milestone to understand what it teaches and how it connects to your Ascend curriculum.</p>
          </div>
          <div className="journey-v2-legend" aria-label="Roadmap legend">
            <span><i className="complete" /> Complete</span>
            <span><i className="current" /> Current</span>
            <span><i className="next" /> Next up</span>
            <span><i /> Ahead</span>
          </div>
        </div>

        <div className="journey-v2-layout">
          <JourneyTrail steps={roadmapSteps} selectedId={selected?.id} onSelect={setSelectedId} />

          {selected && (
            <aside className={`milestone-detail ${selected.state}`} aria-live="polite">
              <div className="milestone-detail-number">{String(selected.number).padStart(2, "0")}</div>
              <span className="eyebrow">{selected.title}</span>
              <h2>{selected.focus}</h2>
              <p>{selected.description}</p>

              <div className="milestone-outcome">
                <Flag size={18} />
                <div>
                  <span>WHAT SUCCESS LOOKS LIKE</span>
                  <strong>{selected.outcome}</strong>
                </div>
              </div>

              {selected.module ? (
                <div className="milestone-module">
                  <div className="milestone-module-heading">
                    <BookOpenCheck size={18} />
                    <div>
                      <span>ASCEND CURRICULUM</span>
                      <strong>Module {selected.module.number}: {selected.module.title}</strong>
                    </div>
                  </div>
                  {selected.module.lessons?.length ? (
                    <>
                      <div className="milestone-progress-row">
                        <div className="progress-track">
                          <div className="progress-fill" style={{ width: `${selected.percent}%` }} />
                        </div>
                        <span>{selected.percent}%</span>
                      </div>
                      {selectedLesson && (
                        <Link className="milestone-action" to={`/lessons/${selectedLesson.id}`}>
                          {selected.percent > 0 ? "Continue this milestone" : "Open first lesson"}
                          <ArrowRight size={17} />
                        </Link>
                      )}
                    </>
                  ) : (
                    <div className="milestone-planned">
                      <Compass size={17} />
                      <span>Curriculum mapped. Lessons will unlock as the Journey expands.</span>
                    </div>
                  )}
                </div>
              ) : (
                <div className="milestone-planned standalone">
                  <Compass size={17} />
                  <span>This roadmap skill will be reinforced across Journey lessons and Workshop labs.</span>
                </div>
              )}
            </aside>
          )}
        </div>
      </section>

      <section className="journey-v2-extensions">
        <div className="journey-v2-heading compact">
          <div>
            <span className="eyebrow">ASCEND EXTENSIONS</span>
            <h2>Skills that travel with you.</h2>
            <p>Security and the capstone are not side quests. They reinforce everything on the roadmap.</p>
          </div>
        </div>
        <div className="journey-v2-extension-grid">
          {ascendExtensions.map((item) => {
            const module = moduleById.get(item.moduleId);
            const Icon = item.id === "security" ? ShieldCheck : Sparkles;
            return (
              <article className="journey-v2-extension-card" key={item.id}>
                <div className="journey-v2-extension-icon"><Icon size={22} /></div>
                <div>
                  <span className="eyebrow">{module ? `MODULE ${module.number}` : "ASCEND"}</span>
                  <h3>{item.title}</h3>
                  <p>{item.description}</p>
                </div>
              </article>
            );
          })}
        </div>
      </section>
    </div>
  );
}
