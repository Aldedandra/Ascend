import { CheckCircle2, FlaskConical, Wrench } from "lucide-react";

export default function WorkshopLabs() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">WORKSHOP PRACTICE</span>
        <h1>Labs</h1>
        <p>
          Practice the tools and workflows discussed in your workshop sessions
          using real projects and your home lab.
        </p>
      </header>

      <section className="panel workshop-empty-state">
        <div className="workshop-empty-icon">
          <FlaskConical size={30} />
        </div>

        <div>
          <span className="eyebrow">LAB FRAMEWORK READY</span>
          <h2>Session-based labs arrive with the workshop content.</h2>
          <p>
            Each lab will include an objective, prerequisites, numbered steps,
            expected evidence, troubleshooting notes, and a completion
            checklist.
          </p>
        </div>
      </section>

      <section className="workshop-preview-grid">
        <article className="panel workshop-preview-card">
          <Wrench size={21} />
          <strong>Build and troubleshoot</strong>
          <p>Use Git, Docker, AWS, Ascend, Forge, and your home server.</p>
        </article>

        <article className="panel workshop-preview-card">
          <CheckCircle2 size={21} />
          <strong>Capture evidence</strong>
          <p>Record commands, screenshots, results, lessons, and follow-up work.</p>
        </article>
      </section>
    </div>
  );
}
