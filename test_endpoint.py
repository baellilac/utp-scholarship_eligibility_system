"""Test the Flask endpoint"""
import requests
import json
import time

# Wait for server to start
time.sleep(2)

url = "http://localhost:5000/predict"
data = {
    "year_of_study": 1,
    "cgpa": 3.2,
    "family_income": 50000,
    "cocurricular_score": 50,
    "leadership_positions": 1,
    "community_service_hours": 1
}

print("Testing Flask endpoint...")
print(f"URL: {url}")
print(f"Data: {json.dumps(data, indent=2)}")

try:
    response = requests.post(url, json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

