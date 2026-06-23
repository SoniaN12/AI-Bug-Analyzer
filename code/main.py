from fastapi import FastAPI, HTTPException
from app.models import BugReport
from app.analyzer import analyze_bug_with_ai
import traceback

app = FastAPI(title="AI Bug Report Analyzer")


@app.get("/")
def home():
    return {
        "message": "AI Bug Report Analyzer API is running",
        "docs": "http://127.0.0.1:8000/docs",
        "endpoint": "/api/analyze-bug"
    }


@app.post("/api/analyze-bug")
def analyze_bug(report: BugReport):
    if not report.description and not report.code and not report.error_logs:
        raise HTTPException(
            status_code=400,
            detail="Please provide a bug description, code, or error logs."
        )

    try:
        gemini_response = analyze_bug_with_ai(report)

        return {
            "success": True,
            "gemini_response": gemini_response
        }

    except Exception as e:
        traceback.print_exc()

        error_text = str(e)

        if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
            raise HTTPException(
                status_code=429,
                detail="Gemini quota exceeded. Please wait and try again."
            )

        if "503" in error_text or "UNAVAILABLE" in error_text:
            raise HTTPException(
                status_code=503,
                detail="Gemini is busy right now. Please try again later."
            )

        raise HTTPException(
            status_code=500,
            detail=error_text
        )