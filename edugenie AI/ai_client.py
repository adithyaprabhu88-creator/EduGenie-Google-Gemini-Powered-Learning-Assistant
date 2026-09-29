import time
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL


# Check API key
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add your API key to the .env file."
    )


# Create Gemini client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_text(prompt: str) -> str:

    # Models to try
    models_to_try = [
        GEMINI_MODEL,
        "gemini-3.8-flash",
        "gemini-3.5-flash-lite"
    ]

    # Remove duplicate model names
    models_to_try = list(dict.fromkeys(models_to_try))

    last_error = None

    for model in models_to_try:

        # Try each model up to 2 times
        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response and response.text:
                    return response.text

                return "No response was generated."

            except Exception as e:

                last_error = e
                error_message = str(e)

                # Retry temporary server errors
                if "503" in error_message or "UNAVAILABLE" in error_message:

                    if attempt == 0:
                        time.sleep(3)
                        continue

                    # Try next model
                    break

                # For other errors, show useful message
                raise RuntimeError(
                    f"Gemini API Error: {error_message}"
                ) from e

    # All models failed
    raise RuntimeError(
        "Gemini AI service is temporarily unavailable. "
        "Please try again after a few seconds. "
        f"Last error: {last_error}"
    )