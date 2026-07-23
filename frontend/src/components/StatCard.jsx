export default function StatCard({ icon: Icon, label, value, helper }) {
  return (
    <article className="stat-card">
      <div className="stat-icon"><Icon size={21} /></div>
      <div>
        <span>{label}</span>
        <strong>{value}</strong>
        {helper && <small>{helper}</small>}
      </div>
    </article>
  );
}
