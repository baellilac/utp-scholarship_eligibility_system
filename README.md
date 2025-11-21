# UTP Scholarship Eligibility System

An AI-powered web application that predicts scholarship eligibility for UTP students using machine learning models.

## Features

- **AI-Powered Prediction**: Uses multiple ML models (Logistic Regression, Decision Tree, Random Forest) to predict scholarship eligibility
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

1. **Predict Eligibility Tab**: Enter student information (CGPA, family income, co-curricular score, etc.) and get instant eligibility predictions from all models.

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

1. **Logistic Regression** (Baseline): Linear model for binary classification
2. **Decision Tree**: Non-linear model that learns decision rules
3. **Random Forest**: Ensemble method combining multiple decision trees

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
- Support for multiple scholarship types
- Recommendation system for specific scholarships
- Admin panel for model retraining
- Export prediction results

## License

This project is developed for educational purposes as part of the UTP AI Group Project.

## Authors

UTP AI Group Project Team

