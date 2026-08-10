import { Bell, BellRing, CheckCircle2, Clock3, Presentation, Smartphone, Trophy } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import {
  cancelDailyLearningReminder,
  getNotificationPermission,
  getPendingNotifications,
  isNativeNotificationsAvailable,
  requestNotificationPermission,
  scheduleDailyLearningReminder,
  sendTestNotification,
} from "../services/ascendNotifications";
import {
  getNotificationPreferences,
  saveNotificationPreferences,
} from "../services/notificationPreferences";
import "../styles/notifications.css";

const DAILY_ID = "ascend.daily-learning";

function permissionLabel(status) {
  if (status === "granted") return "Allowed";
  if (status === "denied") return "Not allowed";
  if (status === "provisional") return "Provisional";
  if (status === "unsupported") return "Native app only";
  return "Not requested";
}

export default function Notifications() {
  const native = useMemo(() => isNativeNotificationsAvailable(), []);
  const [preferences, setPreferences] = useState(getNotificationPreferences);
  const [permission, setPermission] = useState("unknown");
  const [pendingDaily, setPendingDaily] = useState(false);
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState("");
  const [draftDailyTime, setDraftDailyTime] = useState(() => getNotificationPreferences().dailyTime);

  const refreshStatus = async () => {
    if (!native) {
      setPermission("unsupported");
      setPendingDaily(false);
      return;
    }

    try {
      const [permissionResult, pendingResult] = await Promise.all([
        getNotificationPermission(),
        getPendingNotifications(),
      ]);
      setPermission(permissionResult.status || "unknown");
      setPendingDaily(
        (pendingResult.notifications || []).some((item) => item.id === DAILY_ID)
      );
    } catch (error) {
      setMessage(error.message || "Unable to read notification settings.");
    }
  };

  useEffect(() => {
    refreshStatus();
  }, []);

  const savePreferences = (next) => {
    const saved = saveNotificationPreferences(next);
    setPreferences(saved);
  };

  const enablePermission = async () => {
    setBusy(true);
    setMessage("");
    try {
      const result = await requestNotificationPermission();
      setPermission(result.status || "unknown");
      if (result.status === "granted" || result.status === "provisional") {
        setMessage("Notifications are ready on this device.");
      } else {
        setMessage("Notifications are still disabled in iOS Settings.");
      }
    } catch (error) {
      setMessage(error.message || "Unable to request notification permission.");
    } finally {
      setBusy(false);
    }
  };

  const testNotification = async () => {
    setBusy(true);
    setMessage("");
    try {
      if (permission !== "granted" && permission !== "provisional") {
        const result = await requestNotificationPermission();
        setPermission(result.status || "unknown");
        if (result.status !== "granted" && result.status !== "provisional") {
          setMessage("Allow notifications first, then try the test again.");
          return;
        }
      }
      await sendTestNotification();
      setMessage("Test scheduled for about 3 seconds from now.");
    } catch (error) {
      setMessage(error.message || "Unable to schedule the test notification.");
    } finally {
      setBusy(false);
    }
  };

  const toggleDaily = async (enabled) => {
    setBusy(true);
    setMessage("");
    try {
      if (!enabled) {
        await cancelDailyLearningReminder();
        savePreferences({ ...preferences, dailyEnabled: false });
        setPendingDaily(false);
        setMessage("Daily learning reminder turned off.");
        return;
      }

      let currentPermission = permission;
      if (currentPermission !== "granted" && currentPermission !== "provisional") {
        const result = await requestNotificationPermission();
        currentPermission = result.status || "unknown";
        setPermission(currentPermission);
      }

      if (currentPermission !== "granted" && currentPermission !== "provisional") {
        setMessage("Ascend needs notification permission before it can schedule reminders.");
        return;
      }

      const [hour, minute] = preferences.dailyTime.split(":").map(Number);
      await scheduleDailyLearningReminder(hour, minute);
      savePreferences({ ...preferences, dailyEnabled: true });
      setPendingDaily(true);
      setMessage(`Daily learning reminder scheduled for ${formatTime(preferences.dailyTime)}.`);
    } catch (error) {
      setMessage(error.message || "Unable to update the daily reminder.");
    } finally {
      setBusy(false);
    }
  };

  const applyDailyTime = async () => {
    const next = { ...preferences, dailyTime: draftDailyTime };
    savePreferences(next);

    if (!native) return;

    if (!preferences.dailyEnabled) {
      setMessage(`Reminder time saved as ${formatTime(draftDailyTime)}. Turn the daily reminder on when you are ready.`);
      return;
    }

    setBusy(true);
    setMessage("");
    try {
      const [hour, minute] = draftDailyTime.split(":").map(Number);
      await scheduleDailyLearningReminder(hour, minute);
      setPendingDaily(true);
      setMessage(`Reminder moved to ${formatTime(draftDailyTime)}.`);
    } catch (error) {
      setMessage(error.message || "Unable to change the reminder time.");
    } finally {
      setBusy(false);
    }
  };

  const updateNativeTimePart = (part, value) => {
    const [hour24, minute] = draftDailyTime.split(":").map(Number);
    const currentPeriod = hour24 >= 12 ? "PM" : "AM";
    const currentHour12 = hour24 % 12 || 12;

    let nextHour12 = currentHour12;
    let nextMinute = minute;
    let nextPeriod = currentPeriod;

    if (part === "hour") nextHour12 = Number(value);
    if (part === "minute") nextMinute = Number(value);
    if (part === "period") nextPeriod = value;

    let nextHour24 = nextHour12 % 12;
    if (nextPeriod === "PM") nextHour24 += 12;

    setDraftDailyTime(
      `${String(nextHour24).padStart(2, "0")}:${String(nextMinute).padStart(2, "0")}`
    );
  };

  return (
    <div className="page-stack notifications-page">
      <section className="notifications-hero">
        <div className="notifications-hero-icon"><BellRing size={24} /></div>
        <div>
          <span className="eyebrow">NATIVE iPHONE + iPAD</span>
          <h1>Ascend notifications</h1>
          <p>
            Build a steady learning rhythm with reminders that feel like part of Ascend, not noise.
          </p>
        </div>
      </section>

      <section className="notification-status-grid">
        <article className="panel notification-status-card">
          <Smartphone size={20} />
          <div>
            <span>Device support</span>
            <strong>{native ? "Native app detected" : "Browser preview"}</strong>
          </div>
        </article>
        <article className="panel notification-status-card">
          <Bell size={20} />
          <div>
            <span>Permission</span>
            <strong>{permissionLabel(permission)}</strong>
          </div>
        </article>
        <article className="panel notification-status-card">
          <CheckCircle2 size={20} />
          <div>
            <span>Daily reminder</span>
            <strong>{pendingDaily ? "Scheduled" : "Not scheduled"}</strong>
          </div>
        </article>
      </section>

      <section className="panel notification-control-panel">
        <div className="panel-heading compact-heading">
          <div>
            <span className="eyebrow">PERMISSION + TEST</span>
            <h2>Connect Ascend to iOS notifications</h2>
          </div>
        </div>
        <p className="notification-helper">
          Permission is requested only when you choose to enable it. The test notification appears a few seconds after you tap the button.
        </p>
        <div className="notification-button-row">
          <button className="secondary-button" type="button" onClick={enablePermission} disabled={busy || !native}>
            Allow notifications
          </button>
          <button className="primary-button" type="button" onClick={testNotification} disabled={busy || !native}>
            Send test notification
          </button>
        </div>
      </section>

      <section className="panel notification-control-panel">
        <div className="notification-setting-row">
          <div className="notification-setting-copy">
            <span className="notification-setting-icon"><Clock3 size={19} /></span>
            <div>
              <strong>Daily learning reminder</strong>
              <p>A simple prompt to return to your current lesson and keep your ascent moving.</p>
            </div>
          </div>
          <label className="notification-toggle">
            <input
              type="checkbox"
              checked={preferences.dailyEnabled}
              onChange={(event) => toggleDaily(event.target.checked)}
              disabled={busy || !native}
            />
            <span aria-hidden="true" />
            <em>{preferences.dailyEnabled ? "On" : "Off"}</em>
          </label>
        </div>

        <div className="notification-time-row notification-time-editor">
          <div className="notification-time-copy">
            <label htmlFor={native ? "daily-reminder-hour" : "daily-reminder-time"}>Reminder time</label>
            <small>Choose the full time, then tap Save time.</small>
          </div>

          {native ? (
            <div className="notification-native-time-controls" aria-label="Daily reminder time">
              <div className="notification-select-wrap notification-time-select">
                <select
                  id="daily-reminder-hour"
                  value={toTwelveHour(draftDailyTime).hour}
                  onChange={(event) => updateNativeTimePart("hour", event.target.value)}
                  disabled={busy}
                  aria-label="Hour"
                >
                  {Array.from({ length: 12 }, (_, index) => index + 1).map((hour) => (
                    <option key={hour} value={hour}>{hour}</option>
                  ))}
                </select>
              </div>
              <span className="notification-time-colon">:</span>
              <div className="notification-select-wrap notification-time-select">
                <select
                  value={toTwelveHour(draftDailyTime).minute}
                  onChange={(event) => updateNativeTimePart("minute", event.target.value)}
                  disabled={busy}
                  aria-label="Minute"
                >
                  {Array.from({ length: 60 }, (_, minute) => minute).map((minute) => (
                    <option key={minute} value={minute}>{String(minute).padStart(2, "0")}</option>
                  ))}
                </select>
              </div>
              <div className="notification-select-wrap notification-time-period">
                <select
                  value={toTwelveHour(draftDailyTime).period}
                  onChange={(event) => updateNativeTimePart("period", event.target.value)}
                  disabled={busy}
                  aria-label="AM or PM"
                >
                  <option value="AM">AM</option>
                  <option value="PM">PM</option>
                </select>
              </div>
            </div>
          ) : (
            <div className="notification-time-input-wrap">
              <input
                id="daily-reminder-time"
                type="time"
                value={draftDailyTime}
                onChange={(event) => setDraftDailyTime(event.target.value)}
                disabled={busy}
              />
            </div>
          )}

          <div className="notification-time-actions">
            <small>{formatTime(draftDailyTime)} every day</small>
            <button
              className="secondary-button notification-save-time"
              type="button"
              onClick={applyDailyTime}
              disabled={busy || !native || draftDailyTime === preferences.dailyTime}
            >
              Save time
            </button>
          </div>
        </div>
      </section>

      <section className="panel notification-control-panel">
        <div className="panel-heading compact-heading">
          <div>
            <span className="eyebrow">MILESTONES + WORKSHOP</span>
            <h2>Choose what deserves a notification</h2>
          </div>
        </div>

        <div className="notification-preference-list">
          <div className="notification-setting-row notification-preference-item">
            <div className="notification-setting-copy">
              <span className="notification-setting-icon"><Trophy size={19} /></span>
              <div>
                <strong>Learning milestones</strong>
                <p>Celebrate lesson and module completions with the Ascend signature sound.</p>
              </div>
            </div>

            <label className="notification-toggle">
              <input
                type="checkbox"
                checked={preferences.milestoneEnabled}
                disabled={!native}
                onChange={(event) =>
                  savePreferences({ ...preferences, milestoneEnabled: event.target.checked })
                }
              />
              <span aria-hidden="true" />
              <em>{preferences.milestoneEnabled ? "On" : "Off"}</em>
            </label>
          </div>

          <div className="notification-setting-row notification-preference-item">
            <div className="notification-setting-copy">
              <span className="notification-setting-icon"><Presentation size={19} /></span>
              <div>
                <strong>Workshop reminders</strong>
                <p>Keep this preference ready for the Workshop Center sprint and scheduled session reminders.</p>
              </div>
            </div>

            <label className="notification-toggle">
              <input
                type="checkbox"
                checked={preferences.workshopEnabled}
                disabled={!native}
                onChange={(event) =>
                  savePreferences({ ...preferences, workshopEnabled: event.target.checked })
                }
              />
              <span aria-hidden="true" />
              <em>{preferences.workshopEnabled ? "On" : "Off"}</em>
            </label>
          </div>
        </div>
      </section>

      {!native && (
        <div className="notification-note">
          Open this page in the installed Ascend iPhone/iPad app to request permission, send a test, and schedule reminders.
        </div>
      )}

      {message && <div className="notification-feedback" role="status">{message}</div>}
      <section className="panel notification-control-panel notification-smart-panel">
        <div className="panel-heading compact-heading">
          <div>
            <span className="eyebrow">SMART REMINDER</span>
            <h2>Resume Your Climb</h2>
          </div>
        </div>

        <div className="notification-setting-row notification-smart-setting">
          <div className="notification-setting-copy">
            <span className="notification-setting-icon"><BellRing size={19} /></span>
            <div>
              <strong>Resume reminders</strong>
              <p>
                If you leave Ascend during a lesson, save your place and send one gentle reminder later.
                Returning to Ascend automatically clears the pending reminder.
              </p>
            </div>
          </div>

          <label className="notification-toggle">
            <input
              type="checkbox"
              checked={preferences.resumeEnabled}
              disabled={!native}
              onChange={(event) =>
                savePreferences({ ...preferences, resumeEnabled: event.target.checked })
              }
            />
            <span aria-hidden="true" />
            <em>{preferences.resumeEnabled ? "On" : "Off"}</em>
          </label>
        </div>

        <div className={`notification-delay-row ${preferences.resumeEnabled ? "" : "is-disabled"}`}>
          <div>
            <label htmlFor="resume-reminder-delay">Reminder delay</label>
            <small>How long Ascend should wait before nudging you to continue.</small>
          </div>
          <div className="notification-select-wrap">
            <select
              id="resume-reminder-delay"
              value={preferences.resumeDelayMinutes}
              disabled={!preferences.resumeEnabled}
              onChange={(event) =>
                savePreferences({ ...preferences, resumeDelayMinutes: Number(event.target.value) })
              }
            >
              <option value={60}>1 hour</option>
              <option value={120}>2 hours</option>
              <option value={240}>4 hours</option>
              <option value={720}>12 hours</option>
              <option value={1440}>1 day</option>
            </select>
          </div>
        </div>
      </section>

    </div>
  );
}

function toTwelveHour(value) {
  const [hour24, minute] = value.split(":").map(Number);
  return {
    hour: hour24 % 12 || 12,
    minute,
    period: hour24 >= 12 ? "PM" : "AM",
  };
}

function formatTime(value) {
  const [hour, minute] = value.split(":").map(Number);
  return new Intl.DateTimeFormat(undefined, {
    hour: "numeric",
    minute: "2-digit",
  }).format(new Date(2000, 0, 1, hour, minute));
}
