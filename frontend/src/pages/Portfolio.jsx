import {
  Boxes,
  Cloud,
  GitBranch,
  MonitorCog,
  ShieldCheck,
} from "lucide-react";

const portfolioItems = [
  {
    id: "git-history",
    icon: <GitBranch size={22} aria-hidden="true" />,
    title: "Git history",
    body: "Branches, releases, tags, pull requests, and documented recovery exercises.",
  },
  {
    id: "container-journey",
    icon: <Boxes size={22} aria-hidden="true" />,
    title: "Container journey",
    body: "Dockerfiles, Compose architecture, image versions, rollback practice, and troubleshooting notes.",
  },
  {
    id: "aws-deployment",
    icon: <Cloud size={22} aria-hidden="true" />,
    title: "AWS deployment",
    body: "IAM, EC2 or ECS, networking, monitoring, cost controls, and architecture decisions.",
  },
  {
    id: "cicd-reliability",
    icon: <MonitorCog size={22} aria-hidden="true" />,
    title: "CI/CD and reliability",
    body: "Automated builds, deployments, health checks, logs, metrics, alerts, and incident reviews.",
  },
  {
    id: "security-practices",
    icon: <ShieldCheck size={22} aria-hidden="true" />,
    title: "Security practices",
    body: "Secrets, least privilege, HTTPS, vulnerability response, and safe change management.",
  },
];

export default function Portfolio() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PROFESSIONAL ARTIFACTS</span>
        <h1>Your portfolio</h1>
        <p>This area will grow as each module turns learning into evidence.</p>
      </header>

      <section className="portfolio-grid" aria-label="Planned portfolio artifacts">
        {portfolioItems.map((item) => (
          <article className="panel portfolio-card" key={item.id}>
            <div className="stat-icon">{item.icon}</div>
            <h2>{item.title}</h2>
            <p>{item.body}</p>
            <span className="status-pill">Planned</span>
          </article>
        ))}
      </section>

      <section className="panel">
        <span className="eyebrow">CAPSTONE STORY</span>
        <h2>From working application to production-style platform</h2>
        <p>
          Ascend itself becomes the capstone: versioned with Git, containerized,
          deployed, automated, monitored, secured, documented, broken intentionally,
          and recovered.
        </p>
      </section>
    </div>
  );
}
