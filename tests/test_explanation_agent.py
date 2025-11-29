import unittest
from src.agents.explanation_agent import ExplanationAgent

class TestExplanationAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ExplanationAgent()

    def test_simplify_concept(self):
        input_concept = "Photosynthesis"
        expected_output = "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water."
        self.assertEqual(self.agent.simplify_concept(input_concept), expected_output)

    def test_provide_explanation(self):
        user_query = "Can you explain how photosynthesis works?"
        expected_explanation = "Photosynthesis involves converting light energy into chemical energy in the form of glucose."
        self.assertEqual(self.agent.provide_explanation(user_query), expected_explanation)

    def test_adaptive_feedback(self):
        user_performance = {"correct": 5, "total": 10}
        expected_feedback = "Great job! You got 50% correct. Keep practicing!"
        self.assertEqual(self.agent.adaptive_feedback(user_performance), expected_feedback)

if __name__ == '__main__':
    unittest.main()