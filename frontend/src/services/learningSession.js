const SESSION_KEY = "ascend-learning-session-v1";

const EMPTY_SESSION = Object.freeze({
  lessonId: null,
  activeTab: "lesson",
  scrollY: 0,
  audioPosition: 0,
  audioProgress: 0,
  lastOpenedAt: null,
});

function canUseStorage() {
  return typeof window !== "undefined" && Boolean(window.localStorage);
}

export function getLearningSession() {
  if (!canUseStorage()) return { ...EMPTY_SESSION };

  try {
    const stored = JSON.parse(window.localStorage.getItem(SESSION_KEY) || "{}");
    return {
      ...EMPTY_SESSION,
      ...stored,
      scrollY: Number.isFinite(Number(stored.scrollY)) ? Number(stored.scrollY) : 0,
      audioPosition: Number.isFinite(Number(stored.audioPosition)) ? Number(stored.audioPosition) : 0,
      audioProgress: Number.isFinite(Number(stored.audioProgress)) ? Number(stored.audioProgress) : 0,
    };
  } catch {
    return { ...EMPTY_SESSION };
  }
}

export function saveLearningSession(update) {
  const next = {
    ...getLearningSession(),
    ...update,
    lastOpenedAt: update.lastOpenedAt || new Date().toISOString(),
  };

  if (canUseStorage()) {
    window.localStorage.setItem(SESSION_KEY, JSON.stringify(next));
  }

  return next;
}

export function beginLessonSession(lessonId, activeTab = "lesson") {
  const current = getLearningSession();
  const isSameLesson = current.lessonId === lessonId;

  return saveLearningSession({
    lessonId,
    activeTab: isSameLesson ? current.activeTab || activeTab : activeTab,
    scrollY: isSameLesson ? current.scrollY : 0,
    audioPosition: isSameLesson ? current.audioPosition : 0,
    audioProgress: isSameLesson ? current.audioProgress : 0,
  });
}

export function describeLastOpened(isoDate) {
  if (!isoDate) return "Ready when you are";

  const date = new Date(isoDate);
  if (Number.isNaN(date.getTime())) return "Ready when you are";

  const elapsedMinutes = Math.max(0, Math.floor((Date.now() - date.getTime()) / 60000));
  if (elapsedMinutes < 1) return "Just now";
  if (elapsedMinutes < 60) return `${elapsedMinutes} min ago`;

  const elapsedHours = Math.floor(elapsedMinutes / 60);
  if (elapsedHours < 24) return `${elapsedHours} hr${elapsedHours === 1 ? "" : "s"} ago`;

  const elapsedDays = Math.floor(elapsedHours / 24);
  if (elapsedDays === 1) return "Yesterday";
  if (elapsedDays < 7) return `${elapsedDays} days ago`;

  return date.toLocaleDateString(undefined, { month: "short", day: "numeric" });
}
