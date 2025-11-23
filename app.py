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

def get_scholarship_recommendations(year_of_study, cgpa, family_income, cocurricular_score, 
                                    leadership_positions, community_service_hours):
    """
    Determine specific scholarship provider eligibility based on student profile.
    Returns list of eligible scholarships with reasons.
    """
    recommendations = []
    
    # PETRONAS Scholarship Criteria
    # High academic excellence, leadership, and community involvement
    petronas_eligible = (
        cgpa >= 3.5 and
        cocurricular_score >= 70 and
        leadership_positions >= 2 and
        community_service_hours >= 50
    )
    if petronas_eligible:
        recommendations.append({
            'provider': 'PETRONAS',
            'name': 'PETRONAS Scholarship',
            'eligible': True,
            'confidence': 'High',
            'reasons': [
                f'CGPA {cgpa:.2f} meets requirement (≥3.5)',
                f'Co-curricular score {cocurricular_score} meets requirement (≥70)',
                f'Leadership experience: {leadership_positions} positions',
                f'Community service: {community_service_hours} hours'
            ],
            'description': 'Prestigious scholarship for high-achieving students with strong leadership and community involvement.'
        })
    else:
        reasons = []
        if cgpa < 3.5:
            reasons.append(f'CGPA {cgpa:.2f} below requirement (need ≥3.5)')
        if cocurricular_score < 70:
            reasons.append(f'Co-curricular score {cocurricular_score} below requirement (need ≥70)')
        if leadership_positions < 2:
            reasons.append(f'Leadership positions {leadership_positions} below requirement (need ≥2)')
        if community_service_hours < 50:
            reasons.append(f'Community service {community_service_hours} hours below requirement (need ≥50)')
        
        recommendations.append({
            'provider': 'PETRONAS',
            'name': 'PETRONAS Scholarship',
            'eligible': False,
            'confidence': 'Low',
            'reasons': reasons,
            'description': 'Prestigious scholarship for high-achieving students with strong leadership and community involvement.'
        })
    
    # MARA Scholarship Criteria
    # Focus on Bumiputera students, need-based, good academic performance
    mara_eligible = (
        family_income <= 80000 and
        cgpa >= 3.0 and
        cocurricular_score >= 50
    )
    if mara_eligible:
        recommendations.append({
            'provider': 'MARA',
            'name': 'MARA Scholarship',
            'eligible': True,
            'confidence': 'High',
            'reasons': [
                f'Family income RM {family_income:,} meets requirement (≤RM 80,000)',
                f'CGPA {cgpa:.2f} meets requirement (≥3.0)',
                f'Co-curricular score {cocurricular_score} meets requirement (≥50)'
            ],
            'description': 'Government scholarship for Bumiputera students with financial need and good academic performance.'
        })
    else:
        reasons = []
        if family_income > 80000:
            reasons.append(f'Family income RM {family_income:,} exceeds requirement (need ≤RM 80,000)')
        if cgpa < 3.0:
            reasons.append(f'CGPA {cgpa:.2f} below requirement (need ≥3.0)')
        if cocurricular_score < 50:
            reasons.append(f'Co-curricular score {cocurricular_score} below requirement (need ≥50)')
        
        recommendations.append({
            'provider': 'MARA',
            'name': 'MARA Scholarship',
            'eligible': False,
            'confidence': 'Low',
            'reasons': reasons,
            'description': 'Government scholarship for Bumiputera students with financial need and good academic performance.'
        })
    
    # Zakat Scholarship Criteria
    # Need-based, lower income threshold, moderate academic requirements
    zakat_eligible = (
        family_income <= 50000 and
        cgpa >= 2.8 and
        community_service_hours >= 30
    )
    if zakat_eligible:
        recommendations.append({
            'provider': 'Zakat',
            'name': 'Zakat Scholarship',
            'eligible': True,
            'confidence': 'High',
            'reasons': [
                f'Family income RM {family_income:,} meets requirement (≤RM 50,000)',
                f'CGPA {cgpa:.2f} meets requirement (≥2.8)',
                f'Community service: {community_service_hours} hours meets requirement (≥30)'
            ],
            'description': 'Need-based scholarship for students from lower-income families with community service involvement.'
        })
    else:
        reasons = []
        if family_income > 50000:
            reasons.append(f'Family income RM {family_income:,} exceeds requirement (need ≤RM 50,000)')
        if cgpa < 2.8:
            reasons.append(f'CGPA {cgpa:.2f} below requirement (need ≥2.8)')
        if community_service_hours < 30:
            reasons.append(f'Community service {community_service_hours} hours below requirement (need ≥30)')
        
        recommendations.append({
            'provider': 'Zakat',
            'name': 'Zakat Scholarship',
            'eligible': False,
            'confidence': 'Low',
            'reasons': reasons,
            'description': 'Need-based scholarship for students from lower-income families with community service involvement.'
        })
    
    # Yayasan UTP Scholarship Criteria
    # UTP-specific, balanced criteria, supports UTP students
    yayasan_utp_eligible = (
        cgpa >= 3.2 and
        (family_income <= 100000 or cocurricular_score >= 60) and
        year_of_study >= 1
    )
    if yayasan_utp_eligible:
        recommendations.append({
            'provider': 'Yayasan UTP',
            'name': 'Yayasan UTP Scholarship',
            'eligible': True,
            'confidence': 'High',
            'reasons': [
                f'CGPA {cgpa:.2f} meets requirement (≥3.2)',
                f'Family income RM {family_income:,} or co-curricular score {cocurricular_score} meets requirement',
                f'Currently in Year {int(year_of_study)} of study'
            ],
            'description': 'Institutional scholarship for UTP students with good academic standing and active participation.'
        })
    else:
        reasons = []
        if cgpa < 3.2:
            reasons.append(f'CGPA {cgpa:.2f} below requirement (need ≥3.2)')
        if family_income > 100000 and cocurricular_score < 60:
            reasons.append(f'Need either family income ≤RM 100,000 or co-curricular score ≥60')
        
        recommendations.append({
            'provider': 'Yayasan UTP',
            'name': 'Yayasan UTP Scholarship',
            'eligible': False,
            'confidence': 'Low',
            'reasons': reasons,
            'description': 'Institutional scholarship for UTP students with good academic standing and active participation.'
        })
    
    return recommendations

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
        
        # Get specific scholarship provider recommendations
        scholarship_recommendations = get_scholarship_recommendations(
            year_of_study=float(data.get('year_of_study', 1)),
            cgpa=float(data.get('cgpa', 3.0)),
            family_income=float(data.get('family_income', 50000)),
            cocurricular_score=float(data.get('cocurricular_score', 50)),
            leadership_positions=float(data.get('leadership_positions', 0)),
            community_service_hours=float(data.get('community_service_hours', 0))
        )
        
        # Count eligible scholarships
        eligible_scholarships = [s for s in scholarship_recommendations if s['eligible']]
        
        # Model explanations for end users
        model_explanations = {
            'Logistic Regression': {
                'description': 'A statistical model that analyzes the relationship between your profile and scholarship eligibility using linear patterns.',
                'strength': 'Provides a baseline prediction and is easy to interpret.',
                'use_case': 'Good for understanding general eligibility trends.'
            },
            'Decision Tree': {
                'description': 'A rule-based model that makes decisions by following a tree of questions about your profile (e.g., "Is CGPA > 3.5?").',
                'strength': 'Shows clear decision rules and is highly interpretable.',
                'use_case': 'Helps you understand exactly which criteria you meet or don\'t meet.'
            },
            'Random Forest': {
                'description': 'An advanced model that combines multiple decision trees to make more accurate predictions.',
                'strength': 'Most accurate and reliable prediction, considers complex patterns.',
                'use_case': 'Primary model used for final eligibility determination.'
            }
        }
        
        return jsonify({
            'success': True,
            'prediction': int(primary_prediction),
            'probability': primary_probability,
            'all_predictions': predictions,
            'all_probabilities': probabilities,
            'model_used': primary_model,
            'model_explanations': model_explanations,
            'scholarship_recommendations': scholarship_recommendations,
            'eligible_scholarships_count': len(eligible_scholarships),
            'eligible_scholarships': [s['provider'] for s in eligible_scholarships]
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

