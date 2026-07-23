export default function ProgressBar({ value = 0 }) {
  return (
    <div className="progress-track" aria-label={`${value}% complete`}>
      <div className="progress-fill" style={{ width: `${Math.max(0, Math.min(value, 100))}%` }} />
    </div>
  );
}
