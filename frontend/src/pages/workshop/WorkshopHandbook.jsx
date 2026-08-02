import { BookOpenCheck, Boxes, Network, TerminalSquare } from "lucide-react";

const handbookAreas = [
  {
    icon: TerminalSquare,
    title: "Commands",
    description: "Reusable CLI commands with context and examples.",
  },
  {
    icon: Boxes,
    title: "Tools and services",
    description: "Docker, ECR, ECS, AWS CLI, Terraform, and future topics.",
  },
  {
    icon: Network,
    title: "Architecture notes",
    description: "Request flows, deployment diagrams, and system relationships.",
  },
];

export default function WorkshopHandbook() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PERSONAL KNOWLEDGE BASE</span>
        <h1>Engineering handbook</h1>
        <p>
          Build the reference you wish you had: concise, practical, and tied to
          work you have actually performed.
        </p>
      </header>

      <section className="panel workshop-empty-state">
        <div className="workshop-empty-icon">
          <BookOpenCheck size={30} />
        </div>

        <div>
          <span className="eyebrow">HANDBOOK READY</span>
          <h2>Your first entries will be generated from workshop sessions.</h2>
          <p>
            Important commands, definitions, architecture explanations, and
            lessons learned will be extracted into permanent reference notes.
          </p>
        </div>
      </section>

      <section className="workshop-preview-grid three-column-preview">
        {handbookAreas.map(({ icon: Icon, title, description }) => (
          <article className="panel workshop-preview-card" key={title}>
            <Icon size={21} />
            <strong>{title}</strong>
            <p>{description}</p>
          </article>
        ))}
      </section>
    </div>
  );
}
