import { useCallback, useEffect, useRef, useState } from "react";
import {
  beginLessonSession,
  getLearningSession,
  saveLearningSession,
} from "../services/learningSession";
import {
  cancelResumeLearningReminder,
  scheduleResumeLearningReminder,
} from "../services/ascendNotifications";
import { getNotificationPreferences } from "../services/notificationPreferences";

export default function useLearningSession(lessonId) {
  const [session, setSession] = useState(() => beginLessonSession(lessonId));
  const saveTimerRef = useRef(null);
  const restoredRef = useRef(false);

  useEffect(() => {
    const next = beginLessonSession(lessonId);
    setSession(next);
    restoredRef.current = false;

    const frame = window.requestAnimationFrame(() => {
      window.scrollTo({ top: next.scrollY || 0, behavior: "auto" });
      restoredRef.current = true;
    });

    return () => window.cancelAnimationFrame(frame);
  }, [lessonId]);

  useEffect(() => {
    const handleScroll = () => {
      if (!restoredRef.current) return;

      window.clearTimeout(saveTimerRef.current);
      saveTimerRef.current = window.setTimeout(() => {
        const next = saveLearningSession({ lessonId, scrollY: window.scrollY });
        setSession(next);
      }, 180);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });

    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.clearTimeout(saveTimerRef.current);
      saveLearningSession({ lessonId, scrollY: window.scrollY });
    };
  }, [lessonId]);

  const setActiveTab = useCallback((activeTab) => {
    const next = saveLearningSession({ lessonId, activeTab, scrollY: window.scrollY });
    setSession(next);
  }, [lessonId]);

  const updateAudioProgress = useCallback(({ position, progress }) => {
    const next = saveLearningSession({
      lessonId,
      activeTab: "audio",
      audioPosition: Number(position) || 0,
      audioProgress: Number(progress) || 0,
    });
    setSession(next);
  }, [lessonId]);

  useEffect(() => {
    const handleVisibilityChange = async () => {
      if (document.visibilityState === "hidden") {
        try {
          const prefs = getNotificationPreferences();
          if (prefs.resumeEnabled) {
            await scheduleResumeLearningReminder(prefs.resumeDelayMinutes);
          }
        } catch {
          // Notification scheduling should never interrupt learning.
        }
      } else if (document.visibilityState === "visible") {
        try {
          await cancelResumeLearningReminder();
        } catch {
          // Safe no-op if native notifications are unavailable.
        }
      }
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);
    return () => document.removeEventListener("visibilitychange", handleVisibilityChange);
  }, [lessonId]);

  const refresh = useCallback(() => setSession(getLearningSession()), []);

  return { session, setActiveTab, updateAudioProgress, refresh };
}
