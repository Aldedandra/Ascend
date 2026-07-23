import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
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
        <Route path="/progress" element={<Progress />} />
        <Route path="/journal" element={<Journal />} />
        <Route path="/portfolio" element={<Portfolio />} />
      </Route>
    </Routes>
  );
}
