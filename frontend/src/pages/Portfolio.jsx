import { Boxes, Cloud, GitBranch, MonitorCog, ShieldCheck } from "lucide-react";

const items = [
  { icon: GitBranch, title: "Git history", body: "Branches, releases, tags, pull requests, and documented recovery exercises." },
  { icon: Boxes, title: "Container journey", body: "Dockerfiles, Compose architecture, image versions, rollback practice, and troubleshooting notes." },
  { icon: Cloud, title: "AWS deployment", body: "IAM, EC2 or ECS, networking, monitoring, cost controls, and architecture decisions." },
  { icon: MonitorCog, title: "CI/CD and reliability", body: "Automated builds, deployments, health checks, logs, metrics, alerts, and incident reviews." },
  { icon: ShieldCheck, title: "Security practices", body: "Secrets, least privilege, HTTPS, vulnerability response, and safe change management." },
];

export default function Portfolio() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PROFESSIONAL ARTIFACTS</span>
        <h1>Your portfolio</h1>
        <p>This area will grow as each module turns learning into evidence.</p>
      </header>

      <section className="portfolio-grid">
        {items.map(({ icon: Icon, title, body }) => (
          <article className="panel portfolio-card" key={title}>
            <div className="stat-icon"><Icon size={22} /></div>
            <h2>{title}</h2>
            <p>{body}</p>
            <span className="status-pill">Planned</span>
          </article>
        ))}
      </section>

      <section className="panel">
        <span className="eyebrow">CAPSTONE STORY</span>
        <h2>From working application to production-style platform</h2>
        <p>
          The Journey Hub itself becomes the capstone: versioned with Git, containerized,
          deployed, automated, monitored, secured, documented, broken intentionally, and recovered.
        </p>
      </section>
    </div>
  );
}
