import { Capacitor, registerPlugin } from "@capacitor/core";

const NativeSpeech = registerPlugin("AscendSpeech");
const WEB_CHUNK_SIZE = 1800;

function createListenerStore() {
  const listeners = new Map();

  return {
    add(eventName, listener) {
      const eventListeners = listeners.get(eventName) || new Set();
      eventListeners.add(listener);
      listeners.set(eventName, eventListeners);

      return {
        remove() {
          eventListeners.delete(listener);
        },
      };
    },
    emit(eventName, payload) {
      listeners.get(eventName)?.forEach((listener) => listener(payload));
    },
  };
}

function splitIntoSpeechChunks(text, maxLength = WEB_CHUNK_SIZE) {
  const chunks = [];
  let start = 0;

  while (start < text.length) {
    let end = Math.min(start + maxLength, text.length);

    if (end < text.length) {
      const searchStart = Math.max(start, end - 500);
      const candidate = text.slice(searchStart, end);
      const paragraphBreak = candidate.lastIndexOf("\n\n");
      const sentenceBreak = Math.max(
        candidate.lastIndexOf(". "),
        candidate.lastIndexOf("? "),
        candidate.lastIndexOf("! ")
      );
      const wordBreak = candidate.lastIndexOf(" ");
      const relativeBreak = paragraphBreak >= 0
        ? paragraphBreak + 2
        : sentenceBreak >= 0
          ? sentenceBreak + 2
          : wordBreak >= 0
            ? wordBreak + 1
            : -1;

      if (relativeBreak > 0) {
        end = searchStart + relativeBreak;
      }
    }

    const chunkText = text.slice(start, end);
    chunks.push({ text: chunkText, start });
    start = end;
  }

  return chunks;
}

function webVoices() {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) {
    return [];
  }

  return window.speechSynthesis.getVoices()
    .filter((voice) => voice.lang?.toLowerCase().startsWith("en"))
    .map((voice) => ({
      identifier: voice.voiceURI || voice.name,
      name: voice.name,
      language: voice.lang,
      quality: voice.localService ? "Installed" : "Online",
      qualityRank: voice.localService ? 2 : 1,
    }))
    .sort((left, right) =>
      right.qualityRank - left.qualityRank
      || left.language.localeCompare(right.language)
      || left.name.localeCompare(right.name)
    );
}

function chooseWebVoice(identifier) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) {
    return null;
  }

  const voices = window.speechSynthesis.getVoices();
  const requested = voices.find((voice) =>
    voice.voiceURI === identifier || voice.name === identifier
  );

  if (requested) {
    return requested;
  }

  const englishVoices = voices.filter((voice) =>
    voice.lang?.toLowerCase().startsWith("en-us")
  );
  const preferredNames = [
    "Alex",
    "Ava",
    "Samantha",
    "Evan",
    "Allison",
    "Google US English",
    "Microsoft Aria",
    "Microsoft Guy",
  ];

  for (const preferredName of preferredNames) {
    const match = englishVoices.find((voice) =>
      voice.name.toLowerCase().includes(preferredName.toLowerCase())
    );

    if (match) {
      return match;
    }
  }

  return englishVoices.find((voice) => voice.default)
    || englishVoices[0]
    || voices[0]
    || null;
}

class WebSpeechController {
  constructor() {
    this.events = createListenerStore();
    this.state = "idle";
    this.chunks = [];
    this.chunkIndex = 0;
    this.rate = 1;
    this.voiceIdentifier = "";
    this.cancelled = false;
  }

  available() {
    return typeof window !== "undefined"
      && "speechSynthesis" in window
      && "SpeechSynthesisUtterance" in window;
  }

  setState(state) {
    this.state = state;
    this.events.emit("speechStateChanged", { state });
  }

  async getVoices() {
    if (!this.available()) {
      return { voices: [] };
    }

    let voices = webVoices();
    if (!voices.length) {
      await new Promise((resolve) => {
        const timeout = window.setTimeout(resolve, 500);
        window.speechSynthesis.addEventListener("voiceschanged", () => {
          window.clearTimeout(timeout);
          resolve();
        }, { once: true });
      });
      voices = webVoices();
    }

    return { voices };
  }

