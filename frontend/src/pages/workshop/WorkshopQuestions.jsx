import { ArrowRight, MessageCircleQuestion } from "lucide-react";
import { Link } from "react-router-dom";
import { WORKSHOP_QUESTIONS } from "../../data/workshopData";

export default function WorkshopQuestions() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PREPARE THE NEXT CONVERSATION</span>
        <h1>Questions for Travis</h1>
        <p>
          A focused backlog of questions generated from your sessions, labs,
          projects, and areas of uncertainty.
        </p>
      </header>

      <section className="workshop-question-list-page">
        {WORKSHOP_QUESTIONS.map((item, index) => (
          <article className="panel workshop-question-item" key={item.id}>
            <div className="workshop-question-item-number">
              {String(index + 1).padStart(2, "0")}
            </div>

            <div>
              <span className="eyebrow">
                FROM SESSION {String(item.sessionNumber).padStart(2, "0")}
              </span>
              <h2>{item.question}</h2>
              <p>{item.sessionTitle}</p>
            </div>

            <Link
              className="icon-button"
              to={`/workshop/sessions/${item.sessionId}`}
              aria-label={`Open ${item.sessionTitle}`}
            >
              <ArrowRight size={18} />
            </Link>
          </article>
        ))}
      </section>

      <section className="panel workshop-question-tip">
        <MessageCircleQuestion size={23} />
        <div>
          <strong>Before the next meeting</strong>
          <p>
            Choose the highest-value questions, add the context behind each one,
            and note what you have already tried or researched.
          </p>
        </div>
      </section>
    </div>
  );
}
