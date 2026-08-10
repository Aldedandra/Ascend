import { Headphones, LoaderCircle, Pause, Play, Sparkles } from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";
import { api } from "../services/api";
import "../styles/voice-studio.css";

const CANDIDATE_IDS = [
  "hpp4J3VqNfWAUOO0d1Us", // Bella
  "XrExE9yKIg1WjnnlVkGX", // Matilda
  "cjVigY5qzO86Huf0OWal", // Eric
  "nPczCjzI2devNBz1zQrb", // Brian
  "SAz9YHcvj6GT2YYXdXww", // River
];

function buildSample(script = "") {
  const cleaned = script.replace(/\s+/g, " ").trim();
  if (!cleaned) return "";
  const target = cleaned.slice(0, 470);
  const lastSentence = Math.max(
    target.lastIndexOf(". "),
    target.lastIndexOf("? "),
    target.lastIndexOf("! ")
  );
  return (lastSentence > 220 ? target.slice(0, lastSentence + 1) : target).trim();
}

export default function VoiceStudio() {
  const [voices, setVoices] = useState([]);
  const [sample, setSample] = useState("");
  const [loading, setLoading] = useState(true);
  const [generatingId, setGeneratingId] = useState("");
  const [playingId, setPlayingId] = useState("");
  const [error, setError] = useState("");
  const [costs, setCosts] = useState({});
  const [clips, setClips] = useState({});
  const audioRef = useRef(null);
  const urlsRef = useRef({});

  useEffect(() => {
    let cancelled = false;
    Promise.all([api.getElevenLabsVoices(), api.getLesson("0-1")])
      .then(([voiceData, lesson]) => {
        if (cancelled) return;
        setVoices(
          CANDIDATE_IDS
            .map((id) => voiceData.voices.find((voice) => voice.voice_id === id))
            .filter(Boolean)
        );
        setSample(buildSample(lesson.audio_script));
      })
      .catch((err) => !cancelled && setError(err.message))
      .finally(() => !cancelled && setLoading(false));

    return () => {
      cancelled = true;
      audioRef.current?.pause();
      Object.values(urlsRef.current).forEach((url) => URL.revokeObjectURL(url));
    };
  }, []);

  const sampleCharacters = sample.length;
  const readyCount = useMemo(() => Object.keys(clips).length, [clips]);

  const stopAudio = () => {
    audioRef.current?.pause();
    audioRef.current = null;
    setPlayingId("");
  };

  const playClip = (voiceId) => {
    if (playingId === voiceId) {
      stopAudio();
      return;
    }
    stopAudio();
    const url = clips[voiceId];
    if (!url) return;
    const audio = new Audio(url);
    audioRef.current = audio;
    setPlayingId(voiceId);
    audio.onended = () => setPlayingId("");
    audio.onerror = () => {
      setPlayingId("");
      setError("The generated preview could not be played.");
    };
    audio.play().catch((err) => {
      setPlayingId("");
      setError(err.message || "Unable to start preview.");
    });
  };

  const generate = async (voice) => {
    if (!sample || generatingId) return;
    setError("");
    setGeneratingId(voice.voice_id);
    stopAudio();

    try {
      const result = await api.createElevenLabsPreview(voice.voice_id, sample);
      if (urlsRef.current[voice.voice_id]) {
        URL.revokeObjectURL(urlsRef.current[voice.voice_id]);
      }
      const url = URL.createObjectURL(result.blob);
      urlsRef.current[voice.voice_id] = url;
      setClips((current) => ({ ...current, [voice.voice_id]: url }));
      setCosts((current) => ({
        ...current,
        [voice.voice_id]: result.characterCost,
      }));
      setTimeout(() => playGenerated(voice.voice_id, url), 0);
    } catch (err) {
      setError(err.message || "Unable to generate preview.");
    } finally {
      setGeneratingId("");
    }
  };

  const playGenerated = (voiceId, url) => {
    stopAudio();
    const audio = new Audio(url);
    audioRef.current = audio;
    setPlayingId(voiceId);
    audio.onended = () => setPlayingId("");
    audio.onerror = () => setPlayingId("");
    audio.play().catch(() => setPlayingId(""));
  };

  return (
    <section className="voice-studio-page">
      <header className="voice-studio-hero">
        <div>
          <span className="eyebrow">ASCEND VOICE STUDIO</span>
          <h1>Find Ascend's voice.</h1>
          <p>
            Hear the same real lesson excerpt through five promising ElevenLabs
            narrators. Generate only the voices you want to audition.
          </p>
        </div>
        <div className="voice-studio-badge">
          <Sparkles size={18} />
          <span>{readyCount}/5 previews ready</span>
        </div>
      </header>

      <div className="voice-sample panel">
        <div className="voice-sample-heading">
          <div>
            <span className="eyebrow">TEST SCRIPT</span>
            <strong>Module 0 · How Engineers Think</strong>
          </div>
          <span>{sampleCharacters} characters</span>
        </div>
        <p>{sample || "Loading lesson excerpt…"}</p>
        <small>
          Each Generate button creates a fresh ElevenLabs sample and consumes
          credits. Replaying a generated sample does not regenerate it.
        </small>
      </div>

      {error ? <div className="voice-studio-error">{error}</div> : null}

      {loading ? (
        <div className="voice-studio-loading panel">
          <LoaderCircle className="voice-spin" size={22} />
          Loading available narrators…
        </div>
      ) : (
        <div className="voice-candidate-grid">
          {voices.map((voice) => {
            const isGenerating = generatingId === voice.voice_id;
            const isPlaying = playingId === voice.voice_id;
            const hasClip = Boolean(clips[voice.voice_id]);
            const labels = voice.labels || {};

            return (
              <article className="voice-candidate panel" key={voice.voice_id}>
                <div className="voice-candidate-top">
                  <div className="voice-avatar"><Headphones size={22} /></div>
                  <div>
                    <h2>{voice.name.split(" - ")[0]}</h2>
                    <p>{voice.name.split(" - ").slice(1).join(" - ")}</p>
                  </div>
                </div>

                <p className="voice-description">{voice.description}</p>

                <div className="voice-tags">
                  {labels.accent ? <span>{labels.accent}</span> : null}
                  {labels.descriptive ? <span>{labels.descriptive}</span> : null}
                  {labels.gender ? <span>{labels.gender}</span> : null}
                </div>

                <button
                  className={`voice-preview-button ${hasClip ? "ready" : ""}`}
                  onClick={() => hasClip ? playClip(voice.voice_id) : generate(voice)}
                  disabled={Boolean(generatingId) && !isGenerating}
                >
                  {isGenerating ? (
                    <><LoaderCircle className="voice-spin" size={18} /> Generating…</>
                  ) : isPlaying ? (
                    <><Pause size={18} /> Pause preview</>
                  ) : hasClip ? (
                    <><Play size={18} /> Play again</>
                  ) : (
                    <><Play size={18} /> Generate preview</>
                  )}
                </button>

                {costs[voice.voice_id] ? (
                  <small className="voice-cost">
                    ElevenLabs reported cost: {costs[voice.voice_id]} credits
                  </small>
                ) : null}
              </article>
            );
          })}
        </div>
      )}
    </section>
  );
}
