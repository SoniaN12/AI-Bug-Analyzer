import requests

url = "http://127.0.0.1:8000/api/analyze-bug"

payload = {
    "title": "Login crashes",
    "language": "Python",
    "description": "The app crashes when checking user email.",
    "error_logs": "AttributeError: 'NoneType' object has no attribute 'email'",
    "code": """
def login(user):
    return user.email
"""
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())