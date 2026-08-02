import {
  ArrowLeft,
  BookOpenCheck,
  CheckCircle2,
  ClipboardList,
  FileText,
  FlaskConical,
  HelpCircle,
  ListChecks,
  TerminalSquare,
} from "lucide-react";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getWorkshopSession } from "../../data/workshopData";

const tabs = [
  { id: "overview", label: "Overview", icon: FileText },
  { id: "notes", label: "Notes", icon: ClipboardList },
  { id: "commands", label: "Commands", icon: TerminalSquare },
  { id: "lab", label: "Lab", icon: FlaskConical },
  { id: "handbook", label: "Handbook", icon: BookOpenCheck },
  { id: "questions", label: "Questions", icon: HelpCircle },
  { id: "actions", label: "Actions", icon: ListChecks },
];

export default function WorkshopSessionDetail() {
  const { sessionId } = useParams();
  const [activeTab, setActiveTab] = useState("overview");
  const session = getWorkshopSession(sessionId);

  useEffect(() => {
    setActiveTab("overview");
  }, [sessionId]);

  if (!session) {
    return (
      <div className="page-stack">
        <div className="error-card">Workshop session not found.</div>
        <Link className="text-button" to="/workshop/sessions">
          ← Back to sessions
        </Link>
      </div>
    );
  }

  return (
    <div className="page-stack">
      <Link className="text-button workshop-back-link" to="/workshop/sessions">
        <ArrowLeft size={17} />
        Back to sessions
      </Link>

      <header className="workshop-session-hero">
        <div>
          <span className="eyebrow">
            WORKSHOP SESSION {String(session.number).padStart(2, "0")}
          </span>
          <h1>{session.title}</h1>
          <p>{session.summary}</p>

          <div className="workshop-session-hero-meta">
            <span>{session.date}</span>
            <span>{session.duration}</span>
            <span>{session.status}</span>
          </div>
        </div>

        <div className="workshop-session-hero-number">
          {String(session.number).padStart(2, "0")}
        </div>
      </header>

      <div className="workshop-tab-row">
        {tabs.map(({ id, label, icon: Icon }) => (
          <button
            type="button"
            className={activeTab === id ? "active" : ""}
            onClick={() => setActiveTab(id)}
            key={id}
          >
            <Icon size={16} />
            {label}
          </button>
        ))}
      </div>

      {activeTab === "overview" && (
        <div className="workshop-detail-stack">
          <section className="panel workshop-session-overview">
            {session.overview.map((section) => (
              <article key={section.heading}>
                <h2>{section.heading}</h2>
                <p>{section.body}</p>
              </article>
            ))}
          </section>

          <section className="panel">
            <span className="eyebrow">KEY CONCEPTS</span>
            <div className="workshop-concept-grid">
              {session.keyConcepts.map((concept) => (
                <article className="workshop-concept-card" key={concept.term}>
                  <strong>{concept.term}</strong>
                  <p>{concept.definition}</p>
                </article>
              ))}
            </div>
          </section>

          <section className="panel">
            <span className="eyebrow">RELATED CURRICULUM</span>
            <div className="workshop-related-list">
              {session.relatedLessons.map((lesson) => (
                <span key={lesson}>{lesson}</span>
              ))}
            </div>
          </section>
        </div>
      )}

      {activeTab === "notes" && (
        <section className="panel">
          <span className="eyebrow">SESSION NOTES</span>
          <h2>What to remember</h2>

          <ul className="workshop-check-list">
            {session.notes.map((note) => (
              <li key={note}>
                <CheckCircle2 size={18} />
                <span>{note}</span>
              </li>
            ))}
          </ul>

          <div className="workshop-review-block">
            <span className="eyebrow">REVIEW QUESTIONS</span>
            <ol>
              {session.reviewQuestions.map((question) => (
                <li key={question}>{question}</li>
              ))}
            </ol>
          </div>
        </section>
      )}

      {activeTab === "commands" && (
        <section className="workshop-command-list">
          {session.commands.map((item) => (
            <article className="panel workshop-command-card" key={item.label}>
              <div>
                <span className="eyebrow">COMMAND</span>
                <h2>{item.label}</h2>
                <p>{item.explanation}</p>
              </div>

              <pre>
                <code>{item.command}</code>
              </pre>

              {item.warning && (
                <div className="workshop-command-warning">{item.warning}</div>
              )}
            </article>
          ))}
        </section>
      )}

      {activeTab === "lab" && (
        <section className="panel workshop-lab-detail">
          <span className="eyebrow">FOLLOW-UP LAB</span>
          <h2>{session.lab.title}</h2>
          <p className="workshop-lead">{session.lab.objective}</p>

          <div className="workshop-lab-columns">
            <div>
              <h3>Prerequisites</h3>
              <ul>
                {session.lab.prerequisites.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>

            <div>
              <h3>Evidence to capture</h3>
              <ul>
                {session.lab.evidence.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
          </div>

          <h3>Lab steps</h3>
          <ol className="workshop-lab-steps">
            {session.lab.steps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ol>
        </section>
      )}

      {activeTab === "handbook" && (
        <section className="workshop-handbook-grid">
          {session.handbookEntries.map((entry) => (
            <article className="panel workshop-handbook-entry" key={entry.title}>
              <span className="eyebrow">{entry.category}</span>
              <h2>{entry.title}</h2>
              <p>{entry.summary}</p>
            </article>
          ))}
        </section>
      )}

      {activeTab === "questions" && (
        <section className="panel">
          <span className="eyebrow">QUESTIONS FOR TRAVIS</span>
          <h2>Bring these into a future session</h2>

          <ol className="workshop-question-list">
            {session.questionsForTravis.map((question) => (
              <li key={question}>{question}</li>
            ))}
          </ol>
        </section>
      )}

      {activeTab === "actions" && (
        <section className="panel">
          <span className="eyebrow">ACTION ITEMS</span>
          <h2>Turn the session into progress</h2>

          <ul className="workshop-action-list">
            {session.actionItems.map((item) => (
              <li key={item}>
                <span className="workshop-action-box" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
