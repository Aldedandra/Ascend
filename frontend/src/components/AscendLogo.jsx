export default function AscendLogo({ className = "", compact = false }) {
  return (
    <svg
      className={className}
      viewBox="0 0 160 160"
      role="img"
      aria-label="Ascend logo"
    >
      <defs>
        <linearGradient id="ascendPeak" x1="24" y1="18" x2="136" y2="142" gradientUnits="userSpaceOnUse">
          <stop stopColor="#B9FBFF" />
          <stop offset="0.48" stopColor="#29D3E8" />
          <stop offset="1" stopColor="#0A8FA4" />
        </linearGradient>
        <linearGradient id="ascendShadow" x1="80" y1="32" x2="80" y2="140" gradientUnits="userSpaceOnUse">
          <stop stopColor="#35D4E8" />
          <stop offset="1" stopColor="#0A5E6C" />
        </linearGradient>
      </defs>
      <path d="M80 18 140 112 80 76 20 112 80 18Z" fill="url(#ascendPeak)" />
      <path d="M80 18v58l60 36-34-53L80 18Z" fill="#E6FEFF" fillOpacity="0.23" />
      <path d="M80 84 126 113 80 98 34 113 80 84Z" fill="url(#ascendShadow)" />
      <path d="M80 106 115 129 80 117 45 129 80 106Z" fill="url(#ascendShadow)" opacity="0.88" />
      {!compact && <circle cx="80" cy="80" r="73" fill="none" stroke="#29D3E8" strokeOpacity="0.12" />}
    </svg>
  );
}
