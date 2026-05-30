import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_ai_explanation(error_message, category):

    prompt = f"""
    You are an expert backend engineer.

    Analyze this API error.

    Error Message:
    {error_message}

    Detected Category:
    {category}

    Explain:
    1. Why this error happens
    2. How to fix it
    3. Best practices to avoid it

    Keep response concise and technical.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content