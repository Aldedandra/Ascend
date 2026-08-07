import {
  CheckCircle2,
  Clipboard,
  FlaskConical,
  MessageSquareText,
  Trophy,
  Download,
  Lightbulb,
  ListChecks,
  Network,
  ArrowDown,
} from "lucide-react";
import {
  useEffect,
  useMemo,
  useState,
} from "react";
import {
  useNavigate,
  useParams,
} from "react-router-dom";

import {
  api,
} from "../services/api";
import AscendAudioPlayer from "../components/AscendAudioPlayer";
import useLearningSession from "../hooks/useLearningSession";


function LessonDiagram({ diagram }) {
  if (!diagram?.nodes?.length) {
    return null;
  }

  return (
    <section className="lesson-learning-block lesson-diagram-block">
      <div className="lesson-learning-block-heading">
        <span className="lesson-learning-block-icon">
          <Network size={20} />
        </span>
        <div>
          <span className="eyebrow">SYSTEM MAP</span>
          <h2>{diagram.title}</h2>
        </div>
      </div>

      {diagram.description && (
        <p>{diagram.description}</p>
      )}

      <div className="lesson-flow-diagram" role="list" aria-label={diagram.title}>
        {diagram.nodes.map((node, index) => (
          <div className="lesson-flow-step" key={`${node.label}-${index}`} role="listitem">
            <div className="lesson-flow-node">
              <strong>{node.label}</strong>
              {node.detail && <span>{node.detail}</span>}
            </div>

            {index < diagram.nodes.length - 1 && (
              <ArrowDown className="lesson-flow-arrow" size={20} aria-hidden="true" />
            )}
          </div>
        ))}
      </div>

      {diagram.caption && (
        <p className="lesson-learning-caption">{diagram.caption}</p>
      )}
    </section>
  );
}

function EngineerPerspective({ perspective }) {
  if (!perspective) {
    return null;
  }

  return (
    <aside className="lesson-learning-block engineer-perspective">
      <div className="lesson-learning-block-heading">
        <span className="lesson-learning-block-icon">
          <Lightbulb size={20} />
        </span>
        <div>
          <span className="eyebrow">ENGINEER'S PERSPECTIVE</span>
          <h2>{perspective.title}</h2>
        </div>
      </div>
      <p>{perspective.body}</p>
    </aside>
  );
}

function TryItYourself({ exercise }) {
  if (!exercise?.steps?.length) {
    return null;
  }

  return (
    <section className="lesson-learning-block try-it-yourself">
      <div className="lesson-learning-block-heading">
        <span className="lesson-learning-block-icon">
          <ListChecks size={20} />
        </span>
        <div>
          <span className="eyebrow">TRY IT YOURSELF</span>
          <h2>{exercise.title}</h2>
        </div>
      </div>

      {exercise.intro && <p>{exercise.intro}</p>}

      <ol className="lesson-mini-exercise">
        {exercise.steps.map((step, index) => (
          <li key={`${index}-${step}`}>{step}</li>
        ))}
      </ol>

      {exercise.takeaway && (
        <p className="lesson-learning-caption">
          <strong>What to notice:</strong> {exercise.takeaway}
        </p>
      )}
    </section>
  );
}

const tabs = [
  {
    id: "lesson",
    label: "Lesson",
  },
  {
    id: "audio",
    label: "Audio",
  },
  {
    id: "lab",
    label: "Lab",
  },
  {
    id: "quiz",
    label: "Quiz",
  },
  {
    id: "reflection",
    label: "Reflection",
  },
];

