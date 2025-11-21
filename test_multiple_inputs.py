"""Test multiple input scenarios to verify predictions"""
import requests
import json
import time

# Wait for server
time.sleep(2)

url = "http://localhost:5000/predict"

# Test cases with expected outcomes
test_cases = [
    {
        "name": "High CGPA, Low Income (Should be Eligible)",
        "data": {
            "year_of_study": 2,
            "cgpa": 3.8,
            "family_income": 30000,
            "cocurricular_score": 60,
            "leadership_positions": 1,
            "community_service_hours": 50
        }
    },
    {
        "name": "Very High CGPA (Should be Eligible - Merit)",
        "data": {
            "year_of_study": 3,
            "cgpa": 3.9,
            "family_income": 100000,
            "cocurricular_score": 50,
            "leadership_positions": 0,
            "community_service_hours": 0
        }
    },
    {
        "name": "Low CGPA, High Income (Should be Not Eligible)",
        "data": {
            "year_of_study": 2,
            "cgpa": 2.3,
            "family_income": 120000,
            "cocurricular_score": 40,
            "leadership_positions": 0,
            "community_service_hours": 10
        }
    },
    {
        "name": "Low Income, Moderate CGPA (Should be Eligible - Need-based)",
        "data": {
            "year_of_study": 1,
            "cgpa": 2.8,
            "family_income": 25000,
            "cocurricular_score": 50,
            "leadership_positions": 0,
            "community_service_hours": 20
        }
    },
    {
        "name": "Well-rounded Student (Should be Eligible)",
        "data": {
            "year_of_study": 3,
            "cgpa": 3.2,
            "family_income": 60000,
            "cocurricular_score": 85,
            "leadership_positions": 3,
            "community_service_hours": 50
        }
    },
    {
        "name": "Community Service Focus (Should be Eligible)",
        "data": {
            "year_of_study": 4,
            "cgpa": 3.0,
            "family_income": 70000,
            "cocurricular_score": 60,
            "leadership_positions": 1,
            "community_service_hours": 150
        }
    },
    {
        "name": "Average Student (Borderline)",
        "data": {
            "year_of_study": 2,
            "cgpa": 3.0,
            "family_income": 60000,
            "cocurricular_score": 50,
            "leadership_positions": 0,
            "community_service_hours": 30
        }
    }
]

print("=" * 70)
print("Testing Multiple Input Scenarios")
print("=" * 70)

for i, test_case in enumerate(test_cases, 1):
    print(f"\n{i}. {test_case['name']}")
    print(f"   Input: CGPA={test_case['data']['cgpa']}, Income={test_case['data']['family_income']}, "
          f"Co-curricular={test_case['data']['cocurricular_score']}, "
          f"Leadership={test_case['data']['leadership_positions']}, "
          f"Service={test_case['data']['community_service_hours']}")
    
    try:
        response = requests.post(url, json=test_case['data'], timeout=5)
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                prediction = result['prediction']
                probability = result['probability']
                eligible_prob = probability['eligible'] * 100
                
                status = "✅ ELIGIBLE" if prediction == 1 else "❌ NOT ELIGIBLE"
                print(f"   Result: {status} (Probability: {eligible_prob:.1f}%)")
                print(f"   All Models:")
                for model_name, pred in result['all_predictions'].items():
                    prob = result['all_probabilities'][model_name]['eligible'] * 100
                    pred_status = "✅" if pred == 1 else "❌"
                    print(f"     - {model_name}: {pred_status} ({prob:.1f}%)")
            else:
                print(f"   ❌ Error: {result.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Exception: {e}")
    
    time.sleep(0.5)  # Small delay between requests

print("\n" + "=" * 70)
print("Testing Complete!")
print("=" * 70)

