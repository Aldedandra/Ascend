import {
  CheckCircle2,
  Clipboard,
  FlaskConical,
  Headphones,
  MessageSquareText,
  Trophy,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { api } from "../services/api";

const tabs = [
  { id: "lesson", label: "Lesson" },
  { id: "audio", label: "Audio" },
  { id: "lab", label: "Lab" },
  { id: "quiz", label: "Quiz" },
  { id: "reflection", label: "Reflection" },
];

export default function Lesson() {
  const { lessonId } = useParams();
  const navigate = useNavigate();
  const [lesson, setLesson] = useState(null);
  const [activeTab, setActiveTab] = useState("lesson");
  const [answers, setAnswers] = useState([]);
  const [quizResult, setQuizResult] = useState(null);
  const [copied, setCopied] = useState(false);
  const [error, setError] = useState("");

  const loadLesson = () => {
    api.getLesson(lessonId)
      .then((data) => {
        setLesson(data);
        setAnswers(new Array(data.quiz.length).fill(-1));
      })
      .catch((err) => setError(err.message));
  };

  useEffect(loadLesson, [lessonId]);

  const coachPrompt = useMemo(() => {
    if (!lesson) return "";
    return `I am working through The Journey, lesson ${lesson.id}: ${lesson.title}. Please continue coaching me from this lesson. Ask me questions, review my reasoning, and do not skip the lab, quiz, reflection, or portfolio update.`;
  }, [lesson]);

  const copyPrompt = async () => {
    await navigator.clipboard.writeText(coachPrompt);
    setCopied(true);
    setTimeout(() => setCopied(false), 1600);
  };

  const toggleComplete = async () => {
    await api.setLessonComplete(lesson.id, !lesson.completed);
    loadLesson();
  };

  const submitQuiz = async () => {
    if (answers.some((answer) => answer === -1)) {
      setError("Please answer every question before submitting the quiz.");
      return;
    }

    try {
      setError("");
      setQuizResult(null);

      const result = await api.submitQuiz(lesson.id, answers);
      setQuizResult(result);
    } catch (err) {
      setError(err.message);
    }
  };

if (error && !lesson) {
  return <div className="error-card">{error}</div>;
}
  if (!lesson) return <div className="loading-card">Loading lesson...</div>;

  return (
    <div className="page-stack">
      <button className="text-button" onClick={() => navigate("/modules")}>← Back to modules</button>

      <header className="lesson-hero">
        <div>
          <span className="eyebrow">LESSON {lesson.id}</span>
          <h1>{lesson.title}</h1>
          <p>{lesson.summary}</p>
          <div className="lesson-meta">
            <span>{lesson.duration_minutes} min</span>
            <span>+{lesson.xp} XP</span>
            <span>{lesson.completed ? "Completed" : "In progress"}</span>
          </div>
        </div>
        <button className={`complete-button ${lesson.completed ? "completed" : ""}`} onClick={toggleComplete}>
          <CheckCircle2 size={19} />
          {lesson.completed ? "Completed" : "Mark complete"}
        </button>
      </header>

      <div className="tab-row">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            className={activeTab === tab.id ? "active" : ""}
            onClick={() => {
  setActiveTab(tab.id);
  setError("");
}}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {error && (
  <div className="error-card">
    {error}
  </div>
)}

      {activeTab === "lesson" && (
        <section className="panel lesson-content">
          {lesson.content.map((section) => (
            <article key={section.heading}>
              <h2>{section.heading}</h2>
              <p>{section.body}</p>
            </article>
          ))}
        </section>
      )}

      {activeTab === "audio" && (
        <section className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">THE JOURNEY PODCAST</span>
              <h2><Headphones size={22} /> {lesson.title}</h2>
            </div>
          </div>
          <p className="audio-note">
            Use ChatGPT Read Aloud, your browser&apos;s text-to-speech, or copy this script into your preferred reader.
          </p>
          <div className="audio-script">{lesson.audio_script}</div>
        </section>
      )}

      {activeTab === "lab" && (
        <section className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">HANDS-ON LAB</span>
              <h2><FlaskConical size={22} /> {lesson.lab.title}</h2>
            </div>
          </div>
          <ol className="lab-steps">
            {lesson.lab.instructions.map((step) => <li key={step}>{step}</li>)}
          </ol>
        </section>
      )}

      {activeTab === "quiz" && (
        <section className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">KNOWLEDGE CHECK</span>
              <h2><Trophy size={22} /> Lesson quiz</h2>
            </div>
          </div>
          <div className="quiz-list">
            {lesson.quiz.map((item, questionIndex) => (
              <fieldset key={item.question}>
                <legend>{questionIndex + 1}. {item.question}</legend>
                {item.choices.map((choice, choiceIndex) => (
                  <label key={choice} className="choice-row">
                    <input
                      type="radio"
                      name={`question-${questionIndex}`}
                      checked={answers[questionIndex] === choiceIndex}
                      onChange={() => {
                        const next = [...answers];
                        next[questionIndex] = choiceIndex;
                        setAnswers(next);
                      }}
                    />
                    <span>{choice}</span>
                  </label>
                ))}
              </fieldset>
            ))}
          </div>

          <button
            className="primary-button"
            onClick={submitQuiz}
            disabled={answers.some((answer) => answer === -1)}>
            Submit quiz
          </button>

{quizResult && (
  <div className="result-banner">
    <strong>
      Score: {quizResult.score}/{quizResult.total}
    </strong>

    <div>
      {quizResult.score === quizResult.total
        ? "Excellent work. You answered every question correctly."
        : "Review the lesson and try the quiz again when you are ready."}
    </div>
  </div>
)}
        </section>
      )}

      {activeTab === "reflection" && (
        <section className="content-grid two-column">
          <article className="panel">
            <span className="eyebrow">REFLECTION</span>
            <h2><MessageSquareText size={22} /> Look back before moving forward</h2>
            <p className="reflection-question">{lesson.reflection}</p>
            <p>Write your answer in the Journal so it becomes part of your long-term record.</p>
            <button className="secondary-button" onClick={() => navigate("/journal")}>Open journal</button>
          </article>

          <article className="panel">
            <span className="eyebrow">CONTINUE WITH ALEX</span>
            <h2>Bring this lesson back to ChatGPT</h2>
            <p>Copy the context prompt below and paste it into this conversation.</p>
            <div className="prompt-box">{coachPrompt}</div>
            <button className="secondary-button" onClick={copyPrompt}>
              <Clipboard size={18} /> {copied ? "Copied" : "Copy coaching prompt"}
            </button>
          </article>
        </section>
      )}
    </div>
  );
}
