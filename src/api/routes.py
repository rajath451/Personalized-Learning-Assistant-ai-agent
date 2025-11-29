from flask import Blueprint, request, jsonify
from src.agents.quiz_agent import QuizAgent
from src.agents.explanation_agent import ExplanationAgent
from src.agents.scheduler_agent import SchedulerAgent

api = Blueprint('api', __name__)

quiz_agent = QuizAgent()
explanation_agent = ExplanationAgent()
scheduler_agent = SchedulerAgent()

@api.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_response = request.json.get('response')
        result = quiz_agent.evaluate_response(user_response)
        return jsonify(result)
    questions = quiz_agent.generate_questions()
    return jsonify(questions)

@api.route('/explanation', methods=['POST'])
def explanation():
    query = request.json.get('query')
    explanation = explanation_agent.provide_explanation(query)
    return jsonify(explanation)

@api.route('/schedule', methods=['POST'])
def schedule():
    schedule_data = request.json
    confirmation = scheduler_agent.plan_study_session(schedule_data)
    return jsonify(confirmation)