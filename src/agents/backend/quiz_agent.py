class BaseAgent:
    def __init__(self, name):
        self.name = name

    def generate_questions(self, topic):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def evaluate_response(self, question, user_response):
        raise NotImplementedError("This method should be overridden by subclasses.")


class QuizAgent(BaseAgent):
    def __init__(self):
        super().__init__("QuizAgent")

    def generate_questions(self, topic):
        # Example implementation for generating quiz questions
        return [
            {"question": f"What is {topic}?", "options": ["A", "B", "C", "D"], "answer": "A"},
            {"question": f"Explain {topic} in simple terms.", "options": [], "answer": "It is..."},
        ]

    def evaluate_response(self, question, user_response):
        # Example implementation for evaluating user response
        return user_response == question["answer"]