  async previewVoice({ text, rate = 1, voiceIdentifier = "" } = {}) {
    if (!this.available()) {
      throw new Error("Speech synthesis is not supported by this browser.");
    }

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(
      text || "Hello! I'm your Ascend narrator. Let's keep climbing."
    );
    utterance.lang = "en-US";
    utterance.rate = Math.max(0.65, Math.min(Number(rate) || 1, 1.65));
    utterance.voice = chooseWebVoice(voiceIdentifier);
    window.speechSynthesis.speak(utterance);
    return { state: "speaking" };
  }

  async speak({ text, rate = 1, voiceIdentifier = "" }) {
    if (!this.available()) {
      throw new Error("Speech synthesis is not supported by this browser.");
    }

    window.speechSynthesis.cancel();
    this.cancelled = false;
    this.rate = rate;
    this.voiceIdentifier = voiceIdentifier;
    this.chunks = splitIntoSpeechChunks(text);
    this.chunkIndex = 0;
    this.setState("speaking");
    this.speakCurrentChunk();

    return { state: "speaking" };
  }

  speakCurrentChunk() {
    if (this.cancelled) {
      return;
    }

    const chunk = this.chunks[this.chunkIndex];

    if (!chunk) {
      const totalLength = this.chunks.reduce(
        (length, item) => Math.max(length, item.start + item.text.length),
        0
      );
      this.events.emit("speechProgress", {
        characterOffset: totalLength,
        characterLength: 0,
      });
      this.setState("completed");
      return;
    }

    const utterance = new SpeechSynthesisUtterance(chunk.text);
    utterance.lang = "en-US";
    utterance.rate = Math.max(0.65, Math.min(Number(this.rate) || 1, 1.65));
    utterance.pitch = 1;
    utterance.volume = 1;
    utterance.voice = chooseWebVoice(this.voiceIdentifier);

    utterance.onstart = () => this.setState("speaking");
    utterance.onboundary = (event) => {
      this.events.emit("speechProgress", {
        characterOffset: chunk.start + Number(event.charIndex || 0),
        characterLength: Number(event.charLength || 0),
      });
    };
    utterance.onerror = (event) => {
      if (this.cancelled || event.error === "canceled" || event.error === "interrupted") {
        return;
      }

      this.setState("idle");
      this.events.emit("speechError", {
        message: `Browser narration failed: ${event.error || "unknown error"}.`,
      });
    };
    utterance.onend = () => {
      if (this.cancelled) {
        return;
      }

      this.events.emit("speechProgress", {
        characterOffset: chunk.start + chunk.text.length,
        characterLength: 0,
      });
      this.chunkIndex += 1;
      this.speakCurrentChunk();
    };

    window.speechSynthesis.speak(utterance);
  }

  async pause() {
    if (!this.available()) return { state: "idle" };
    window.speechSynthesis.pause();
    this.setState("paused");
    return { state: "paused" };
  }

  async resume() {
    if (!this.available()) return { state: "idle" };
    window.speechSynthesis.resume();
    this.setState("speaking");
    return { state: "speaking" };
  }

  async stop() {
    if (this.available()) {
      this.cancelled = true;
      window.speechSynthesis.cancel();
    }

    this.setState("idle");
    return { state: "idle" };
  }

  async getState() {
    return { state: this.state };
  }

  async addListener(eventName, listener) {
    return this.events.add(eventName, listener);
  }
}

const webSpeech = new WebSpeechController();

export const isNativeSpeechAvailable = () => Capacitor.getPlatform() === "ios";
export const isSpeechAvailable = () => isNativeSpeechAvailable() || webSpeech.available();
export const getSpeechProviderLabel = () =>
  isNativeSpeechAvailable() ? "Native Apple narration" : "Browser narration";

function speechProvider() {
  return isNativeSpeechAvailable() ? NativeSpeech : webSpeech;
}

export const ascendSpeech = {
  speak(options) {
    return speechProvider().speak(options);
  },
  pause() {
    return speechProvider().pause();
  },
  resume() {
    return speechProvider().resume();
  },
  stop() {
    return speechProvider().stop();
  },
  getState() {
    return speechProvider().getState();
  },
  getVoices() {
    return speechProvider().getVoices();
  },
  previewVoice(options) {
    return speechProvider().previewVoice(options);
  },
  addListener(eventName, listener) {
    return speechProvider().addListener(eventName, listener);
  },
};
