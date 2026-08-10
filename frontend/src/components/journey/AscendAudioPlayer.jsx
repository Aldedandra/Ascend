import {
  Headphones, LoaderCircle, Pause, Play, RotateCcw, RotateCw, Square, Mic2
} from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";
import { api } from "../services/api";
import "../styles/ascend-audio-voice.css";

const SPEED_OPTIONS = [0.8, 0.9, 1, 1.15, 1.3, 1.5];
const SEEK_SECONDS = 15;
const NARRATOR_KEY = "ascend-elevenlabs-narrator";
const RATE_KEY = "ascend-audio-playback-speed";

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function formatClock(seconds) {
  const safe = Math.max(0, Math.round(Number(seconds) || 0));
  return `${Math.floor(safe / 60)}:${String(safe % 60).padStart(2, "0")}`;
}

export default function AscendAudioPlayer({ lesson, onProgress }) {
  const audioRef = useRef(null);
  const storageKey = `ascend-elevenlabs-${lesson.id}`;
  const [narratorId, setNarratorId] = useState(
    () => localStorage.getItem(NARRATOR_KEY) || "bella"
  );
  const [narrators, setNarrators] = useState([
    { id: "bella", name: "Bella", description: "Clear & Professional" },
    { id: "brian", name: "Brian", description: "Deep & Calm" },
  ]);
  const [rate, setRate] = useState(() => {
    const stored = Number(localStorage.getItem(RATE_KEY));
    return SPEED_OPTIONS.includes(stored) ? stored : 0.8;
  });
  const [audioUrl, setAudioUrl] = useState("");
  const [status, setStatus] = useState("loading");
  const [duration, setDuration] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const [scrubTime, setScrubTime] = useState(null);
  const [error, setError] = useState("");
  const [generationNote, setGenerationNote] = useState("");

  const displayTime = scrubTime ?? currentTime;
  const progress = duration ? clamp((displayTime / duration) * 100, 0, 100) : 0;
  const selectedNarrator = useMemo(
    () => narrators.find((n) => n.id === narratorId) || narrators[0],
    [narratorId, narrators]
  );

  useEffect(() => {
    api.getAscendNarrators()
      .then((data) => data?.narrators?.length && setNarrators(data.narrators))
      .catch(() => {});
  }, []);

  useEffect(() => {
    let cancelled = false;
    const prepare = async () => {
      setStatus("loading");
      setError("");
      setGenerationNote("");
      setAudioUrl("");
      try {
        const state = await api.getElevenLabsLessonAudioStatus(lesson.id, narratorId);
        let metadata = state.metadata;
        if (!state.ready) {
          setStatus("generating");
          setGenerationNote(
            `${selectedNarrator?.name || "Ascend"} is preparing this lesson for the first time.`
          );
          metadata = await api.prepareElevenLabsLessonAudio(lesson.id, narratorId);
        }
        if (cancelled) return;
        setGenerationNote(
          metadata?.cached === false
            ? `Generated once with ${metadata.narrator_name || selectedNarrator?.name}. Future plays use the cached audio.`
            : ""
        );
        setAudioUrl(api.getElevenLabsLessonAudioUrl(lesson.id, narratorId));
        setStatus("ready");
      } catch (err) {
        if (!cancelled) {
          setStatus("error");
          setError(err?.message || "Unable to prepare ElevenLabs narration.");
        }
      }
    };
    prepare();
    return () => {
      cancelled = true;
      audioRef.current?.pause();
    };
  }, [lesson.id, narratorId]);

  useEffect(() => {
    localStorage.setItem(NARRATOR_KEY, narratorId);
  }, [narratorId]);

  useEffect(() => {
    localStorage.setItem(RATE_KEY, String(rate));
    if (audioRef.current) audioRef.current.playbackRate = rate;
  }, [rate]);

  const restorePosition = () => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.playbackRate = rate;
    const stored = Number(localStorage.getItem(`${storageKey}-${narratorId}-seconds`));
    if (Number.isFinite(stored) && stored > 0 && stored < audio.duration - 2) {
      audio.currentTime = stored;
      setCurrentTime(stored);
    }
    setDuration(Number.isFinite(audio.duration) ? audio.duration : 0);
  };

  const saveProgress = (seconds) => {
    localStorage.setItem(`${storageKey}-${narratorId}-seconds`, String(seconds));
    const pct = duration ? clamp((seconds / duration) * 100, 0, 100) : 0;
    onProgress?.({ position: seconds, progress: pct });
  };

  const togglePlayback = async () => {
    const audio = audioRef.current;
    if (!audio || !audioUrl) return;
    setError("");
    try {
      if (!audio.paused) {
        audio.pause();
        setStatus("paused");
      } else {
        if (audio.ended) audio.currentTime = 0;
        audio.playbackRate = rate;
        await audio.play();
        setStatus("playing");
      }
    } catch (err) {
      setError(err?.message || "Unable to start playback.");
    }
  };

  const seekBy = (seconds) => {
    const audio = audioRef.current;
    if (!audio || !duration) return;
    audio.currentTime = clamp(audio.currentTime + seconds, 0, duration);
    setCurrentTime(audio.currentTime);
    saveProgress(audio.currentTime);
  };

  const commitScrub = (value) => {
    const audio = audioRef.current;
    if (!audio) return;
    const next = clamp(Number(value), 0, duration || 0);
    audio.currentTime = next;
    setCurrentTime(next);
    setScrubTime(null);
    saveProgress(next);
  };

  const restart = () => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.currentTime = 0;
    setCurrentTime(0);
    saveProgress(0);
  };

  const stop = () => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.pause();
    setStatus("ready");
  };

  const changeNarrator = (event) => {
    audioRef.current?.pause();
    setCurrentTime(0);
    setDuration(0);
    setNarratorId(event.target.value);
  };

  const busy = status === "loading" || status === "generating";
  const statusLabel =
    status === "playing" ? "Playing" :
    status === "paused" ? "Paused" :
    status === "generating" ? "Preparing" :
    status === "loading" ? "Loading" :
    status === "error" ? "Unavailable" : "Ready";

  return (
    <section className="panel ascend-audio-player elevenlabs-player">
      <div className="panel-heading ascend-audio-heading">
        <div>
          <span className="eyebrow">ASCEND AUDIO</span>
          <h2><Headphones size={22} />{lesson.title}</h2>
        </div>
        <span className={`audio-status audio-status-${status}`}>{statusLabel}</span>
      </div>

      <div className="audio-now-reading elevenlabs-now-playing">
        <Mic2 size={20} />
        <div>
          <span>Narrated by</span>
          <strong>{selectedNarrator?.name} · {selectedNarrator?.description}</strong>
        </div>
        <span className="elevenlabs-rate-pill">{rate}×</span>
      </div>

      {busy ? (
        <div className="elevenlabs-preparing">
          <LoaderCircle className="voice-spin" size={20} />
          <div>
            <strong>{status === "generating" ? "Generating lesson audio…" : "Loading audio…"}</strong>
            <span>{generationNote || "Checking Ascend's audio cache."}</span>
          </div>
        </div>
      ) : (
        <>
          <audio
            ref={audioRef}
            src={audioUrl}
            preload="metadata"
            onLoadedMetadata={restorePosition}
            onTimeUpdate={(event) => {
              const seconds = event.currentTarget.currentTime;
              setCurrentTime(seconds);
              saveProgress(seconds);
            }}
            onPlay={() => setStatus("playing")}
            onPause={() => {
              if (!audioRef.current?.ended && status === "playing") setStatus("paused");
            }}
            onEnded={() => {
              setStatus("ready");
              setCurrentTime(duration);
              saveProgress(duration);
            }}
            onError={() => setError("The generated lesson audio could not be loaded.")}
          />

          <div className="audio-progress-wrap">
            <div className="audio-progress-labels">
              <span>{formatClock(displayTime)} · {Math.round(progress)}%</span>
              <span>-{formatClock(Math.max(0, duration - displayTime))}</span>
            </div>
            <div className="audio-scrubber-wrap">
              <input
                className="audio-progress-scrubber"
                type="range"
                min="0"
                max={duration || 1}
                step="0.1"
                value={displayTime}
                onChange={(e) => setScrubTime(Number(e.target.value))}
                onPointerUp={(e) => commitScrub(e.currentTarget.value)}
                onKeyUp={(e) => {
                  if (["ArrowLeft", "ArrowRight", "Home", "End"].includes(e.key)) {
                    commitScrub(e.currentTarget.value);
                  }
                }}
                onBlur={(e) => scrubTime !== null && commitScrub(e.currentTarget.value)}
                style={{ "--audio-progress": `${progress}%` }}
              />
            </div>
          </div>

          <div className="audio-primary-controls audio-transport-controls">
            <button className="audio-control-button audio-seek-button" onClick={() => seekBy(-SEEK_SECONDS)} disabled={!currentTime}>
              <RotateCcw size={24}/><span>{SEEK_SECONDS}</span>
            </button>
            <button className="audio-play-button" onClick={togglePlayback} disabled={!audioUrl}>
              {status === "playing" ? <Pause size={28}/> : <Play size={28} fill="currentColor"/>}
              <span>{status === "playing" ? "Pause" : currentTime > 0 ? "Continue" : "Listen"}</span>
            </button>
            <button className="audio-control-button audio-seek-button" onClick={() => seekBy(SEEK_SECONDS)} disabled={!duration || currentTime >= duration}>
              <RotateCw size={24}/><span>{SEEK_SECONDS}</span>
            </button>
          </div>

          <div className="audio-secondary-actions">
            <button className="audio-text-action" onClick={stop}><Square size={14} fill="currentColor"/>Stop</button>
            <button className="audio-text-action" onClick={restart}><RotateCcw size={15}/>Start over</button>
          </div>
        </>
      )}

      <details className="elevenlabs-playback-settings">
        <summary>Voice & playback</summary>
        <div className="audio-narrator-panel">
          <div className="audio-narrator-copy">
            <Mic2 size={20}/>
            <div><span>Narrator</span><strong>{selectedNarrator?.name} · {selectedNarrator?.description}</strong></div>
          </div>
          <div className="audio-narrator-controls">
            <label>
              <span className="sr-only">Choose narrator</span>
              <select value={narratorId} onChange={changeNarrator}>
                {narrators.map((n) => (
                  <option key={n.id} value={n.id}>{n.name} — {n.description}</option>
                ))}
              </select>
            </label>
          </div>
        </div>

        <div className="audio-speed-row">
          <span>Playback speed</span>
          <div className="audio-speed-options">
            {SPEED_OPTIONS.map((option) => (
              <button key={option} className={rate === option ? "active" : ""} onClick={() => setRate(option)}>
                {option}×
              </button>
            ))}
          </div>
        </div>
      </details>

      {generationNote && !busy ? <p className="audio-note">{generationNote}</p> : null}
      {error ? <div className="audio-player-message">{error}</div> : null}

      <details className="audio-script-details">
        <summary>View narration script</summary>
        <div className="audio-script">{lesson.audio_script || ""}</div>
      </details>
    </section>
  );
}
