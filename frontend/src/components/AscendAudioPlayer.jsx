import {
  Headphones,
  Pause,
  Play,
  RotateCcw,
  Square,
  Volume2,
  Mic2,
} from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";

import "../styles/ascend-audio-voice.css";

import {
  ascendSpeech,
  getSpeechProviderLabel,
  isSpeechAvailable,
} from "../services/ascendSpeech";

const SPEED_OPTIONS = [0.8, 1, 1.15, 1.3, 1.5];
const WORDS_PER_MINUTE_AT_1X = 165;
const VOICE_STORAGE_KEY = "ascend-audio-narrator";

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function estimateMinutes(text, rate) {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.ceil(words / (WORDS_PER_MINUTE_AT_1X * rate)));
}

function curatedAppleVoices(voices = []) {
  const english = voices.filter((voice) =>
    String(voice.language || "").toLowerCase().startsWith("en")
  );

  const premium = english.filter((voice) =>
    String(voice.quality || "").toLowerCase() === "premium"
  );

  const preferredNames = ["Ava", "Samantha", "Alex", "Evan", "Allison"];
  const preferred = preferredNames
    .map((name) => english.find((voice) =>
      String(voice.name || "").toLowerCase() === name.toLowerCase()
    ))
    .filter(Boolean);

  const pool = premium.length ? premium : preferred.length ? preferred : english;

  return [...pool]
    .sort((left, right) => {
      const leftPreferred = preferredNames.findIndex(
        (name) => name.toLowerCase() === String(left.name || "").toLowerCase()
      );
      const rightPreferred = preferredNames.findIndex(
        (name) => name.toLowerCase() === String(right.name || "").toLowerCase()
      );
      const leftRank = leftPreferred === -1 ? 999 : leftPreferred;
      const rightRank = rightPreferred === -1 ? 999 : rightPreferred;
      return leftRank - rightRank || String(left.name).localeCompare(String(right.name));
    })
    .slice(0, 8);
}

