const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "";

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

export const api = {
  getModules: () => request("/api/modules"),

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