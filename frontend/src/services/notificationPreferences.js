const STORAGE_KEY = "ascend.notificationPreferences.v1";

export const DEFAULT_NOTIFICATION_PREFERENCES = Object.freeze({
  dailyEnabled: false,
  dailyTime: "19:00",
  resumeEnabled: false,
  resumeDelayMinutes: 120,
  milestoneEnabled: false,
  workshopEnabled: false,
});

function canUseStorage() {
  return typeof window !== "undefined" && Boolean(window.localStorage);
}

export function getNotificationPreferences() {
  if (!canUseStorage()) return { ...DEFAULT_NOTIFICATION_PREFERENCES };

  try {
    const saved = JSON.parse(window.localStorage.getItem(STORAGE_KEY) || "{}");
    return {
      ...DEFAULT_NOTIFICATION_PREFERENCES,
      ...saved,
      dailyEnabled: Boolean(saved.dailyEnabled),
      resumeEnabled: Boolean(saved.resumeEnabled),
      milestoneEnabled: Boolean(saved.milestoneEnabled),
      workshopEnabled: Boolean(saved.workshopEnabled),
      resumeDelayMinutes: Number(saved.resumeDelayMinutes) || 120,
      dailyTime: saved.dailyTime || "19:00",
    };
  } catch {
    return { ...DEFAULT_NOTIFICATION_PREFERENCES };
  }
}

export function saveNotificationPreferences(update) {
  const next = {
    ...getNotificationPreferences(),
    ...update,
  };

  if (canUseStorage()) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  }

  return next;
}

export function notificationsPreferenceKey() {
  return STORAGE_KEY;
}
