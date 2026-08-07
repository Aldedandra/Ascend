import {
  Headphones,
  Pause,
  Play,
  RotateCcw,
  RotateCw,
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
import { formatForNarration } from "../services/narrationFormatter";

const SPEED_OPTIONS = [0.8, 0.9, 1, 1.15, 1.3, 1.5];
const WORDS_PER_MINUTE_AT_1X = 165;
const SEEK_SECONDS = 15;
const VOICE_STORAGE_KEY = "ascend-audio-narrator";
const RATE_STORAGE_KEY = "ascend-audio-playback-speed";

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function estimateMinutes(text, rate) {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.ceil(words / (WORDS_PER_MINUTE_AT_1X * rate)));
}

function estimateSeconds(text, rate) {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  if (!words) return 0;
  return Math.max(1, Math.round((words / (WORDS_PER_MINUTE_AT_1X * rate)) * 60));
}

function formatClock(totalSeconds) {
  const safeSeconds = Math.max(0, Math.round(totalSeconds || 0));
  const minutes = Math.floor(safeSeconds / 60);
  const seconds = safeSeconds % 60;
  return `${minutes}:${String(seconds).padStart(2, "0")}`;
}

function snapToWordBoundary(text, index) {
  if (!text.length) return 0;

  const safeIndex = clamp(Math.round(index), 0, text.length);
  if (safeIndex === 0 || safeIndex === text.length) {
    return safeIndex;
  }

  const before = text.lastIndexOf(" ", safeIndex);
  const after = text.indexOf(" ", safeIndex);

  if (before < 0) return after < 0 ? safeIndex : after + 1;
  if (after < 0) return before + 1;

  return safeIndex - before <= after - safeIndex ? before + 1 : after + 1;
}

