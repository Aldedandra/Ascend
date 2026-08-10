import { Capacitor } from "@capacitor/core";

const NATIVE_API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://100.73.37.48:8000";

const API_BASE_URL = Capacitor.isNativePlatform()
  ? NATIVE_API_BASE_URL
  : "";

const request = async (path, options = {}) => {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });


  if (!response.ok) {
    const error = await response
      .json()
      .catch(() => ({ detail: "Request failed" }));

    throw new Error(error.detail || "Request failed");
  }

  return response.json();
};



const binaryRequest = async (path, options = {}) => {
  const response = await fetch(`${API_BASE_URL}${path}`, options);

  if (!response.ok) {
    const error = await response
      .json()
      .catch(() => ({ detail: "Request failed" }));
    throw new Error(error.detail || "Request failed");
  }

  return {
    blob: await response.blob(),
    characterCost: response.headers.get("X-Ascend-Character-Cost") || "unknown",
    modelId: response.headers.get("X-Ascend-ElevenLabs-Model") || "",
  };
};

export const api = {
  getModules: () => request("/api/modules"),

  getElevenLabsStatus: () =>
    request("/api/audio/elevenlabs/status"),

  getElevenLabsVoices: () =>
    request("/api/audio/elevenlabs/voices"),

  getAscendNarrators: () =>
    request("/api/audio/elevenlabs/narrators"),

  getElevenLabsLessonAudioStatus: (lessonId, narratorId = "bella") =>
    request(`/api/audio/elevenlabs/lessons/${lessonId}/status?narrator_id=${encodeURIComponent(narratorId)}`),

  prepareElevenLabsLessonAudio: (lessonId, narratorId = "bella") =>
    request(`/api/audio/elevenlabs/lessons/${lessonId}/prepare`, {
      method: "POST",
      body: JSON.stringify({ narrator_id: narratorId }),
    }),

  getElevenLabsLessonAudioUrl: (lessonId, narratorId = "bella") =>
    `${API_BASE_URL}/api/audio/elevenlabs/lessons/${lessonId}?narrator_id=${encodeURIComponent(narratorId)}`,

  createElevenLabsPreview: (voiceId, text) =>
    binaryRequest("/api/audio/elevenlabs/preview", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ voice_id: voiceId, text }),
    }),

  getLesson: (lessonId) =>
    request(`/api/lessons/${lessonId}`),

  getProgress: () =>
    request("/api/progress"),

  setLessonComplete: (lessonId, completed) =>
    request(`/api/progress/${lessonId}`, {
      method: "PUT",
      body: JSON.stringify({ completed }),
    }),

  submitQuiz: (lessonId, answers) =>
    request(`/api/quizzes/${lessonId}`, {
      method: "POST",
      body: JSON.stringify({ answers }),
    }),

  getJournal: () =>
    request("/api/journal"),

  createJournal: (entry) =>
    request("/api/journal", {
      method: "POST",
      body: JSON.stringify(entry),
    }),

  deleteJournal: (entryId) =>
    request(`/api/journal/${entryId}`, {
      method: "DELETE",
    }),
};