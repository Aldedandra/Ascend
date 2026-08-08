import { Capacitor, registerPlugin } from "@capacitor/core";

const NativeNotifications = registerPlugin("AscendNotifications");

const DAILY_REMINDER_ID = "ascend.daily-learning";
const TEST_NOTIFICATION_ID = "ascend.test";

export function isNativeNotificationsAvailable() {
  return Capacitor.isNativePlatform();
}

export async function getNotificationPermission() {
  if (!isNativeNotificationsAvailable()) {
    return { status: "unsupported" };
  }

  return NativeNotifications.checkPermission();
}

export async function requestNotificationPermission() {
  if (!isNativeNotificationsAvailable()) {
    return { status: "unsupported" };
  }

  return NativeNotifications.requestPermission();
}

export async function sendTestNotification() {
  if (!isNativeNotificationsAvailable()) {
    throw new Error("Ascend notifications are available in the native iPhone/iPad app.");
  }

  return NativeNotifications.schedule({
    id: TEST_NOTIFICATION_ID,
    title: "Ascend",
    body: "Your next step is waiting. Elevate every day.",
    delaySeconds: 3,
  });
}

export async function scheduleDailyLearningReminder(hour, minute) {
  if (!isNativeNotificationsAvailable()) {
    throw new Error("Ascend notifications are available in the native iPhone/iPad app.");
  }

  return NativeNotifications.scheduleDaily({
    id: DAILY_REMINDER_ID,
    title: "Time to Ascend",
    body: "A few focused minutes today can move your journey forward.",
    hour,
    minute,
  });
}

export async function cancelDailyLearningReminder() {
  if (!isNativeNotificationsAvailable()) return;
  return NativeNotifications.cancel({ ids: [DAILY_REMINDER_ID] });
}

export async function getPendingNotifications() {
  if (!isNativeNotificationsAvailable()) return { notifications: [] };
  return NativeNotifications.getPending();
}

const RESUME_REMINDER_ID = "ascend.resume-your-climb";

export async function scheduleResumeLearningReminder(delayMinutes = 120) {
  if (!isNativeNotificationsAvailable()) return { scheduled: false };

  const safeMinutes = Math.max(1, Number(delayMinutes) || 120);
  await NativeNotifications.cancel({ ids: [RESUME_REMINDER_ID] });
  return NativeNotifications.schedule({
    id: RESUME_REMINDER_ID,
    title: "Resume Your Climb",
    body: "Your place is saved. Pick up where you left off when you're ready.",
    delaySeconds: Math.round(safeMinutes * 60),
  });
}

export async function cancelResumeLearningReminder() {
  if (!isNativeNotificationsAvailable()) return;
  return NativeNotifications.cancel({ ids: [RESUME_REMINDER_ID] });
}


export async function sendMilestoneNotification({ title, body, id }) {
  if (!isNativeNotificationsAvailable()) return { scheduled: false };

  const permission = await getNotificationPermission();
  if (permission.status !== "granted" && permission.status !== "provisional") {
    return { scheduled: false, permission: permission.status };
  }

  return NativeNotifications.schedule({
    id: id || `ascend.milestone.${Date.now()}`,
    title: title || "Ascend Milestone",
    body: body || "Another step upward. Keep going.",
    delaySeconds: 1,
  });
}
