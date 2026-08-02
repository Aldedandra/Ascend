import { CalendarDays, FileText, Sparkles } from "lucide-react";

export default function WorkshopSessions() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">DEVOPS WORKSHOP</span>
        <h1>Sessions</h1>
        <p>
          Every meeting will become a structured session pack you can review,
          practice, and build upon.
        </p>
      </header>

      <section className="panel workshop-empty-state">
        <div className="workshop-empty-icon">
          <CalendarDays size={30} />
        </div>

        <div>
          <span className="eyebrow">READY FOR PHASE 2</span>
          <h2>Your previous workshop sessions will appear here.</h2>
          <p>
            The transcripts you already shared will be converted into clean
            summaries, concepts, commands, labs, review questions, action
            items, and questions for Travis.
          </p>
        </div>
      </section>

      <section className="workshop-preview-grid">
        <article className="panel workshop-preview-card">
          <FileText size={21} />
          <strong>Structured session notes</strong>
          <p>Summary, concepts, terminology, commands, and workflows.</p>
        </article>

        <article className="panel workshop-preview-card">
          <Sparkles size={21} />
          <strong>Connected follow-up</strong>
          <p>Labs, handbook entries, action items, and curriculum links.</p>
        </article>
      </section>
    </div>
  );
}
