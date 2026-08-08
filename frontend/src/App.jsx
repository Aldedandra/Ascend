import { Navigate, Route, Routes } from "react-router-dom";
import LaunchTransition from "./components/LaunchTransition";
import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Journal from "./pages/Journal";
import Lesson from "./pages/Lesson";
import Journey from "./pages/Journey";
import Modules from "./pages/Modules";
import Notifications from "./pages/Notifications";
import Portfolio from "./pages/Portfolio";
import Progress from "./pages/Progress";
import WorkshopDashboard from "./pages/workshop/WorkshopDashboard";
import WorkshopHandbook from "./pages/workshop/WorkshopHandbook";
import WorkshopLabs from "./pages/workshop/WorkshopLabs";
import WorkshopQuestions from "./pages/workshop/WorkshopQuestions";
import WorkshopSessionDetail from "./pages/workshop/WorkshopSessionDetail";
import WorkshopSessions from "./pages/workshop/WorkshopSessions";

export default function App() {
  return (
    <>
      <LaunchTransition />

      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/journey" element={<Journey />} />
          <Route path="/modules" element={<Modules />} />
          <Route path="/lessons/:lessonId" element={<Lesson />} />
          <Route path="/progress" element={<Progress />} />
          <Route path="/journal" element={<Journal />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/notifications" element={<Notifications />} />

          <Route path="/workshop" element={<WorkshopDashboard />} />
          <Route path="/workshop/sessions" element={<WorkshopSessions />} />
          <Route
            path="/workshop/sessions/:sessionId"
            element={<WorkshopSessionDetail />}
          />
          <Route path="/workshop/labs" element={<WorkshopLabs />} />
          <Route path="/workshop/handbook" element={<WorkshopHandbook />} />
          <Route path="/workshop/questions" element={<WorkshopQuestions />} />

          <Route path="/labs" element={<Navigate to="/workshop/labs" replace />} />
          <Route
            path="/handbook"
            element={<Navigate to="/workshop/handbook" replace />}
          />
        </Route>
      </Routes>
    </>
  );
}
