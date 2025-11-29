class AgentManager:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name, agent):
        self.agents[agent_name] = agent

    def get_agent(self, agent_name):
        return self.agents.get(agent_name)

    def execute_agent_action(self, agent_name, action, *args, **kwargs):
        agent = self.get_agent(agent_name)
        if agent and hasattr(agent, action):
            return getattr(agent, action)(*args, **kwargs)
        else:
            raise ValueError(f"Agent '{agent_name}' not found or action '{action}' is not available.")

    def list_agents(self):
        return list(self.agents.keys())