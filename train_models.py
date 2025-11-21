"""
Train ML models for Scholarship Eligibility Prediction
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import joblib
import json
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Load dataset
print("Loading dataset...")
df = pd.read_csv('scholarship_dataset.csv')

# Feature selection
features = ['year_of_study', 'cgpa', 'family_income', 'cocurricular_score', 
            'leadership_positions', 'community_service_hours']
X = df[features]
y = df['eligible']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Training set - Eligible: {y_train.sum()}, Not Eligible: {(y_train==0).sum()}")
print(f"Test set - Eligible: {y_test.sum()}, Not Eligible: {(y_test==0).sum()}")

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
}

# Train and evaluate models
results = {}

for name, model in models.items():
    print(f"\n{'='*50}")
    print(f"Training {name}...")
    
    # Train
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    results[name] = {
        'accuracy': float(accuracy),
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'confusion_matrix': cm.tolist()
    }
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print(f"Confusion Matrix:\n{cm}")
    
    # Save model
    filename = f'models/{name.lower().replace(" ", "_")}_model.pkl'
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

# Save results
with open('models/model_results.json', 'w') as f:
    json.dump(results, f, indent=2)

# Save feature names for later use
with open('models/features.json', 'w') as f:
    json.dump(features, f, indent=2)

print(f"\n{'='*50}")
print("Training completed!")
print(f"\nBest model by F1-Score: {max(results.items(), key=lambda x: x[1]['f1_score'])[0]}")

