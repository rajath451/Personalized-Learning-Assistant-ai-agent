// QuizView.jsx
import React, { useState, useEffect } from "react";

const QuizView = () => {
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchQuizQuestions = async () => {
      setLoading(true);
      try {
        const response = await fetch("http://127.0.0.1:8000/quiz", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ user_id: "alice", topic: "machine learning" }),
        });

        const data = await response.json();

        // Expecting backend to return { quiz: [...] } or similar
        if (data.quiz) {
          setQuizQuestions(data.quiz);
        } else {
          // fallback if backend returns plain text
          setQuizQuestions([
            {
              question: "Sample question (backend not implemented fully)",
              options: ["Option A", "Option B", "Option C"],
            },
          ]);
        }
      } catch (err) {
        console.error("Error fetching quiz:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchQuizQuestions();
  }, []);

  const handleAnswer = (answer) => {
    setUserAnswers([...userAnswers, answer]);
    if (currentQuestionIndex < quizQuestions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setIsSubmitted(true);
    }
  };

  const renderQuestion = () => {
    if (quizQuestions.length === 0) {
      return <p>No quiz questions available.</p>;
    }

    if (currentQuestionIndex < quizQuestions.length) {
      const question = quizQuestions[currentQuestionIndex];
      return (
        <div>
          <h2>{question.question}</h2>
          {question.options?.map((option, index) => (
            <button key={index} onClick={() => handleAnswer(option)}>
              {option}
            </button>
          ))}
        </div>
      );
    } else {
      return <h2>Quiz Completed!</h2>;
    }
  };

  return (
    <section className="quiz-view">
      <h2>🧠 Quiz Agent</h2>
      {loading ? (
        <p>Loading quiz…</p>
      ) : isSubmitted ? (
        <div>
          <h3>Your Answers:</h3>
          <ul>
            {userAnswers.map((answer, index) => (
              <li key={index}>{answer}</li>
            ))}
          </ul>
        </div>
      ) : (
        renderQuestion()
      )}
    </section>
  );
};

export default QuizView;