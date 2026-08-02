import {
  ArrowRight,
  HelpCircle,
  Lightbulb,
  MessageCircleQuestion,
} from "lucide-react";

export default function WorkshopQuestions() {
  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">PREPARE THE NEXT CONVERSATION</span>
        <h1>Questions for Travis</h1>
        <p>
          Keep a focused list of questions that turn uncertainty into useful
          workshop conversations.
        </p>
      </header>

      <section className="panel workshop-empty-state">
        <div className="workshop-empty-icon">
          <MessageCircleQuestion size={30} />
        </div>

        <div>
          <span className="eyebrow">QUESTION WORKSPACE READY</span>
          <h2>Questions will be connected to sessions and labs in Phase 2.</h2>
          <p>
            You will be able to carry forward anything unclear, identify
            follow-up topics, and prepare concise questions before each meeting.
          </p>
        </div>
      </section>

      <section className="workshop-question-guide">
        <article className="panel workshop-question-card">
          <HelpCircle size={21} />
          <div>
            <strong>What did not fully click?</strong>
            <p>Capture the exact concept, command, or relationship that is unclear.</p>
          </div>
          <ArrowRight size={18} />
        </article>

        <article className="panel workshop-question-card">
          <Lightbulb size={21} />
          <div>
            <strong>What should you see in the real environment?</strong>
            <p>Ask how the concept appears in your team’s pipelines, AWS setup, and daily work.</p>
          </div>
          <ArrowRight size={18} />
        </article>
      </section>
    </div>
  );
}
