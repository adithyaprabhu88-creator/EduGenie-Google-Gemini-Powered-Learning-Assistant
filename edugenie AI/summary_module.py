from ai_client import generate_text


def summarize(text):

    prompt = f"""
Summarize the following educational text.

Rules:
- Keep the important information
- Remove unnecessary repetition
- Use simple English
- Give a short summary
- Add important points as bullets

Text:
{text}
"""

    return generate_text(prompt)