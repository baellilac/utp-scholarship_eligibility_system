# UTP Scholarship Eligibility System

An AI-powered web application that predicts scholarship eligibility for UTP students using machine learning models.

## Features

- **AI-Powered Prediction**: Uses multiple ML models (Logistic Regression, Decision Tree, Random Forest) to predict scholarship eligibility
- **Specific Scholarship Recommendations**: Get personalized eligibility status for specific scholarship providers:
  - **PETRONAS Scholarship**: For high-achieving students with strong leadership and community involvement
  - **MARA Scholarship**: Government scholarship for Bumiputera students with financial need
  - **Zakat Scholarship**: Need-based scholarship for lower-income families
  - **Yayasan UTP Scholarship**: Institutional scholarship for UTP students
- **Model Explanations**: Clear explanations of what each AI model does and how it makes predictions
- **User-Friendly Interface**: Modern, responsive web interface for easy interaction
- **Dashboard & Visualizations**: Interactive charts showing dataset statistics and model performance
- **Model Comparison**: Compare performance metrics across different ML models

## Project Structure

```
scholarship_eligibility_system/
├── app.py                      # Flask web application
├── generate_dataset.py         # Script to generate synthetic dataset
├── train_models.py            # Script to train ML models
├── requirements.txt           # Python dependencies
├── scholarship_dataset.csv    # Generated dataset (created after running generate_dataset.py)
├── models/                    # Trained models directory
│   ├── logistic_regression_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── model_results.json
│   └── features.json
├── templates/
│   └── index.html            # Main HTML template
└── static/
    ├── css/
    │   └── style.css         # Styling
    └── js/
        └── app.js            # Frontend JavaScript
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Dataset

```bash
python generate_dataset.py
```

This will create `scholarship_dataset.csv` with 2000 synthetic student records.

### 3. Train Models

```bash
python train_models.py
```

This will:
- Train three ML models (Logistic Regression, Decision Tree, Random Forest)
- Evaluate model performance
- Save trained models to the `models/` directory
- Generate performance metrics in `models/model_results.json`

### 4. Run the Web Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. **Predict Eligibility Tab**: 
   - Enter student information (CGPA, family income, co-curricular score, etc.)
   - Get instant eligibility predictions from all three AI models
   - View specific scholarship recommendations (PETRONAS, MARA, Zakat, Yayasan UTP)
   - See detailed explanations of why you're eligible or what to improve
   - Understand how each AI model works and what it means for your prediction

2. **Dashboard Tab**: View dataset statistics and visualizations including:
   - Eligibility distribution
   - CGPA distribution
   - Family income distribution

3. **Model Performance Tab**: Compare performance metrics (Accuracy, Precision, Recall, F1-Score) across all trained models.

## Dataset Features

- **Year of Study**: 1-4
- **CGPA**: 2.0 - 4.0
- **Family Income**: Annual income in RM
- **Co-curricular Score**: 0-100
- **Leadership Positions**: Number of leadership roles
- **Community Service Hours**: Total volunteer hours
- **Eligible**: Binary target variable (0 or 1)

## AI Models

The system uses three different AI models, each with its own approach:

1. **Logistic Regression** (Baseline): 
   - Statistical model that analyzes relationships using linear patterns
   - Provides a baseline prediction and is easy to interpret
   - Good for understanding general eligibility trends

2. **Decision Tree**: 
   - Rule-based model that makes decisions by following a tree of questions
   - Shows clear decision rules and is highly interpretable
   - Helps you understand exactly which criteria you meet or don't meet

3. **Random Forest** (Primary Model): 
   - Advanced ensemble model that combines multiple decision trees
   - Most accurate and reliable prediction, considers complex patterns
   - Used as the primary model for final eligibility determination

## Scholarship Provider Criteria

The system evaluates eligibility for four major scholarship providers:

### PETRONAS Scholarship
- **Requirements**: CGPA ≥ 3.5, Co-curricular ≥ 70, Leadership ≥ 2 positions, Community Service ≥ 50 hours
- **Focus**: High academic excellence with strong leadership and community involvement

### MARA Scholarship
- **Requirements**: Family Income ≤ RM 80,000, CGPA ≥ 3.0, Co-curricular ≥ 50
- **Focus**: Government scholarship for Bumiputera students with financial need

### Zakat Scholarship
- **Requirements**: Family Income ≤ RM 50,000, CGPA ≥ 2.8, Community Service ≥ 30 hours
- **Focus**: Need-based scholarship for lower-income families with community service involvement

### Yayasan UTP Scholarship
- **Requirements**: CGPA ≥ 3.2, (Income ≤ RM 100,000 OR Co-curricular ≥ 60)
- **Focus**: Institutional scholarship for UTP students with good academic standing

## Model Evaluation

Models are evaluated using:
- **Accuracy**: Overall correctness
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall

## Ethical Considerations

- Data is anonymized (no personal identifiers)
- Synthetic dataset used for demonstration
- Models trained on balanced dataset
- Transparent prediction probabilities shown to users

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Chart.js

## Future Enhancements

- Integration with UTP student database
- Additional scholarship providers and criteria
- Admin panel for model retraining
- Export prediction results
- Email notifications for scholarship opportunities


