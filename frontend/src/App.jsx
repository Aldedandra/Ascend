import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import ComingSoon from "./components/ComingSoon";
import Dashboard from "./pages/Dashboard";
import Journal from "./pages/Journal";
import Lesson from "./pages/Lesson";
import Modules from "./pages/Modules";
import Portfolio from "./pages/Portfolio";
import Progress from "./pages/Progress";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Dashboard />} />
        <Route path="/modules" element={<Modules />} />
        <Route path="/lessons/:lessonId" element={<Lesson />} />
        <Route path="/workshop" element={<ComingSoon eyebrow="WORKSHOP" title="Learn from the work" description="Capture Travis sessions, recordings, questions, action items, and follow-up learning in one connected workspace." items={["Workshop notes", "Questions for Travis", "Action items", "Related lessons"]} />} />
        <Route path="/labs" element={<ComingSoon eyebrow="HANDS-ON PRACTICE" title="Labs" description="Turn every concept into something you can build, break, troubleshoot, explain, and recover." items={["Guided labs", "Break-and-fix exercises", "Rollback practice", "Lab evidence"]} />} />
        <Route path="/handbook" element={<ComingSoon eyebrow="PERSONAL KNOWLEDGE BASE" title="Engineering handbook" description="Build the reference you wish you had: commands, diagrams, postmortems, interview notes, and personal engineering principles." items={["Command references", "Incident reviews", "Architecture notes", "Interview preparation"]} />} />
        <Route path="/progress" element={<Progress />} />
        <Route path="/journal" element={<Journal />} />
        <Route path="/portfolio" element={<Portfolio />} />
      </Route>
    </Routes>
  );
}
