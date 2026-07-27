import { ArrowUpRight, Mountain } from "lucide-react";

export default function ComingSoon({ eyebrow, title, description, items = [] }) {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">{eyebrow}</span>
        <h1>{title}</h1>
        <p>{description}</p>
      </header>

      <section className="panel coming-soon-panel">
        <div className="coming-soon-icon"><Mountain size={28} /></div>
        <div>
          <span className="eyebrow">NEXT ASCENT</span>
          <h2>This section is prepared for the next release.</h2>
          <p>
            The navigation is live now so Ascend already reflects the unified learning platform we designed.
            We will connect the data and workflows without disrupting your existing lessons.
          </p>
        </div>
      </section>

      <section className="feature-preview-grid">
        {items.map((item) => (
          <article className="panel feature-preview-card" key={item}>
            <ArrowUpRight size={18} />
            <strong>{item}</strong>
          </article>
        ))}
      </section>
    </div>
  );
}
