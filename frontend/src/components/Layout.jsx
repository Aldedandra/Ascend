import {
  Award,
  BookOpen,
  FlaskConical,
  Gauge,
  Menu,
  NotebookPen,
  Presentation,
  Route,
  ScrollText,
  X,
} from "lucide-react";
import { useState } from "react";
import { NavLink, Outlet } from "react-router-dom";
import AscendLogo from "./AscendLogo";

const navGroups = [
  {
    label: "Climb",
    items: [
      { to: "/", label: "Dashboard", icon: Gauge },
      { to: "/modules", label: "Journey", icon: BookOpen },
      { to: "/workshop", label: "Workshop", icon: Presentation },
      { to: "/labs", label: "Labs", icon: FlaskConical },
      { to: "/handbook", label: "Handbook", icon: ScrollText },
    ],
  },
  {
    label: "Reflect",
    items: [
      { to: "/journal", label: "Journal", icon: NotebookPen },
      { to: "/portfolio", label: "Portfolio", icon: Award },
      { to: "/progress", label: "Progress", icon: Route },
    ],
  },
];

export default function Layout() {
  const [open, setOpen] = useState(false);

  return (
    <div className="app-shell">
      <aside className={`sidebar ${open ? "sidebar-open" : ""}`}>
        <div className="brand">
          <div className="brand-mark"><AscendLogo compact /></div>
          <div className="brand-copy">
            <strong>ASCEND</strong>
            <span>Keep Climbing.</span>
          </div>
          <button className="icon-button sidebar-close" onClick={() => setOpen(false)} aria-label="Close navigation">
            <X size={20} />
          </button>
        </div>

        <nav className="nav-list">
          {navGroups.map((group) => (
            <div className="nav-group" key={group.label}>
              <span className="nav-group-label">{group.label}</span>
              {group.items.map(({ to, label, icon: Icon }) => (
                <NavLink
                  key={to}
                  to={to}
                  end={to === "/"}
                  onClick={() => setOpen(false)}
                  className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}
                >
                  <Icon size={19} />
                  <span>{label}</span>
                </NavLink>
              ))}
            </div>
          ))}
        </nav>

        <div className="mission-card">
          <span>Ascend principle</span>
          <strong>Every lesson is another step upward.</strong>
          <p>Progress does not require perfection. It requires the next step.</p>
        </div>
      </aside>

      <div className="main-column">
        <header className="topbar">
          <button className="icon-button menu-button" onClick={() => setOpen(true)} aria-label="Open navigation">
            <Menu size={22} />
          </button>
          <div className="topbar-copy">
            <span className="eyebrow">YOUR DEVOPS ASCENT</span>
            <strong>Learn it. Build it. Explain it. Keep climbing.</strong>
          </div>
          <div className="topbar-badge">ASCEND</div>
        </header>
        <main className="main-content">
          <Outlet />
        </main>
      </div>
      {open && <button className="sidebar-overlay" onClick={() => setOpen(false)} aria-label="Close navigation" />}
    </div>
  );
}
