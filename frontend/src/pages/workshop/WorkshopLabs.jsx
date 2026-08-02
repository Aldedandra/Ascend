import { ArrowRight, CheckCircle2, FlaskConical } from "lucide-react";
import { Link } from "react-router-dom";
import { WORKSHOP_LABS } from "../../data/workshopData";

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

      <section className="workshop-lab-list">
        {WORKSHOP_LABS.map((lab) => (
          <article className="panel workshop-lab-card" key={lab.id}>
            <div className="workshop-lab-card-icon">
              <FlaskConical size={23} />
            </div>

            <div>
              <span className="eyebrow">
                SESSION {String(lab.sessionNumber).padStart(2, "0")}
              </span>
              <h2>{lab.title}</h2>
              <p>{lab.objective}</p>

              <div className="workshop-lab-card-evidence">
                <CheckCircle2 size={16} />
                {lab.evidence.length} evidence items
              </div>
            </div>

            <Link
              className="secondary-button"
              to={`/workshop/sessions/${lab.id}`}
            >
              Open lab
              <ArrowRight size={16} />
            </Link>
          </article>
        ))}
      </section>
    </div>
  );
}
