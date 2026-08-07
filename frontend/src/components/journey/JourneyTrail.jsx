import {
  Activity,
  Boxes,
  Box,
  Braces,
  Check,
  ChevronRight,
  Cloud,
  Code2,
  GitBranch,
  LockKeyhole,
  SlidersHorizontal,
  TerminalSquare,
  Workflow,
} from "lucide-react";

const ICONS = {
  linux: TerminalSquare,
  "software-design": Boxes,
  programming: Code2,
  "source-control": GitBranch,
  containerization: Box,
  orchestration: Boxes,
  cicd: Workflow,
  configuration: SlidersHorizontal,
  cloud: Cloud,
  iac: Braces,
  observability: Activity,
};

function stateLabel(state) {
  if (state === "complete") return "Complete";
  if (state === "current") return "Current";
  if (state === "next") return "Next up";
  return "Ahead";
}

export default function JourneyTrail({ steps, selectedId, onSelect }) {
  return (
    <div className="trail-map" role="list" aria-label="DevOps Journey roadmap">
      <div className="trail-route" aria-hidden="true" />

      {steps.map((item, index) => {
        const Icon = ICONS[item.id] || LockKeyhole;
        const selected = item.id === selectedId;
        return (
          <button
            className={`trail-stop trail-stop-${index % 2 === 0 ? "left" : "right"} ${item.state} ${selected ? "selected" : ""}`}
            key={item.id}
            onClick={() => onSelect(item.id)}
            type="button"
            role="listitem"
            aria-current={item.state === "current" ? "step" : undefined}
          >
            <span className="trail-stop-node" aria-hidden="true">
              {item.state === "complete" ? <Check size={19} /> : <span>{item.number}</span>}
            </span>

            <span className="trail-stop-card">
              <span className="trail-stop-icon"><Icon size={20} /></span>
              <span className="trail-stop-copy">
                <span className="trail-stop-meta">
                  <span>{stateLabel(item.state)}</span>
                  {item.percent > 0 && <span>{item.percent}%</span>}
                </span>
                <strong>{item.focus}</strong>
                <small>{item.title}</small>
              </span>
              <ChevronRight className="trail-stop-chevron" size={18} />
            </span>
          </button>
        );
      })}

      <div className="trail-summit" aria-hidden="true">
        <span>SUMMIT</span>
        <strong>Operate with confidence.</strong>
      </div>
    </div>
  );
}
