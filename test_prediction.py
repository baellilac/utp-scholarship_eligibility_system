"""Test prediction to debug the issue"""
import joblib
import numpy as np
import json

# Load models
print("Loading models...")
models = {}
model_files = {
    'Logistic Regression': 'models/logistic_regression_model.pkl',
    'Decision Tree': 'models/decision_tree_model.pkl',
    'Random Forest': 'models/random_forest_model.pkl'
}

for name, path in model_files.items():
    try:
        model = joblib.load(path)
        models[name] = model
        print(f"✓ Loaded {name}")
    except Exception as e:
        print(f"✗ Failed to load {name}: {e}")

# Test prediction
print("\nTesting prediction...")
input_features = np.array([[
    1,      # year_of_study
    3.2,    # cgpa
    50000,  # family_income
    50,     # cocurricular_score
    1,      # leadership_positions
    1       # community_service_hours
]])

print(f"Input shape: {input_features.shape}")
print(f"Input: {input_features}")

for name, model in models.items():
    try:
        print(f"\n--- {name} ---")
        pred = model.predict(input_features)
        print(f"Prediction shape: {pred.shape}")
        print(f"Prediction: {pred}")
        print(f"Prediction type: {type(pred)}")
        
        prob = model.predict_proba(input_features)
        print(f"Probability shape: {prob.shape}")
        print(f"Probability: {prob}")
        print(f"Probability type: {type(prob)}")
        
        if len(prob.shape) > 1:
            prob_array = prob[0]
        else:
            prob_array = prob
        
        print(f"Prob array length: {len(prob_array)}")
        print(f"Prob array: {prob_array}")
        
        if len(prob_array) >= 2:
            print(f"Not Eligible: {prob_array[0]}, Eligible: {prob_array[1]}")
        else:
            print(f"WARNING: Only {len(prob_array)} class(es) in probability array!")
            
    except Exception as e:
        import traceback
        print(f"ERROR with {name}: {e}")
        traceback.print_exc()

