import unittest
from src.agents.quiz_agent import QuizAgent

class TestQuizAgent(unittest.TestCase):

    def setUp(self):
        self.agent = QuizAgent()

    def test_generate_question(self):
        question = self.agent.generate_question()
        self.assertIsInstance(question, dict)
        self.assertIn('question', question)
        self.assertIn('options', question)
        self.assertIn('answer', question)

    def test_evaluate_response_correct(self):
        question = self.agent.generate_question()
        response = question['answer']
        result = self.agent.evaluate_response(question, response)
        self.assertTrue(result)

    def test_evaluate_response_incorrect(self):
        question = self.agent.generate_question()
        incorrect_response = 'wrong_answer'
        result = self.agent.evaluate_response(question, incorrect_response)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()