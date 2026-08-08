import { useEffect, useState } from "react";
import AscendLogo from "./AscendLogo";
import "../styles/launch-transition.css";

const HOLD_MS = 1450;
const FADE_MS = 520;

export default function LaunchTransition() {
  const [phase, setPhase] = useState("enter");
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const fadeTimer = window.setTimeout(() => setPhase("exit"), HOLD_MS);
    const removeTimer = window.setTimeout(
      () => setVisible(false),
      HOLD_MS + FADE_MS
    );

    return () => {
      window.clearTimeout(fadeTimer);
      window.clearTimeout(removeTimer);
    };
  }, []);

  if (!visible) return null;

  return (
    <div
      className={`ascend-launch-transition ascend-launch-transition--${phase}`}
      aria-hidden="true"
    >
      <div className="ascend-launch-atmosphere" />
      <div className="ascend-launch-grid" />

      <div className="ascend-launch-content">
        <div className="ascend-launch-mark-wrap">
          <div className="ascend-launch-halo" />
          <AscendLogo className="ascend-launch-mark" compact />
        </div>

        <div className="ascend-launch-copy">
          <div className="ascend-launch-wordmark">ASCEND</div>
          <div className="ascend-launch-rule" />
          <div className="ascend-launch-tagline">ELEVATE EVERY DAY.</div>
        </div>
      </div>

      <div className="ascend-launch-rise" aria-hidden="true">
        <span />
        <span />
        <span />
      </div>
    </div>
  );
}