export default function AscendAudioPlayer({ lesson, onProgress }) {
  const storageKey = `ascend-audio-${lesson.id}`;
  const [status, setStatus] = useState("idle");
  const [rate, setRate] = useState(() => {
    const lessonRate = Number(localStorage.getItem(`${storageKey}-rate`));
    const globalRate = Number(localStorage.getItem(RATE_STORAGE_KEY));
    if (SPEED_OPTIONS.includes(lessonRate)) return lessonRate;
    if (SPEED_OPTIONS.includes(globalRate)) return globalRate;
    return 0.8;
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
  const [scrubProgress, setScrubProgress] = useState(null);
  const playbackStartIndex = useRef(characterIndex);
  const narrationMapRef = useRef(null);
  const seekInFlightRef = useRef(false);
  const characterIndexRef = useRef(characterIndex);

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
  const totalEstimatedSeconds = useMemo(
    () => estimateSeconds(script, rate),
    [script, rate]
  );
  const displayedProgress = scrubProgress ?? progress;
  const elapsedEstimatedSeconds = Math.round(
    (displayedProgress / 100) * totalEstimatedSeconds
  );
  const remainingEstimatedSeconds = Math.max(
    0,
    totalEstimatedSeconds - elapsedEstimatedSeconds
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

        setVoices(availableVoices);
        setSelectedVoiceId((currentVoiceId) => {
          if (availableVoices.some((voice) => voice.identifier === currentVoiceId)) {
            return currentVoiceId;
          }

          const alexPremium = availableVoices.find((voice) =>
            voice.name.toLowerCase() === "alex"
            && voice.quality.toLowerCase() === "premium"
          );
          const premiumVoice = availableVoices.find((voice) =>
            voice.quality.toLowerCase() === "premium"
          );
          const bestAvailable = alexPremium || premiumVoice || availableVoices[0];
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
    localStorage.setItem(RATE_STORAGE_KEY, String(rate));
  }, [rate, storageKey]);

  useEffect(() => {
    localStorage.setItem(`${storageKey}-position`, String(characterIndex));
    onProgress?.({ position: characterIndex, progress });
  }, [characterIndex, onProgress, progress, storageKey]);

  useEffect(() => {
    characterIndexRef.current = characterIndex;
  }, [characterIndex]);

  useEffect(() => {
    const savedPosition = Number(localStorage.getItem(`${storageKey}-position`));
    const lessonRate = Number(localStorage.getItem(`${storageKey}-rate`));
    const globalRate = Number(localStorage.getItem(RATE_STORAGE_KEY));

    setCharacterIndex(Number.isFinite(savedPosition) ? savedPosition : 0);
    setRate(
      SPEED_OPTIONS.includes(lessonRate)
        ? lessonRate
        : SPEED_OPTIONS.includes(globalRate)
          ? globalRate
          : 0.8
    );
    setScrubProgress(null);
    setStatus("idle");
    setError("");
  }, [lesson.id, storageKey]);

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
        const relativeNarrationOffset = Number(characterOffset || 0);
        const relativeSourceOffset = narrationMapRef.current
          ? narrationMapRef.current.sourceIndexForNarrationIndex(relativeNarrationOffset)
          : relativeNarrationOffset;

        setCharacterIndex(
          clamp(
            playbackStartIndex.current + relativeSourceOffset,
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
    const sourceText = script.slice(startIndex);
    const formattedNarration = formatForNarration(sourceText);
    const text = formattedNarration.text;

    if (!sourceText.trim()) {
      setCharacterIndex(0);
      await startSpeaking({ restart: true });
      return;
    }

    try {
      setError("");
      playbackStartIndex.current = startIndex;
      narrationMapRef.current = formattedNarration;
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

  const seekToCharacterIndex = async (nextCharacterIndex, { autoplay = false } = {}) => {
    if (seekInFlightRef.current || !script.length) return;

    seekInFlightRef.current = true;
    const snappedIndex = snapToWordBoundary(
      script,
      clamp(nextCharacterIndex, 0, script.length)
    );

    // Update the UI immediately. This also prevents a late progress callback from
    // the old utterance from becoming the basis of the next seek.
    characterIndexRef.current = snappedIndex;
    playbackStartIndex.current = snappedIndex;
    narrationMapRef.current = null;
    setCharacterIndex(snappedIndex);
    setScrubProgress(null);
    setError("");

    try {
      if (autoplay && snappedIndex < script.length) {
        const sourceText = script.slice(snappedIndex);
        const formattedNarration = formatForNarration(sourceText);
        playbackStartIndex.current = snappedIndex;
        narrationMapRef.current = formattedNarration;

        // Let the native plugin replace the current utterance atomically. Calling
        // stop() first can deliver a late completion/cancel callback from the old
        // utterance after the replacement begins, which was causing seeks to jump
        // to 100%.
        await ascendSpeech.speak({
          text: formattedNarration.text,
          rate,
          title: lesson.title,
          lessonId: lesson.id,
          voiceIdentifier: selectedVoiceId,
        });
      } else {
        await ascendSpeech.stop().catch(() => {});
        setStatus(snappedIndex >= script.length ? "completed" : "idle");
      }
    } catch (seekError) {
      setError(seekError?.message || "Unable to seek narration.");
    } finally {
      seekInFlightRef.current = false;
    }
  };

  const seekBySeconds = async (seconds) => {
    if (!script.length || !totalEstimatedSeconds) return;

    const wasPlaying = status === "speaking";
    const baseIndex = characterIndexRef.current;
    const characterDelta = (seconds / totalEstimatedSeconds) * script.length;
    const nextIndex = baseIndex + characterDelta;

    await seekToCharacterIndex(nextIndex, { autoplay: wasPlaying });
  };

  const commitScrub = async (explicitProgress = scrubProgress) => {
    const progressValue = Number(explicitProgress);
    if (!Number.isFinite(progressValue) || !script.length) return;

    const wasPlaying = status === "speaking";
    const nextIndex = (clamp(progressValue, 0, 100) / 100) * script.length;
    await seekToCharacterIndex(nextIndex, { autoplay: wasPlaying });
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
        text: "Hello! I'm Alex, your Ascend narrator. Let's keep climbing.",
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
          <span>
            {formatClock(elapsedEstimatedSeconds)} · {Math.round(displayedProgress)}%
          </span>
          <span>
            -{formatClock(remainingEstimatedSeconds)} · about {estimatedMinutes} min
          </span>
        </div>

        <div className="audio-scrubber-wrap">
          <input
            className="audio-progress-scrubber"
            type="range"
            min="0"
            max="100"
            step="0.1"
            value={displayedProgress}
            aria-label="Seek through lesson narration"
            onChange={(event) => setScrubProgress(Number(event.target.value))}
            onPointerUp={(event) => commitScrub(Number(event.currentTarget.value))}
            onKeyUp={(event) => {
              if (["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) {
                commitScrub(Number(event.currentTarget.value));
              }
            }}
            onBlur={(event) => {
              if (scrubProgress !== null) {
                commitScrub(Number(event.currentTarget.value));
              }
            }}
            disabled={!speechAvailable || !script.length}
            style={{ "--audio-progress": `${displayedProgress}%` }}
          />
        </div>
      </div>

      <div className="audio-primary-controls audio-transport-controls">
        <button
          className="audio-control-button audio-seek-button"
          onClick={() => seekBySeconds(-SEEK_SECONDS)}
          title={`Go back ${SEEK_SECONDS} seconds`}
          aria-label={`Go back ${SEEK_SECONDS} seconds`}
          disabled={!speechAvailable || !script.length || characterIndex <= 0}
        >
          <RotateCcw size={24} />
          <span>{SEEK_SECONDS}</span>
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
          className="audio-control-button audio-seek-button"
          onClick={() => seekBySeconds(SEEK_SECONDS)}
          title={`Skip forward ${SEEK_SECONDS} seconds`}
          aria-label={`Skip forward ${SEEK_SECONDS} seconds`}
          disabled={!speechAvailable || !script.length || characterIndex >= script.length}
        >
          <RotateCw size={24} />
          <span>{SEEK_SECONDS}</span>
        </button>
      </div>

      <div className="audio-secondary-actions">
        <button
          className="audio-text-action"
          onClick={stopPlayback}
          disabled={!speechAvailable || status === "idle"}
        >
          <Square size={14} fill="currentColor" />
          Stop
        </button>
        <button
          className="audio-text-action"
          onClick={() => seekToCharacterIndex(0, { autoplay: status === "speaking" })}
          disabled={!speechAvailable || characterIndex <= 0}
        >
          <RotateCcw size={15} />
          Start over
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
