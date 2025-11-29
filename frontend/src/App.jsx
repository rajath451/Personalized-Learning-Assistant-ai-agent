import React, { useState } from "react";

// Import your components
import Dashboard from "./components/Dashboard";
import QuizView from "./components/QuizView";
import ExplanationView from "./components/ExplanationView";
import SchedulerView from "./components/SchedulerView";

export default function App() {
  const [quizResult, setQuizResult] = useState(null);

  const runQuiz = async () => {
    const response = await fetch("http://127.0.0.1:8000/quiz", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic: "math", user_id: "rajath" }),
    });
    const data = await response.json();
    setQuizResult(data);
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Personalized Learning Assistant</h1>
      </header>

      {/* Dashboard Section */}
      <Dashboard />

      {/* Run Quiz Button */}
      <button onClick={runQuiz} className="btn">
        Run Quiz
      </button>

      {/* Quiz Result Section */}
      <div className="quiz-section">
        <h2>Quiz View Section</h2>

        {quizResult ? (
          <pre className="result-box">{JSON.stringify(quizResult, null, 2)}</pre>
        ) : (
          <p>No quiz yet</p>
        )}
      </div>

      {/* Other Features */}
      <QuizView />
      <ExplanationView />
      <SchedulerView />
    </div>
  );
}
