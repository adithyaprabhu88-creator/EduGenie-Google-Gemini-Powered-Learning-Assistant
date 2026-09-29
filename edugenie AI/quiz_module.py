import json
from ai_client import generate_text


def generate_quiz(topic, num_questions=5):

    prompt = f"""
Create {num_questions} multiple-choice questions
about {topic}.

Each question must contain:
- question
- four options
- correct_answer
- explanation

Return ONLY valid JSON.

Format:

[
  {{
    "question": "Question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option A",
    "explanation": "Explanation"
  }}
]
"""

    response = generate_text(prompt)

    try:
        questions = json.loads(response)

        return {
            "topic": topic,
            "questions": questions
        }

    except json.JSONDecodeError:

        return {
            "topic": topic,
            "questions": [],
            "error": "Unable to generate quiz."
        }