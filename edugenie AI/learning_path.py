from ai_client import generate_text


def recommend_learning_path(goal):

    prompt = f"""
Create a learning path for a student
who wants to learn:

{goal}

Create three levels:

1. Beginner
2. Intermediate
3. Advanced

For each level include:
- Topics
- Activities
- Expected learning outcome

Use simple English.
"""

    result = generate_text(prompt)

    return {
        "goal": goal,
        "learning_path": result
    }