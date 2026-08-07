import {
  BookOpen,
  Check,
  ChevronDown,
  Presentation,
} from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const workspaces = [
  {
    id: "curriculum",
    title: "The Journey",
    subtitle: "Core DevOps curriculum",
    icon: BookOpen,
    path: "/",
  },
  {
    id: "workshop",
    title: "DevOps Workshop",
    subtitle: "Real-world sessions with Travis",
    icon: Presentation,
    path: "/workshop",
  },
];

export default function WorkspaceSwitcher({ onNavigate }) {
  const location = useLocation();
  const navigate = useNavigate();
  const menuRef = useRef(null);
  const [open, setOpen] = useState(false);

  const activeId = location.pathname.startsWith("/workshop")
    ? "workshop"
    : "curriculum";

  const activeWorkspace = workspaces.find(
    (workspace) => workspace.id === activeId
  );

  useEffect(() => {
    const handlePointerDown = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setOpen(false);
      }
    };

    document.addEventListener("pointerdown", handlePointerDown);

    return () => {
      document.removeEventListener("pointerdown", handlePointerDown);
    };
  }, []);

  const chooseWorkspace = (workspace) => {
    setOpen(false);
    navigate(workspace.path);
    onNavigate?.();
  };

  const ActiveIcon = activeWorkspace.icon;

  return (
    <div className="workspace-switcher" ref={menuRef}>
      <span className="workspace-kicker">Learning space</span>

      <button
        type="button"
        className={`workspace-trigger ${open ? "open" : ""}`}
        onClick={() => setOpen((current) => !current)}
        aria-expanded={open}
        aria-haspopup="menu"
      >
        <span className="workspace-trigger-icon">
          <ActiveIcon size={18} />
        </span>

        <span className="workspace-trigger-copy">
          <strong>{activeWorkspace.title}</strong>
          <span>{activeWorkspace.subtitle}</span>
        </span>

        <ChevronDown
          className="workspace-chevron"
          size={18}
          aria-hidden="true"
        />
      </button>

      {open && (
        <div className="workspace-menu" role="menu">
          <span className="workspace-menu-label">Choose learning space</span>

          {workspaces.map((workspace) => {
            const Icon = workspace.icon;
            const isActive = workspace.id === activeId;

            return (
              <button
                type="button"
                className={`workspace-option ${isActive ? "active" : ""}`}
                key={workspace.id}
                onClick={() => chooseWorkspace(workspace)}
                role="menuitem"
              >
                <span className="workspace-option-icon">
                  <Icon size={18} />
                </span>

                <span className="workspace-option-copy">
                  <strong>{workspace.title}</strong>
                  <span>{workspace.subtitle}</span>
                </span>

                {isActive && <Check size={17} aria-label="Current workspace" />}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}
