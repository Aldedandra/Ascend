export default function AscendLogo({ className = "", compact = false }) {
  return (
    <svg
      className={className}
      viewBox="0 0 160 160"
      role="img"
      aria-label="Ascend logo"
    >
      <defs>
        <linearGradient id="ascendOuter" x1="80" y1="18" x2="80" y2="142" gradientUnits="userSpaceOnUse">
          <stop stopColor="#63D1FF" />
          <stop offset="0.44" stopColor="#16A6FF" />
          <stop offset="1" stopColor="#1356C9" />
        </linearGradient>
        <linearGradient id="ascendInner" x1="80" y1="64" x2="80" y2="140" gradientUnits="userSpaceOnUse">
          <stop stopColor="#44C7FF" />
          <stop offset="0.56" stopColor="#148EF4" />
          <stop offset="1" stopColor="#0C4EBA" />
        </linearGradient>
      </defs>

      <path
        d="M80 16 143 137h-23L80 59 40 137H17L80 16Z"
        fill="url(#ascendOuter)"
      />
      <path
        d="M80 72 123 137h-24L80 108 61 137H37L80 72Z"
        fill="url(#ascendInner)"
      />

      {!compact && (
        <circle
          cx="80"
          cy="80"
          r="74"
          fill="none"
          stroke="#2BAEFF"
          strokeOpacity="0.10"
        />
      )}
    </svg>
  );
}
