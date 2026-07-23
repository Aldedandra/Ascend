import {
  Award,
  BookOpen,
  Gauge,
  GraduationCap,
  Menu,
  NotebookPen,
  Route,
  X,
} from "lucide-react";
import { useState } from "react";
import { NavLink, Outlet } from "react-router-dom";

const navItems = [
  { to: "/", label: "Dashboard", icon: Gauge },
  { to: "/modules", label: "Modules", icon: BookOpen },
  { to: "/progress", label: "Progress", icon: Route },
  { to: "/journal", label: "Journal", icon: NotebookPen },
  { to: "/portfolio", label: "Portfolio", icon: Award },
];

export default function Layout() {
  const [open, setOpen] = useState(false);

  return (
    <div className="app-shell">
      <aside className={`sidebar ${open ? "sidebar-open" : ""}`}>
        <div className="brand">
          <div className="brand-mark"><GraduationCap size={22} /></div>
          <div>
            <strong>The Journey</strong>
            <span>DevOps Learning Hub</span>
          </div>
          <button className="icon-button sidebar-close" onClick={() => setOpen(false)}>
            <X size={20} />
          </button>
        </div>

        <nav className="nav-list">
          {navItems.map(({ to, label, icon: Icon }) => (
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
        </nav>

        <div className="mission-card">
          <span>Mission</span>
          <strong>Become someone you're proud of.</strong>
          <p>Stop comparing. Start becoming.</p>
        </div>
      </aside>

      <div className="main-column">
        <header className="topbar">
          <button className="icon-button menu-button" onClick={() => setOpen(true)}>
            <Menu size={22} />
          </button>
          <div>
            <span className="eyebrow">CURRENT QUEST</span>
            <strong>Build the engineer. The opportunities will follow.</strong>
          </div>
        </header>
        <main className="main-content">
          <Outlet />
        </main>
      </div>
      {open && <button className="sidebar-overlay" onClick={() => setOpen(false)} />}
    </div>
  );
}
