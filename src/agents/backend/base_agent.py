class BaseAgent:
    def __init__(self, name):
        self.name = name

    def perform_action(self, *args, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def get_name(self):
        return self.name

    def provide_feedback(self, feedback):
        raise NotImplementedError("This method should be overridden by subclasses.")