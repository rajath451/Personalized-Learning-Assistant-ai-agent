import unittest
from src.core.agent_manager import AgentManager
from src.agents.quiz_agent import QuizAgent
from src.agents.explanation_agent import ExplanationAgent
from src.agents.scheduler_agent import SchedulerAgent

class TestAgentManager(unittest.TestCase):

    def setUp(self):
        self.agent_manager = AgentManager()
        self.quiz_agent = QuizAgent()
        self.explanation_agent = ExplanationAgent()
        self.scheduler_agent = SchedulerAgent()
        self.agent_manager.register_agent(self.quiz_agent)
        self.agent_manager.register_agent(self.explanation_agent)
        self.agent_manager.register_agent(self.scheduler_agent)

    def test_register_agent(self):
        self.assertIn(self.quiz_agent, self.agent_manager.agents)
        self.assertIn(self.explanation_agent, self.agent_manager.agents)
        self.assertIn(self.scheduler_agent, self.agent_manager.agents)

    def test_unregister_agent(self):
        self.agent_manager.unregister_agent(self.quiz_agent)
        self.assertNotIn(self.quiz_agent, self.agent_manager.agents)

    def test_get_agent(self):
        agent = self.agent_manager.get_agent('quiz')
        self.assertEqual(agent, self.quiz_agent)

    def test_get_nonexistent_agent(self):
        agent = self.agent_manager.get_agent('nonexistent')
        self.assertIsNone(agent)

    def test_agent_interaction(self):
        response = self.agent_manager.interact('quiz', {'question': 'What is 2 + 2?'})
        self.assertIn('answer', response)

if __name__ == '__main__':
    unittest.main()