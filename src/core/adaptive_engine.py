class AdaptiveEngine:
    def __init__(self):
        self.user_performance_data = {}

    def update_performance(self, user_id, performance_metrics):
        if user_id not in self.user_performance_data:
            self.user_performance_data[user_id] = []
        self.user_performance_data[user_id].append(performance_metrics)

    def generate_feedback(self, user_id):
        if user_id not in self.user_performance_data:
            return "No performance data available."
        
        metrics = self.user_performance_data[user_id]
        average_score = sum(metric['score'] for metric in metrics) / len(metrics)
        
        if average_score >= 80:
            return "Great job! Keep up the good work!"
        elif average_score >= 50:
            return "You're doing well, but there's room for improvement."
        else:
            return "It looks like you need to review the material. Don't hesitate to ask for help!"