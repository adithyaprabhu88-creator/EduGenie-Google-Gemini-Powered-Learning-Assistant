from ai_client import generate_text


def answer_question(question):

    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the following student question
in simple and clear language.

Question:
{question}

Give an accurate and concise answer.
"""

    return generate_text(prompt)