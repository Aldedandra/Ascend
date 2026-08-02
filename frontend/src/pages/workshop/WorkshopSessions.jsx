import { ArrowRight, CalendarDays, Clock3 } from "lucide-react";
import { Link } from "react-router-dom";
import { WORKSHOP_SESSIONS } from "../../data/workshopData";

export default function WorkshopSessions() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">DEVOPS WORKSHOP</span>
        <h1>Sessions</h1>
        <p>
          Review what Travis taught, reconnect the concepts, practice the
          workflow, and prepare better questions for the next meeting.
        </p>
      </header>

      <section className="workshop-session-list">
        {WORKSHOP_SESSIONS.map((session) => (
          <Link
            className="workshop-session-card"
            to={`/workshop/sessions/${session.id}`}
            key={session.id}
          >
            <div className="workshop-session-number">
              {String(session.number).padStart(2, "0")}
            </div>

            <div className="workshop-session-main">
              <div className="workshop-session-meta">
                <span>
                  <CalendarDays size={14} />
                  {session.date}
                </span>
                <span>
                  <Clock3 size={14} />
                  {session.duration}
                </span>
              </div>

              <h2>{session.title}</h2>
              <p>{session.summary}</p>

              <div className="workshop-topic-list">
                {session.topics.map((topic) => (
                  <span key={topic}>{topic}</span>
                ))}
              </div>
            </div>

            <div className="workshop-session-open">
              <span>{session.status}</span>
              <ArrowRight size={21} />
            </div>
          </Link>
        ))}
      </section>
    </div>
  );
}
