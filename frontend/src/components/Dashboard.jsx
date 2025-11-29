// Dashboard.jsx
import React, { useState, useEffect } from "react";
import ProgressBar from "./ProgressBar"; // adjust path if needed

const Dashboard = () => {
  const [progress, setProgress] = useState(0);

  // Example: simulate progress increasing
  useEffect(() => {
    const interval = setInterval(() => {
      setProgress((prev) => (prev < 100 ? prev + 10 : prev));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard">
      <h1>Personalized Learning Dashboard</h1>
      <p>
        Welcome to your personalized learning assistant! Here you can track your
        progress, access quizzes, view explanations, and manage your study
        schedule.
      </p>

      <div className="progress-overview">
        <h2>Your Learning Progress</h2>
        <ProgressBar progress={progress} />
        <p>{progress}% completed</p>
      </div>

      <div className="quick-access">
        <h2>Quick Access</h2>
        <ul>
          <li><a href="/quizzes">Take a Quiz</a></li>
          <li><a href="/explanations">View Explanations</a></li>
          <li><a href="/schedule">Manage Schedule</a></li>
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;