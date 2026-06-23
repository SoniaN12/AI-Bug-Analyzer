from google import genai

from app.config import GEMINI_API_KEY
from app.models import BugReport

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_bug_with_ai(report: BugReport):
    prompt = f"""
You are an AI bug report analyzer.

Analyze this bug report and give a clear explanation with suggestions.

Title:
{report.title or "Not provided"}

Description:
{report.description or "Not provided"}

Language:
{report.language or "Unknown"}

Error Logs:
{report.error_logs or "Not provided"}

Code:
{report.code or "Not provided"}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text