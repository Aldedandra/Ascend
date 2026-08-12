from pathlib import Path

root = Path.home() / "Projects" / "Ascend"
lesson_path = root / "frontend/src/pages/Lesson.jsx"
css_path = root / "frontend/src/styles/global.css"
lesson = lesson_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

if "lesson-back-to-top" not in lesson:
    old = '  ArrowRight,\n} from "lucide-react";'
    new = '  ArrowRight,\n  ArrowUp,\n} from "lucide-react";'
    if old not in lesson:
        raise RuntimeError("Could not find lucide import marker.")
    lesson = lesson.replace(old, new, 1)

    old = '  const [lessonNavigation, setLessonNavigation] = useState({ previous: null, next: null, module: null });\n'
    new = old + '  const [showBackToTop, setShowBackToTop] = useState(false);\n'
    if old not in lesson:
        raise RuntimeError("Could not find lessonNavigation state marker.")
    lesson = lesson.replace(old, new, 1)

    old = '  useEffect(() => {\n    let cancelled = false;\n    api.getModules().then((modules) => {'
    new = '''  useEffect(() => {
    const handleScroll = () => {
      setShowBackToTop(window.scrollY > 650);
    };

    handleScroll();
    window.addEventListener("scroll", handleScroll, { passive: true });

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  useEffect(() => {
    let cancelled = false;
    api.getModules().then((modules) => {'''
    if old not in lesson:
        raise RuntimeError("Could not find useEffect insertion marker.")
    lesson = lesson.replace(old, new, 1)

    old = '      <nav className="lesson-sequence-nav" aria-label="Lesson navigation">'
    new = '''      {activeTab === "lesson" && showBackToTop && (
        <button
          className="lesson-back-to-top"
          type="button"
          aria-label="Back to top of lesson"
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        >
          <ArrowUp size={18} />
          <span>Top</span>
        </button>
      )}

      <nav className="lesson-sequence-nav" aria-label="Lesson navigation">'''
    if old not in lesson:
        raise RuntimeError("Could not find lesson navigation render marker.")
    lesson = lesson.replace(old, new, 1)
    lesson_path.write_text(lesson, encoding="utf-8")
    print("✓ Installed Back to Top behavior in Lesson.jsx.")
else:
    print("✓ Back to Top JSX already installed.")

marker = "Ascend — floating Back to Top control for long lesson notes"
if marker not in css:
    css += '''

/* Ascend — floating Back to Top control for long lesson notes */
.lesson-back-to-top {
  position: fixed;
  right: max(22px, env(safe-area-inset-right));
  bottom: max(22px, calc(env(safe-area-inset-bottom) + 14px));
  z-index: 80;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 10px 14px;
  border: 1px solid rgba(55, 200, 255, 0.38);
  border-radius: 999px;
  color: #eaf9ff;
  background: rgba(7, 28, 48, 0.94);
  box-shadow: 0 12px 30px rgba(0, 0, 0, .28);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  cursor: pointer;
  font: inherit;
  font-size: .82rem;
  font-weight: 800;
}
.lesson-back-to-top:hover {
  border-color: rgba(55, 200, 255, 0.72);
  background: rgba(10, 44, 76, 0.98);
}
.lesson-back-to-top:focus-visible {
  outline: 2px solid #37c8ff;
  outline-offset: 3px;
}
@media (max-width: 600px) {
  .lesson-back-to-top {
    right: max(12px, env(safe-area-inset-right));
    bottom: max(14px, calc(env(safe-area-inset-bottom) + 10px));
    min-width: 44px;
    width: 44px;
    height: 44px;
    justify-content: center;
    padding: 0;
  }
  .lesson-back-to-top span { display: none; }
}
'''
    css_path.write_text(css, encoding="utf-8")
    print("✓ Installed Back to Top styles in global.css.")
else:
    print("✓ Back to Top CSS already installed.")

print("Back to Top installation complete.")
