import {
  ArrowLeft,
  Award,
  BookOpen,
  BookOpenCheck,
  CalendarDays,
  FlaskConical,
  Gauge,
  Bell,
  Menu,
  MessageCircleQuestion,
  NotebookPen,
  Presentation,
  Route,
  X,
} from "lucide-react";
import { Capacitor } from "@capacitor/core";
import { useState } from "react";
import { NavLink, Outlet, useLocation, useNavigate } from "react-router-dom";
import AscendLogo from "./AscendLogo";
import WorkspaceSwitcher from "./WorkspaceSwitcher";

const curriculumGroups = [
  {
    label: "Climb",
    items: [
      { to: "/", label: "Dashboard", icon: Gauge },
      { to: "/journey", label: "Journey", icon: Route },
      { to: "/modules", label: "Modules", icon: BookOpen },
    ],
  },
  {
    label: "Reflect",
    items: [
      { to: "/journal", label: "Journal", icon: NotebookPen },
      { to: "/portfolio", label: "Portfolio", icon: Award },
      { to: "/progress", label: "Progress", icon: Route },
      { to: "/notifications", label: "Notifications", icon: Bell },
    ],
  },
];

const workshopGroups = [
  {
    label: "Workshop",
    items: [
      { to: "/workshop", label: "Workshop Home", icon: Presentation },
      { to: "/workshop/sessions", label: "Sessions", icon: CalendarDays },
      { to: "/workshop/labs", label: "Labs", icon: FlaskConical },
      { to: "/workshop/handbook", label: "Handbook", icon: BookOpenCheck },
      {
        to: "/workshop/questions",
        label: "Questions for Travis",
        icon: MessageCircleQuestion,
      },
    ],
  },
];

export default function Layout() {
  const location = useLocation();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);

  const isWorkshop = location.pathname.startsWith("/workshop");
  const native = Capacitor.isNativePlatform();
  const pageAlreadyOwnsBackNavigation =
    location.pathname.startsWith("/lessons/") ||
    /^\/workshop\/sessions\/[^/]+$/.test(location.pathname);

  const dashboardBackRoutes = new Set([
    "/journey",
    "/modules",
    "/journal",
    "/portfolio",
    "/progress",
    "/notifications",
  ]);

  const workshopBackRoutes = new Set([
    "/workshop/sessions",
    "/workshop/labs",
    "/workshop/handbook",
    "/workshop/questions",
  ]);

  const nativeBackTarget = (() => {
    if (dashboardBackRoutes.has(location.pathname)) {
      return { to: "/", label: "Dashboard" };
    }

    if (workshopBackRoutes.has(location.pathname)) {
      return { to: "/workshop", label: "Workshop" };
    }

    return null;
  })();

  const showNativeBack =
    native &&
    location.pathname !== "/" &&
    !pageAlreadyOwnsBackNavigation;

  const goBack = () => {
    if (nativeBackTarget) {
      navigate(nativeBackTarget.to);
      return;
    }

    if (window.history.length > 1) {
      navigate(-1);
      return;
    }

    navigate(isWorkshop ? "/workshop" : "/");
  };
  const navGroups = isWorkshop ? workshopGroups : curriculumGroups;

  const topbar = isWorkshop
    ? {
        eyebrow: "DEVOPS WORKSHOP",
        message: "Capture the lesson. Practice the work. Bring better questions.",
        badge: "WORKSHOP",
      }
    : {
        eyebrow: "YOUR DEVOPS ASCENT",
        message: "Learn it. Build it. Explain it. Keep climbing.",
        badge: "ASCEND",
      };

  const mission = isWorkshop
    ? {
        eyebrow: "Workshop principle",
        title: "Turn every conversation into practical growth.",
        body: "Capture the why, practice the commands, and return with better questions.",
      }
    : {
        eyebrow: "Ascend principle",
        title: "Every lesson is another step upward.",
        body: "Progress does not require perfection. It requires the next step.",
      };

  return (
    <div className="app-shell">
      <aside className={`sidebar ${open ? "sidebar-open" : ""}`}>
        <div className="brand">
          <div className="brand-header">
            <div className="brand-identity" aria-label="Ascend">
              <div className="brand-mark">
                <AscendLogo compact />
              </div>
              <div className="brand-copy">
                <strong>ASCEND</strong>
                <span>Elevate every day.</span>
              </div>
            </div>

            <button
              className="icon-button sidebar-close"
              onClick={() => setOpen(false)}
              aria-label="Close navigation"
            >
              <X size={20} />
            </button>
          </div>

          <WorkspaceSwitcher onNavigate={() => setOpen(false)} />
        </div>

        <nav className="nav-list">
          {navGroups.map((group) => (
            <div className="nav-group" key={group.label}>
              <span className="nav-group-label">{group.label}</span>

              {group.items.map(({ to, label, icon: Icon }) => (
                <NavLink
                  key={to}
                  to={to}
                  end={to === "/" || to === "/workshop"}
                  onClick={() => setOpen(false)}
                  className={({ isActive }) =>
                    `nav-link ${isActive ? "active" : ""}`
                  }
                >
                  <Icon size={19} />
                  <span>{label}</span>
                </NavLink>
              ))}
            </div>
          ))}
        </nav>

        <div className="mission-card">
          <span>{mission.eyebrow}</span>
          <strong>{mission.title}</strong>
          <p>{mission.body}</p>
        </div>
      </aside>

      <div className="main-column">
        <header className="topbar">
          <button
            className="icon-button menu-button"
            onClick={() => setOpen(true)}
            aria-label="Open navigation"
          >
            <Menu size={22} />
          </button>

          <div className="topbar-copy">
            <span className="eyebrow">{topbar.eyebrow}</span>
            <strong>{topbar.message}</strong>
          </div>

          <div className="topbar-badge">{topbar.badge}</div>
        </header>

        <main className="main-content">
          {showNativeBack ? (
            <button className="native-page-back" type="button" onClick={goBack}>
              <ArrowLeft size={17} />
              <span>{nativeBackTarget?.label || "Back"}</span>
            </button>
          ) : null}
          <Outlet />
        </main>
      </div>

      {open && (
        <button
          className="sidebar-overlay"
          onClick={() => setOpen(false)}
          aria-label="Close navigation"
        />
      )}
    </div>
  );
}
