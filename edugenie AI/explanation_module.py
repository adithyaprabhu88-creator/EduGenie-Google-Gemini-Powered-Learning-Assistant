from ai_client import generate_text


def explain(topic):

    prompt = f"""
You are an educational tutor.

Explain the following topic to a beginner.

Topic:
{topic}

Requirements:
- Use simple English
- Explain step by step
- Give a small example
- Keep it easy to understand
"""

    return generate_text(prompt)