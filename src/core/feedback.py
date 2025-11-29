def generate_feedback(user_performance, agent_output):
    feedback_messages = []

    if user_performance['score'] < 50:
        feedback_messages.append("It seems you're struggling with this topic. Consider reviewing the material again.")
    elif 50 <= user_performance['score'] < 75:
        feedback_messages.append("You're doing well, but there's room for improvement. Keep practicing!")
    else:
        feedback_messages.append("Great job! You're mastering this topic.")

    feedback_messages.append(f"Agent feedback: {agent_output}")

    return feedback_messages

def adaptive_feedback(user_profile, agent_output):
    feedback = generate_feedback(user_profile['performance'], agent_output)
    return {
        "feedback": feedback,
        "suggestions": user_profile['suggestions']
    }