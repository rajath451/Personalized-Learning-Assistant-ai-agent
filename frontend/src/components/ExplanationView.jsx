// ExplanationView.jsx
import React, { useState } from "react";

const ExplanationView = () => {
  const [concept, setConcept] = useState("");
  const [explanation, setExplanation] = useState(null);
  const [loading, setLoading] = useState(false);

  async function fetchExplanation() {
    if (!concept.trim()) {
      setExplanation("⚠️ Please enter a concept first.");
      return;
    }
    setExplanation(null);
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/explain", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: "alice", concept }),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.detail || "Failed to fetch explanation");
      }
      setExplanation(data.explanation || JSON.stringify(data));
    } catch (err) {
      setExplanation("❌ Error: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="explanation-view">
      <h2>💡 Explanation Agent</h2>
      <input
        type="text"
        placeholder="Enter concept"
        value={concept}
        onChange={(e) => setConcept(e.target.value)}
      />
      <button onClick={fetchExplanation} disabled={loading}>
        {loading ? "Generating…" : "Get Explanation"}
      </button>

      {explanation && <pre className="output">{explanation}</pre>}
    </section>
  );
};

export default ExplanationView;