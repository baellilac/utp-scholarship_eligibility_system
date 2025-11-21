"""
Flask Web Application for Scholarship Eligibility System
"""
from flask import Flask, render_template, request, jsonify
import joblib
import json
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os

app = Flask(__name__)

# Load models and features
models = {}
features = []

def load_models():
    """Load all trained models"""
    global models, features
    
    model_files = {
        'Logistic Regression': 'models/logistic_regression_model.pkl',
        'Decision Tree': 'models/decision_tree_model.pkl',
        'Random Forest': 'models/random_forest_model.pkl'
    }
    
    for name, path in model_files.items():
        if os.path.exists(path):
            models[name] = joblib.load(path)
    
    # Load features
    if os.path.exists('models/features.json'):
        with open('models/features.json', 'r') as f:
            features = json.load(f)
    
    print(f"Loaded {len(models)} models")

# Load models on startup
load_models()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict scholarship eligibility"""
    try:
        if not models:
            return jsonify({
                'success': False,
                'error': 'Models not loaded. Please train models first.'
            }), 500
        
        data = request.json
        
        # Extract features
        input_features = np.array([[
            float(data.get('year_of_study', 1)),
            float(data.get('cgpa', 3.0)),
            float(data.get('family_income', 50000)),
            float(data.get('cocurricular_score', 50)),
            float(data.get('leadership_positions', 0)),
            float(data.get('community_service_hours', 0))
        ]])
        
        predictions = {}
        probabilities = {}
        
        # Get predictions from all models
        for name, model in models.items():
            try:
                pred = model.predict(input_features)
                prob = model.predict_proba(input_features)
                
                # Handle different array shapes
                if len(pred.shape) > 0:
                    pred_value = int(pred[0])
                else:
                    pred_value = int(pred)
                
                # Handle probability array
                if len(prob.shape) > 1:
                    prob_array = prob[0]
                else:
                    prob_array = prob
                
                # Ensure we have at least 2 classes
                if len(prob_array) >= 2:
                    predictions[name] = pred_value
                    probabilities[name] = {
                        'not_eligible': float(prob_array[0]),
                        'eligible': float(prob_array[1])
                    }
                else:
                    # Fallback if only one class probability is returned
                    predictions[name] = pred_value
                    prob_val = float(prob_array[0]) if len(prob_array) > 0 else 0.5
                    probabilities[name] = {
                        'not_eligible': 1.0 - prob_val,
                        'eligible': prob_val
                    }
            except Exception as e:
                print(f"Error with model {name}: {str(e)}")
                continue
        
        if not predictions:
            return jsonify({
                'success': False,
                'error': 'Failed to get predictions from any model.'
            }), 500
        
        # Use Random Forest as primary model (usually best)
        primary_model = 'Random Forest' if 'Random Forest' in predictions else list(predictions.keys())[0]
        primary_prediction = predictions[primary_model]
        primary_probability = probabilities[primary_model]
        
        return jsonify({
            'success': True,
            'prediction': int(primary_prediction),
            'probability': primary_probability,
            'all_predictions': predictions,
            'all_probabilities': probabilities,
            'model_used': primary_model
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Prediction error: {error_details}")
        return jsonify({
            'success': False,
            'error': f'Prediction failed: {str(e)}'
        }), 400

@app.route('/model_info', methods=['GET'])
def model_info():
    """Get model performance information"""
    try:
        if os.path.exists('models/model_results.json'):
            with open('models/model_results.json', 'r') as f:
                results = json.load(f)
            return jsonify({
                'success': True,
                'results': results
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Model results not found. Please train models first.'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/dataset_stats', methods=['GET'])
def dataset_stats():
    """Get dataset statistics"""
    try:
        if os.path.exists('scholarship_dataset.csv'):
            df = pd.read_csv('scholarship_dataset.csv')
            
            stats = {
                'total_samples': len(df),
                'eligible_count': int(df['eligible'].sum()),
                'not_eligible_count': int((df['eligible'] == 0).sum()),
                'eligible_percentage': float(df['eligible'].mean() * 100),
                'features': {
                    'year_of_study': {
                        'min': float(df['year_of_study'].min()),
                        'max': float(df['year_of_study'].max()),
                        'mean': float(df['year_of_study'].mean())
                    },
                    'cgpa': {
                        'min': float(df['cgpa'].min()),
                        'max': float(df['cgpa'].max()),
                        'mean': float(df['cgpa'].mean())
                    },
                    'family_income': {
                        'min': float(df['family_income'].min()),
                        'max': float(df['family_income'].max()),
                        'mean': float(df['family_income'].mean())
                    },
                    'cocurricular_score': {
                        'min': float(df['cocurricular_score'].min()),
                        'max': float(df['cocurricular_score'].max()),
                        'mean': float(df['cocurricular_score'].mean())
                    }
                }
            }
            
            return jsonify({
                'success': True,
                'stats': stats
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Dataset not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

