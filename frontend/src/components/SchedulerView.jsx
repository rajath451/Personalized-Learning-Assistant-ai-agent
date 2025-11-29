// SchedulerView.jsx
import React, { useState } from "react";

const SchedulerView = () => {
  const [sessionId, setSessionId] = useState(null);
  const [intervalSec, setIntervalSec] = useState(60);
  const [topic, setTopic] = useState("calculus");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  async function start() {
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/start_session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: "alice",
          topic,
          reminder_interval: intervalSec,
        }),
      });
      const data = await res.json();
      setSessionId(data.session_id || "unknown");
      setStatus("Session started successfully");
    } catch (err) {
      setStatus("❌ Error: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  async function pause() {
    if (!sessionId) return;
    try {
      await fetch("http://127.0.0.1:8000/pause_session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId }),
      });
      setStatus("Session paused");
    } catch (err) {
      setStatus("❌ Error: " + err.message);
    }
  }

  async function resume() {
    if (!sessionId) return;
    try {
      await fetch("http://127.0.0.1:8000/resume_session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId }),
      });
      setStatus("Session resumed");
    } catch (err) {
      setStatus("❌ Error: " + err.message);
    }
  }

  return (
    <section className="scheduler-view">
      <h2>⏱️ Scheduler Agent</h2>

      <label>
        Topic:
        <input
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
      </label>

      <label>
        Reminder interval (sec):
        <input
          type="number"
          value={intervalSec}
          onChange={(e) => setIntervalSec(Number(e.target.value))}
        />
      </label>

      <div className="buttons">
        <button onClick={start} disabled={loading || sessionId}>
          {loading ? "Starting…" : "Start Session"}
        </button>
        <button onClick={pause} disabled={!sessionId}>Pause</button>
        <button onClick={resume} disabled={!sessionId}>Resume</button>
      </div>

      {sessionId && <p><strong>Session:</strong> {sessionId}</p>}
      {status && <p>{status}</p>}
    </section>
  );
};

export default SchedulerView;