export default function Lesson() {
  const {
    lessonId,
  } = useParams();

  const navigate = useNavigate();
  const {
    session: learningSession,
    setActiveTab: saveActiveTab,
    updateAudioProgress,
  } = useLearningSession(lessonId);

  const [
    lesson,
    setLesson,
  ] = useState(null);

  const activeTab = learningSession.activeTab || "lesson";

  const [
    answers,
    setAnswers,
  ] = useState([]);

  const [
    quizResult,
    setQuizResult,
  ] = useState(null);

  const [
    copied,
    setCopied,
  ] = useState(false);

  const [
    error,
    setError,
  ] = useState("");

  const [
    justCompleted,
    setJustCompleted,
  ] = useState(false);

  const [
    nextLesson,
    setNextLesson,
  ] = useState(null);

  useEffect(() => {
    let cancelled = false;

    setLesson(null);
    setAnswers([]);
    setQuizResult(null);
    setCopied(false);
    setError("");
    setJustCompleted(false);
    setNextLesson(null);

    api
      .getLesson(lessonId)
      .then((data) => {
        if (cancelled) {
          return;
        }

        setLesson(data);
        setAnswers(
          new Array(data.quiz?.length || 0)
            .fill(-1)
        );
      })
      .catch((err) => {
        if (!cancelled) {
          setError(err.message);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [lessonId]);

  const coachPrompt = useMemo(() => {
    if (!lesson) {
      return "";
    }

    return (
      `I am working through Ascend, lesson ${lesson.id}: ` +
      `${lesson.title}. Please continue coaching me from this lesson. ` +
      "Ask me questions, review my reasoning, and do not skip the lab, " +
      "quiz, reflection, or portfolio update."
    );
  }, [lesson]);

  const findNextLesson = async (
    currentLessonId
  ) => {
    const modules =
      await api.getModules();

    const lessons = modules.flatMap(
      (module) =>
        module.lessons || []
    );

    const currentIndex =
      lessons.findIndex(
        (item) =>
          item.id === currentLessonId
      );

    if (
      currentIndex >= 0 &&
      currentIndex < lessons.length - 1
    ) {
      return lessons[currentIndex + 1];
    }

    return null;
  };

  const copyPrompt = async () => {
    try {
      await navigator.clipboard.writeText(
        coachPrompt
      );

      setCopied(true);

      window.setTimeout(() => {
        setCopied(false);
      }, 1600);
    } catch {
      setError(
        "Unable to copy the coaching prompt."
      );
    }
  };

  const toggleComplete = async () => {
    if (!lesson) {
      return;
    }

    try {
      setError("");

      const completing =
        !lesson.completed;

      await api.setLessonComplete(
        lesson.id,
        completing
      );

      setLesson((currentLesson) => ({
        ...currentLesson,
        completed: completing,
      }));

      if (completing) {
        const followingLesson =
          await findNextLesson(
            lesson.id
          );

        setNextLesson(
          followingLesson
        );

        setJustCompleted(true);
      } else {
        setJustCompleted(false);
        setNextLesson(null);
      }
    } catch (err) {
      setError(err.message);
    }
  };

  const submitQuiz = async () => {
    const unanswered =
      answers.some(
        (answer) => answer === -1
      );

    if (unanswered) {
      setError(
        "Please answer every question before submitting the quiz."
      );

      return;
    }

    try {
      setError("");
      setQuizResult(null);

      const result =
        await api.submitQuiz(
          lesson.id,
          answers
        );

      setQuizResult(result);
    } catch (err) {
      setError(err.message);
    }
  };

  const downloadNotes = () => {
    const sections = lesson.content
      .map((section) => `${section.heading}\n${section.body}`)
      .join("\n\n");
    const notes = `ASCEND — LESSON ${lesson.id}\n${lesson.title}\n\n${lesson.summary}\n\n${sections}\n\nLAB\n${lesson.lab.instructions.map((step, index) => `${index + 1}. ${step}`).join("\n")}\n\nREFLECTION\n${lesson.reflection}`;
    const blob = new Blob([notes], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `ascend-lesson-${lesson.id}-notes.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const goToNextLesson = () => {
    if (!nextLesson) {
      return;
    }

    navigate(
      `/lessons/${nextLesson.id}`
    );
  };

  if (error && !lesson) {
    return (
      <div className="error-card">
        {error}
      </div>
    );
  }

  if (!lesson) {
    return (
      <div className="loading-card">
        Loading lesson...
      </div>
    );
  }

  const quizIsIncomplete =
    answers.some(
      (answer) => answer === -1
    );

  return (
    <div className="page-stack">
      <button
        className="text-button"
        onClick={() =>
          navigate("/modules")
        }
      >
        ← Back to modules
      </button>

      <header className="lesson-hero">
        <div>
          <span className="eyebrow">
            LESSON {lesson.id}
          </span>

          <h1>{lesson.title}</h1>

          <p>{lesson.summary}</p>

          <div className="lesson-meta">
            <span>
              {lesson.duration_minutes} min
            </span>

            <span>
              +{lesson.xp} XP
            </span>

            {!lesson.completed && (
              <span>In progress</span>
            )}
          </div>
        </div>

        <button
          className={
            `complete-button ${
              lesson.completed
                ? "completed"
                : ""
            }`
          }
          onClick={toggleComplete}
        >
          <CheckCircle2 size={19} />

          {lesson.completed
            ? "Completed"
            : "Mark complete"}
        </button>
      </header>

      {justCompleted && (
        <section className="panel completion-banner">
          <span className="eyebrow">
            LESSON COMPLETE
          </span>

          <h2>
            <CheckCircle2 size={22} />
            Great work.
          </h2>

          <p>
            +{lesson.xp} XP earned.
            Great work building your
            foundation.
          </p>

          {nextLesson && (
            <button
              className="primary-button"
              onClick={goToNextLesson}
            >
              Continue to{" "}
              {nextLesson.title}
            </button>
          )}
        </section>
      )}

      <div className="tab-row">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            className={
              activeTab === tab.id
                ? "active"
                : ""
            }
            onClick={() => {
              saveActiveTab(tab.id);
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
          <div className="lesson-content-toolbar">
            <div>
              <span className="eyebrow">LESSON NOTES</span>
              <p>Read the full lesson or save a clean text copy for offline review.</p>
            </div>
            <button className="secondary-button" onClick={downloadNotes}>
              <Download size={18} /> Download notes
            </button>
          </div>
          {lesson.content.map(
            (section) => (
              <article
                key={section.heading}
              >
                <h2>
                  {section.heading}
                </h2>

                <p>
                  {section.body}
                </p>
              </article>
            )
          )}

          <div className="lesson-learning-extras">
            <LessonDiagram diagram={lesson.diagram} />
            <EngineerPerspective perspective={lesson.engineer_perspective} />
            <TryItYourself exercise={lesson.try_it_yourself} />
          </div>
        </section>
      )}

      {activeTab === "audio" && (
        <AscendAudioPlayer
          lesson={lesson}
          onProgress={updateAudioProgress}
        />
      )}

      {activeTab === "lab" && (
        <section className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">
                HANDS-ON LAB
              </span>

              <h2>
                <FlaskConical size={22} />
                {lesson.lab.title}
              </h2>
            </div>
          </div>

          <ol className="lab-steps">
            {lesson.lab.instructions.map(
              (step) => (
                <li key={step}>
                  {step}
                </li>
              )
            )}
          </ol>
        </section>
      )}

      {activeTab === "quiz" && (
        <section className="panel">
          <div className="panel-heading">
            <div>
              <span className="eyebrow">
                KNOWLEDGE CHECK
              </span>

              <h2>
                <Trophy size={22} />
                Lesson quiz
              </h2>
            </div>
          </div>

          <div className="quiz-list">
            {lesson.quiz.map(
              (
                item,
                questionIndex
              ) => (
                <fieldset
                  key={item.question}
                >
                  <legend>
                    {questionIndex + 1}.{" "}
                    {item.question}
                  </legend>

                  {item.choices.map(
                    (
                      choice,
                      choiceIndex
                    ) => (
                      <label
                        key={choice}
                        className="choice-row"
                      >
                        <input
                          type="radio"
                          name={
                            `question-${questionIndex}`
                          }
                          checked={
                            answers[
                              questionIndex
                            ] ===
                            choiceIndex
                          }
                          onChange={() => {
                            setAnswers(
                              (
                                currentAnswers
                              ) => {
                                const next = [
                                  ...currentAnswers,
                                ];

                                next[
                                  questionIndex
                                ] =
                                  choiceIndex;

                                return next;
                              }
                            );
                          }}
                        />

                        <span>
                          {choice}
                        </span>
                      </label>
                    )
                  )}
                </fieldset>
              )
            )}
          </div>

          <button
            className="primary-button"
            onClick={submitQuiz}
            disabled={
              quizIsIncomplete
            }
          >
            Submit quiz
          </button>

          {quizResult && (
            <div className="result-banner">
              <strong>
                Score:{" "}
                {quizResult.score}/
                {quizResult.total}
              </strong>

              <div>
                {quizResult.score ===
                quizResult.total
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
            <span className="eyebrow">
              REFLECTION
            </span>

            <h2>
              <MessageSquareText
                size={22}
              />
              Look back before moving
              forward
            </h2>

            <p className="reflection-question">
              {lesson.reflection}
            </p>

            <p>
              Write your answer in the
              Journal so it becomes
              part of your long-term
              record.
            </p>

            <button
              className="secondary-button"
              onClick={() =>
                navigate("/journal")
              }
            >
              Open journal
            </button>
          </article>

          <article className="panel">
            <span className="eyebrow">
              CONTINUE WITH ALEX
            </span>

            <h2>
              Bring this lesson back
              to ChatGPT
            </h2>

            <p>
              Copy the context prompt
              below and paste it into
              this conversation.
            </p>

            <div className="prompt-box">
              {coachPrompt}
            </div>

            <button
              className="secondary-button"
              onClick={copyPrompt}
            >
              <Clipboard size={18} />

              {copied
                ? "Copied"
                : "Copy coaching prompt"}
            </button>
          </article>
        </section>
      )}
    </div>
  );
}