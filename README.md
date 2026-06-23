# AI-Bug-Analyzer
<img width="1419" height="573" alt="Screenshot 2026-06-23 at 14 22 15" src="https://github.com/user-attachments/assets/cf471571-4afc-46ba-a070-97338b102e73" />

AI Bug Report Analyzer is a python based application that uses Google's Gemini AI to analyze software bug reports , users can  submit bug descriptions , error logs , and source code and the system provides explanations, identifies possible causes and suggests fixes.

# Technologies used 
Python
FASTAPI
Google Gemini AI
Python Dotenv

# Installation.
1. Clone the repository.
```bash
git clone <https://github.com/SoniaN12/AI-Bug-Analyzer.git>
cd AI-Bug-Analyzer
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Create a .env file:
```env
GEMINI_API_KEY = _api_key_here
```
# Running the application.
Start the Server:
```bash
uvicorn app.main:app --reload
```
Opening Swagger UI:
```bash
http://127.0.0.1:8000/docs
```
Example
```JSON
{
  "title": "Users can log in with wrong password",
  "description": "Authentication succeeds unexpectedly.",
  "language": "Java",
  "error_logs": "",
  "code": "if password == password:\n    return True"
}
```
Example Response
```JSON
{
  "success": true,
  "gemini_response": "This is a **critical security vulnerability** with a straightforward root cause.....
}
```
# How it works
1. User submits a bug report.
2. FASTAPI receives request.
3. The bug details are sent to Gemini AI.
4. Gemini analyzes the issue.
5. The analysis is returned to the user.


