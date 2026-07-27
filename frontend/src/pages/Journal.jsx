import { NotebookPen, Plus, Trash2 } from "lucide-react";
import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function Journal() {
  const [entries, setEntries] = useState([]);
  const [form, setForm] = useState({ title: "", body: "" });
  const [error, setError] = useState("");

const load = async () => {
  try {
    const data = await api.getJournal();
    setEntries(data);
  } catch (err) {
    setError(err.message);
  }
};

useEffect(() => {
  load();
}, []);

  const submit = async (event) => {
    event.preventDefault();
    try {
      await api.createJournal(form);
      setForm({ title: "", body: "" });
      load();
    } catch (err) {
      setError(err.message);
    }
  };

  const remove = async (id) => {
    await api.deleteJournal(id);
    load();
  };

  return (
    <div className="page-stack">
      <header className="page-header">
        <span className="eyebrow">REFLECTION JOURNAL</span>
        <h1>Document the journey</h1>
        <p>Capture what you learned, what challenged you, and what you can do now.</p>
      </header>

      <section className="content-grid two-column journal-layout">
        <form className="panel journal-form" onSubmit={submit}>
          <div className="panel-heading">
            <div>
              <span className="eyebrow">NEW ENTRY</span>
              <h2><NotebookPen size={22} /> Write a reflection</h2>
            </div>
          </div>
          <label>
            Title
            <input
              value={form.title}
              onChange={(event) => setForm({ ...form, title: event.target.value })}
              placeholder="Module 0.1 reflection"
              required
            />
          </label>
          <label>
            Reflection
            <textarea
              value={form.body}
              onChange={(event) => setForm({ ...form, body: event.target.value })}
              placeholder="What can I do now that I could not do before?"
              rows={10}
              required
            />
          </label>
          {error && <div className="error-card">{error}</div>}
          <button className="primary-button" type="submit"><Plus size={18} /> Save entry</button>
        </form>

        <div className="journal-entries">
          {entries.length ? entries.map((entry) => (
            <article className="panel journal-entry" key={entry.id}>
              <div className="panel-heading">
                <div>
                  <h2>{entry.title}</h2>
                  <small>{new Date(entry.created_at).toLocaleString()}</small>
                </div>
                <button className="icon-button danger" onClick={() => remove(entry.id)}>
                  <Trash2 size={18} />
                </button>
              </div>
              <p>{entry.body}</p>
            </article>
          )) : <div className="panel">Your first reflection will appear here.</div>}
        </div>
      </section>
    </div>
  );
}
