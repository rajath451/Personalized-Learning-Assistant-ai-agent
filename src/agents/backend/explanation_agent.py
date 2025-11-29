class BaseAgent:
    def __init__(self, name):
        self.name = name

    def respond(self, query):
        raise NotImplementedError("This method should be overridden by subclasses.")


class ExplanationAgent(BaseAgent):
    def __init__(self):
        super().__init__("ExplanationAgent")

    def simplify_concept(self, concept):
        # Logic to simplify the concept
        return f"Simplified explanation of {concept}"

    def provide_explanation(self, query):
        # Logic to provide an explanation based on the user query
        return f"Explanation for: {query}"