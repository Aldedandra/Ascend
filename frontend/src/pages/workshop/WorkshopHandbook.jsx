import { ArrowRight, BookOpenCheck } from "lucide-react";
import { Link } from "react-router-dom";
import { WORKSHOP_HANDBOOK } from "../../data/workshopData";

export default function WorkshopHandbook() {
  const categories = [...new Set(WORKSHOP_HANDBOOK.map((entry) => entry.category))];

  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PERSONAL KNOWLEDGE BASE</span>
        <h1>Engineering handbook</h1>
        <p>
          Reusable reference notes extracted from work you actually performed
          and conversations you actually had.
        </p>
      </header>

      <div className="workshop-topic-list workshop-category-list">
        {categories.map((category) => (
          <span key={category}>{category}</span>
        ))}
      </div>

      <section className="workshop-handbook-grid">
        {WORKSHOP_HANDBOOK.map((entry) => (
          <article className="panel workshop-handbook-entry" key={entry.id}>
            <div className="workshop-handbook-entry-icon">
              <BookOpenCheck size={20} />
            </div>
            <span className="eyebrow">{entry.category}</span>
            <h2>{entry.title}</h2>
            <p>{entry.summary}</p>

            <Link
              className="text-button"
              to={`/workshop/sessions/${entry.sessionId}`}
            >
              From Session {String(entry.sessionNumber).padStart(2, "0")}
              <ArrowRight size={15} />
            </Link>
          </article>
        ))}
      </section>
    </div>
  );
}
