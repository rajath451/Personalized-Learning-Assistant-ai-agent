import unittest
from src.agents.scheduler_agent import SchedulerAgent

class TestSchedulerAgent(unittest.TestCase):

    def setUp(self):
        self.scheduler_agent = SchedulerAgent()

    def test_plan_study_session(self):
        session = self.scheduler_agent.plan_study_session("Math", 2)
        self.assertEqual(session['subject'], "Math")
        self.assertEqual(session['duration'], 2)

    def test_manage_user_schedule(self):
        self.scheduler_agent.manage_user_schedule("user1", "2023-10-01", "Math", 2)
        schedule = self.scheduler_agent.get_user_schedule("user1")
        self.assertIn("2023-10-01", schedule)

    def test_adaptive_feedback(self):
        feedback = self.scheduler_agent.adaptive_feedback("user1", "Math", 80)
        self.assertIn("good job", feedback)

if __name__ == '__main__':
    unittest.main()