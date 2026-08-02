import {
  ArrowRight,
  BookOpenCheck,
  CalendarDays,
  FlaskConical,
  MessageCircleQuestion,
  Presentation,
} from "lucide-react";
import { Link } from "react-router-dom";
import {
  WORKSHOP_HANDBOOK,
  WORKSHOP_LABS,
  WORKSHOP_QUESTIONS,
  WORKSHOP_SESSIONS,
} from "../../data/workshopData";

const workshopAreas = [
  {
    to: "/workshop/sessions",
    icon: CalendarDays,
    eyebrow: "SESSIONS",
    title: "Workshop sessions",
    description:
      "Structured notes, concepts, commands, action items, and follow-up learning from each meeting.",
  },
  {
    to: "/workshop/labs",
    icon: FlaskConical,
    eyebrow: "PRACTICE",
    title: "Follow-up labs",
    description:
      "Turn workshop conversations into hands-on exercises using Ascend, Forge, Docker, AWS, and your home lab.",
  },
  {
    to: "/workshop/handbook",
    icon: BookOpenCheck,
    eyebrow: "REFERENCE",
    title: "Engineering handbook",
    description:
      "Keep reusable commands, diagrams, explanations, architecture notes, and lessons learned.",
  },
  {
    to: "/workshop/questions",
    icon: MessageCircleQuestion,
    eyebrow: "NEXT MEETING",
    title: "Questions for Travis",
    description:
      "Capture unclear topics, follow-up ideas, and high-value questions before the next workshop.",
  },
];

export default function WorkshopDashboard() {
  const latestSession = WORKSHOP_SESSIONS.at(-1);

  return (
    <div className="page-stack">
      <section className="workshop-hero">
        <div className="workshop-hero-copy">
          <span className="eyebrow">DEVOPS WORKSHOP</span>
          <h1>Turn every session into lasting progress.</h1>
          <p>
            The Workshop workspace connects your real meetings with structured
            notes, hands-on labs, questions, and a personal engineering
            handbook.
          </p>

          <div className="workshop-hero-actions">
            <Link
              className="primary-button"
              to={`/workshop/sessions/${latestSession.id}`}
            >
              Open latest session
              <ArrowRight size={18} />
            </Link>

            <Link className="secondary-button" to="/workshop/questions">
              Prepare questions
            </Link>
          </div>
        </div>

        <div className="workshop-hero-mark" aria-hidden="true">
          <Presentation size={54} />
          <span>LEARN</span>
          <span>PRACTICE</span>
          <span>RETURN</span>
        </div>
      </section>

      <section className="workshop-status-grid workshop-status-grid-four">
        <article className="workshop-status-card">
          <span>Sessions captured</span>
          <strong>{WORKSHOP_SESSIONS.length}</strong>
          <small>Structured from your meeting transcripts</small>
        </article>

        <article className="workshop-status-card">
          <span>Follow-up labs</span>
          <strong>{WORKSHOP_LABS.length}</strong>
          <small>Practice tied directly to workshop topics</small>
        </article>

        <article className="workshop-status-card">
          <span>Questions prepared</span>
          <strong>{WORKSHOP_QUESTIONS.length}</strong>
          <small>Ready to refine before the next meeting</small>
        </article>

        <article className="workshop-status-card">
          <span>Handbook entries</span>
          <strong>{WORKSHOP_HANDBOOK.length}</strong>
          <small>Reusable engineering reference notes</small>
        </article>
      </section>

      <section className="workshop-latest-session panel">
        <div>
          <span className="eyebrow">LATEST SESSION</span>
          <h2>{latestSession.title}</h2>
          <p>{latestSession.summary}</p>

          <div className="workshop-topic-list">
            {latestSession.topics.slice(0, 5).map((topic) => (
              <span key={topic}>{topic}</span>
            ))}
          </div>
        </div>

        <Link
          className="secondary-button"
          to={`/workshop/sessions/${latestSession.id}`}
        >
          Review session
          <ArrowRight size={17} />
        </Link>
      </section>

      <section className="workshop-area-grid">
        {workshopAreas.map(({ to, icon: Icon, eyebrow, title, description }) => (
          <Link className="workshop-area-card" to={to} key={to}>
            <div className="workshop-area-icon">
              <Icon size={22} />
            </div>

            <div>
              <span className="eyebrow">{eyebrow}</span>
              <h2>{title}</h2>
              <p>{description}</p>
            </div>

            <ArrowRight className="workshop-area-arrow" size={20} />
          </Link>
        ))}
      </section>
    </div>
  );
}