export default function AscendAudioPlayer({ lesson }) {
  const storageKey = `ascend-audio-${lesson.id}`;
  const [status, setStatus] = useState("idle");
  const [rate, setRate] = useState(() => {
    const stored = Number(localStorage.getItem(`${storageKey}-rate`));
    return SPEED_OPTIONS.includes(stored) ? stored : 1;
  });
  const [characterIndex, setCharacterIndex] = useState(() => {
    const stored = Number(localStorage.getItem(`${storageKey}-position`));
    return Number.isFinite(stored) ? stored : 0;
  });
  const [error, setError] = useState("");
  const [voices, setVoices] = useState([]);
  const [selectedVoiceId, setSelectedVoiceId] = useState(
    () => localStorage.getItem(VOICE_STORAGE_KEY) || ""
  );
  const [voicesLoading, setVoicesLoading] = useState(true);
  const [previewingVoice, setPreviewingVoice] = useState(false);
  const playbackStartIndex = useRef(characterIndex);

  const script = lesson.audio_script || "";
  const speechAvailable = isSpeechAvailable();
  const providerLabel = getSpeechProviderLabel();
  const progress = script.length
    ? clamp((characterIndex / script.length) * 100, 0, 100)
    : 0;
  const remainingText = useMemo(
    () => script.slice(clamp(characterIndex, 0, script.length)),
    [characterIndex, script]
  );
  const estimatedMinutes = useMemo(
    () => estimateMinutes(remainingText || script, rate),
    [remainingText, rate, script]
  );


  useEffect(() => {
    if (!speechAvailable) {
      setVoicesLoading(false);
      return undefined;
    }

    let cancelled = false;

    ascendSpeech.getVoices()
      .then(({ voices: availableVoices = [] }) => {
        if (cancelled) return;

        const curatedVoices = curatedAppleVoices(availableVoices);
        setVoices(curatedVoices);
        setSelectedVoiceId((currentVoiceId) => {
          if (curatedVoices.some((voice) => voice.identifier === currentVoiceId)) {
            return currentVoiceId;
          }

          const preferredDefault =
            curatedVoices.find((voice) => voice.name.toLowerCase() === "ava")
            || curatedVoices.find((voice) => voice.name.toLowerCase() === "samantha")
            || curatedVoices.find((voice) => voice.name.toLowerCase() === "alex");
          const premiumVoice = curatedVoices.find((voice) =>
            voice.quality.toLowerCase() === "premium"
          );
          const bestAvailable = preferredDefault || premiumVoice || curatedVoices[0];
          const nextId = bestAvailable?.identifier || "";

          if (nextId) {
            localStorage.setItem(VOICE_STORAGE_KEY, nextId);
          }

          return nextId;
        });
      })
      .catch((voiceError) => {
        if (!cancelled) {
          setError(voiceError?.message || "Unable to load installed voices.");
        }
      })
      .finally(() => {
        if (!cancelled) setVoicesLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [speechAvailable]);

  useEffect(() => {
    if (selectedVoiceId) {
      localStorage.setItem(VOICE_STORAGE_KEY, selectedVoiceId);
    }
  }, [selectedVoiceId]);

  useEffect(() => {
    localStorage.setItem(`${storageKey}-rate`, String(rate));
  }, [rate, storageKey]);

  useEffect(() => {
    localStorage.setItem(`${storageKey}-position`, String(characterIndex));
  }, [characterIndex, storageKey]);

  useEffect(() => {
    setStatus("idle");
    setError("");
  }, [lesson.id]);

  useEffect(() => {
    if (!speechAvailable) {
      return undefined;
    }

    let stateHandle;
    let progressHandle;
    let errorHandle;
    let disposed = false;

    Promise.all([
      ascendSpeech.addListener("speechStateChanged", ({ state }) => {
        if (disposed) return;
        setStatus(state === "completed" ? "completed" : state);
        if (state === "completed") {
          setCharacterIndex(script.length);
        }
      }),
      ascendSpeech.addListener("speechProgress", ({ characterOffset }) => {
        if (disposed) return;
        setCharacterIndex(
          clamp(
            playbackStartIndex.current + Number(characterOffset || 0),
            0,
            script.length
          )
        );
      }),
      ascendSpeech.addListener("speechError", ({ message }) => {
        if (disposed) return;
        setError(message || "Narration stopped unexpectedly.");
      }),
    ]).then(([stateListener, progressListener, errorListener]) => {
      stateHandle = stateListener;
      progressHandle = progressListener;
      errorHandle = errorListener;
    });

    return () => {
      disposed = true;
      stateHandle?.remove();
      progressHandle?.remove();
      errorHandle?.remove();
      ascendSpeech.stop().catch(() => {});
    };
  }, [lesson.id, script.length, speechAvailable]);

  const startSpeaking = async ({ restart = false } = {}) => {
    if (!speechAvailable) {
      setError("Narration is not supported by this browser or device.");
      return;
    }

    const startIndex = restart ? 0 : characterIndex;
    const text = script.slice(startIndex);

    if (!text.trim()) {
      setCharacterIndex(0);
      await startSpeaking({ restart: true });
      return;
    }

    try {
      setError("");
      playbackStartIndex.current = startIndex;
      if (restart) {
        setCharacterIndex(0);
      }
      await ascendSpeech.speak({
        text,
        rate,
        title: lesson.title,
        lessonId: lesson.id,
        voiceIdentifier: selectedVoiceId,
      });
    } catch (speechError) {
      setError(speechError?.message || "Unable to start narration.");
    }
  };

  const togglePlayback = async () => {
    try {
      setError("");
      if (status === "speaking") {
        await ascendSpeech.pause();
      } else if (status === "paused") {
        await ascendSpeech.resume();
      } else {
        await startSpeaking({ restart: status === "completed" });
      }
    } catch (speechError) {
      setError(speechError?.message || "Unable to control narration.");
    }
  };

  const stopPlayback = async () => {
    try {
      await ascendSpeech.stop();
      setStatus("idle");
    } catch (speechError) {
      setError(speechError?.message || "Unable to stop narration.");
    }
  };

  const restartPlayback = async () => {
    await ascendSpeech.stop().catch(() => {});
    await startSpeaking({ restart: true });
  };

  const handleRateChange = async (nextRate) => {
    setRate(nextRate);
    if (status === "speaking" || status === "paused") {
      await ascendSpeech.stop().catch(() => {});
      setStatus("idle");
      setError("Speed updated. Tap Listen to continue from your saved position.");
    }
  };

  const handleVoiceChange = async (event) => {
    const nextVoiceId = event.target.value;

    if (status === "speaking" || status === "paused") {
      await ascendSpeech.stop().catch(() => {});
      setStatus("idle");
    }

    setSelectedVoiceId(nextVoiceId);
    setError("");
  };

  const previewSelectedVoice = async () => {
    if (!selectedVoiceId) {
      setError("Choose a narrator before previewing a voice.");
      return;
    }

    try {
      setError("");
      setPreviewingVoice(true);
      await ascendSpeech.stop().catch(() => {});
      setStatus("idle");
      await ascendSpeech.previewVoice({
        voiceIdentifier: selectedVoiceId,
        rate,
        text: "Welcome to Ascend. Your next lesson is ready. Keep climbing.",
      });
    } catch (previewError) {
      setError(previewError?.message || "Unable to preview this narrator.");
    } finally {
      window.setTimeout(() => setPreviewingVoice(false), 1200);
    }
  };

  const selectedVoice = voices.find((voice) => voice.identifier === selectedVoiceId);

  const statusLabel = status === "speaking"
    ? "Playing"
    : status === "paused"
      ? "Paused"
      : status === "completed"
        ? "Completed"
        : "Ready";

  return (
    <section className="panel ascend-audio-player">
      <div className="panel-heading ascend-audio-heading">
        <div>
          <span className="eyebrow">ASCEND AUDIO</span>
          <h2>
            <Headphones size={22} />
            {lesson.title}
          </h2>
        </div>
        <span className={`audio-status audio-status-${status}`}>
          {statusLabel}
        </span>
      </div>

      <div className="audio-now-reading">
        <Volume2 size={20} />
        <div>
          <span>{providerLabel}</span>
          <strong>
            {characterIndex > 0 && status !== "completed"
              ? "Continue where you left off"
              : status === "completed"
                ? "Lesson listening complete"
                : "Start this lesson"}
          </strong>
        </div>
      </div>

      <div className="audio-progress-wrap">
        <div className="audio-progress-labels">
          <span>{Math.round(progress)}% listened</span>
          <span>About {estimatedMinutes} min remaining</span>
        </div>
        <div className="audio-progress-track" aria-label="Listening progress">
          <div className="audio-progress-fill" style={{ width: `${progress}%` }} />
        </div>
      </div>

      <div className="audio-primary-controls">
        <button
          className="audio-control-button secondary"
          onClick={restartPlayback}
          title="Restart lesson"
          disabled={!speechAvailable}
        >
          <RotateCcw size={20} />
        </button>
        <button
          className="audio-play-button"
          onClick={togglePlayback}
          disabled={!speechAvailable}
        >
          {status === "speaking" ? <Pause size={28} /> : <Play size={28} fill="currentColor" />}
          <span>
            {status === "speaking"
              ? "Pause"
              : status === "paused"
                ? "Resume"
                : status === "completed"
                  ? "Listen again"
                  : characterIndex > 0
                    ? "Continue"
                    : "Listen"}
          </span>
        </button>
        <button
          className="audio-control-button secondary"
          onClick={stopPlayback}
          title="Stop narration"
          disabled={!speechAvailable}
        >
          <Square size={18} fill="currentColor" />
        </button>
      </div>

      <div className="audio-narrator-panel">
        <div className="audio-narrator-copy">
          <Mic2 size={20} />
          <div>
            <span>Narrator</span>
            <strong>
              {selectedVoice
                ? `${selectedVoice.name} · ${selectedVoice.quality}`
                : voicesLoading
                  ? "Loading installed voices..."
                  : "Choose a voice"}
            </strong>
          </div>
        </div>

        <div className="audio-narrator-controls">
          <label>
            <span className="sr-only">Choose narrator</span>
            <select
              value={selectedVoiceId}
              onChange={handleVoiceChange}
              disabled={voicesLoading || !voices.length}
            >
              {!voices.length && <option value="">No voices found</option>}
              {voices.map((voice) => (
                <option key={voice.identifier} value={voice.identifier}>
                  {voice.name} — {voice.quality} ({voice.language})
                </option>
              ))}
            </select>
          </label>

          <button
            className="secondary-button audio-preview-button"
            onClick={previewSelectedVoice}
            disabled={!selectedVoiceId || previewingVoice}
          >
            <Volume2 size={17} />
            {previewingVoice ? "Previewing..." : "Preview voice"}
          </button>
        </div>
      </div>

      <div className="audio-speed-row">
        <span>Playback speed</span>
        <div className="audio-speed-options">
          {SPEED_OPTIONS.map((option) => (
            <button
              key={option}
              className={rate === option ? "active" : ""}
              onClick={() => handleRateChange(option)}
            >
              {option}×
            </button>
          ))}
        </div>
      </div>

      {!speechAvailable && (
        <p className="audio-note">
          Narration is unavailable in this browser. Open Ascend in a supported browser or the native iPhone app.
        </p>
      )}

      {error && <div className="audio-player-message">{error}</div>}

      <details className="audio-script-details">
        <summary>View narration script</summary>
        <div className="audio-script">{remainingText || script}</div>
      </details>
    </section>
  );
}
