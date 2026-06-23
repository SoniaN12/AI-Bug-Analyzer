from typing import Optional, List
from pydantic import BaseModel


class BugReport(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    language: Optional[str] = None
    error_logs: Optional[str] = None


class BugAnalysis(BaseModel):
    bugSummary: str
    likelyCause: str
    severity: str
    bugType: str
    affectedCode: str
    suggestedFix: str
    fixedCodeExample: str
    preventionTips: List[str]