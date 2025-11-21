# AI-Powered Scholarship Eligibility System for UTP Students

**Group Project Report**

**Course:** Artificial Intelligence  
**Institution:** Universiti Teknologi PETRONAS (UTP)  
**Date:** December 2024

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Introduction](#introduction)
3. [Problem Statement and Significance](#problem-statement-and-significance)
4. [Objectives](#objectives)
5. [Literature Review](#literature-review)
6. [Methodology](#methodology)
7. [Data Collection and Preprocessing](#data-collection-and-preprocessing)
8. [Model Development](#model-development)
9. [Model Evaluation](#model-evaluation)
10. [System Implementation](#system-implementation)
11. [Results and Discussion](#results-and-discussion)
12. [Ethical Considerations](#ethical-considerations)
13. [Limitations and Future Work](#limitations-and-future-work)
14. [Conclusion](#conclusion)
15. [References](#references)
16. [Appendices](#appendices)

---

## 1. Executive Summary

This project presents an AI-powered scholarship eligibility system designed specifically for Universiti Teknologi PETRONAS (UTP) students. The system utilizes supervised machine learning algorithms to predict scholarship eligibility based on student academic performance, financial background, and co-curricular activities. Three machine learning models were developed and evaluated: Logistic Regression (baseline), Decision Tree, and Random Forest. The Random Forest model achieved the best performance with 93.25% accuracy, 94.29% precision, 94.67% recall, and 94.48% F1-score. A web-based application was developed to provide an intuitive interface for students to check their scholarship eligibility in real-time, complete with interactive visualizations and model performance metrics.

**Key Achievements:**
- Developed three ML models with Random Forest achieving 93.25% accuracy
- Created a user-friendly web application with real-time predictions
- Implemented comprehensive data visualization dashboard
- Ensured ethical data handling with anonymized synthetic dataset

---

## 2. Introduction

Scholarship programs play a crucial role in supporting students' educational journeys, particularly in higher education institutions. However, the process of identifying and applying for suitable scholarships can be overwhelming for students due to the complexity of eligibility criteria and the vast number of available opportunities. This challenge is particularly relevant at UTP, where numerous scholarship programs exist with varying requirements.

Artificial Intelligence (AI) and Machine Learning (ML) technologies offer promising solutions to automate and optimize the scholarship matching process. By leveraging historical data and eligibility patterns, ML models can accurately predict scholarship eligibility, thereby reducing the time and effort required for students to identify suitable opportunities.

This project aims to develop an AI-powered system that automatically matches UTP students with appropriate scholarships based on their academic performance, financial background, and co-curricular achievements. The system employs supervised machine learning techniques to learn from historical eligibility patterns and provide accurate predictions.

---

## 3. Problem Statement and Significance

### 3.1 Problem Statement

Many UTP students struggle to find scholarships they qualify for due to:
1. **Numerous Options**: Multiple scholarship programs with different eligibility criteria
2. **Complex Requirements**: Eligibility criteria often involve multiple factors (CGPA, income, activities, etc.)
3. **Time Constraints**: Manual checking of each scholarship is time-consuming
4. **Missed Opportunities**: Students may miss suitable scholarships due to lack of awareness
5. **Inefficient Process**: Current manual process is inefficient for both students and administrators

### 3.2 Significance

This project addresses a real-world problem within the UTP environment by:

1. **Improving Accessibility**: Making scholarship information more accessible to all students
2. **Saving Time**: Reducing the time required to identify suitable scholarships
3. **Increasing Fairness**: Ensuring transparent and consistent eligibility assessment
4. **Enhancing Efficiency**: Streamlining the scholarship recommendation process
5. **Supporting Decision-Making**: Providing data-driven insights for both students and administrators

The system can be integrated into UTP's existing financial aid infrastructure, potentially improving student participation in scholarship programs and ensuring optimal distribution of financial resources.

---

## 4. Objectives

The primary objectives of this project are:

1. **Develop an AI System**: Create a machine learning-based system that identifies scholarships based on students' academic, co-curricular, and financial background
2. **Minimize Time and Effort**: Reduce the time and effort required for students to find suitable scholarships
3. **Provide User-Friendly Interface**: Develop an intuitive web interface for personalized scholarship recommendations
4. **Ensure Accuracy**: Achieve high prediction accuracy through appropriate model selection and evaluation
5. **Enable Scalability**: Design a system that can be easily extended and enhanced by UTP's financial aid unit

### Expected Outcomes

- A working prototype that accurately recommends scholarships
- Improved student participation in financial aid programs
- A scalable system for future enhancement
- Comprehensive evaluation metrics demonstrating model performance

---

## 5. Literature Review

### 5.1 Machine Learning in Education

Machine learning has been increasingly applied in educational contexts, including student performance prediction, course recommendation, and scholarship allocation. Supervised learning algorithms, particularly classification models, have shown effectiveness in predicting student outcomes based on various features.

### 5.2 Scholarship Recommendation Systems

Previous research has explored automated scholarship matching systems using various approaches:
- **Rule-based systems**: Use predefined rules but lack flexibility
- **Machine learning approaches**: Learn patterns from data, offering better adaptability
- **Hybrid systems**: Combine rule-based and ML approaches

### 5.3 Classification Algorithms

For binary classification tasks like scholarship eligibility prediction, several algorithms have proven effective:
- **Logistic Regression**: Linear model providing interpretable results
- **Decision Trees**: Non-linear models that learn decision rules
- **Random Forest**: Ensemble method combining multiple decision trees for improved accuracy

### 5.4 Evaluation Metrics

Classification models are typically evaluated using:
- **Accuracy**: Overall correctness of predictions
- **Precision**: Proportion of positive predictions that are correct
- **Recall**: Proportion of actual positives correctly identified
- **F1-Score**: Harmonic mean of precision and recall

---

## 6. Methodology

### 6.1 Research Design

This project follows a systematic approach:
1. **Problem Analysis**: Identify requirements and constraints
2. **Data Collection**: Generate synthetic dataset representing UTP student population
3. **Data Preprocessing**: Clean, normalize, and prepare data for modeling
4. **Model Development**: Train and evaluate multiple ML algorithms
5. **System Implementation**: Develop web-based application
6. **Evaluation**: Assess model performance and system usability

### 6.2 AI Method Selection

**Supervised Machine Learning** was selected as the primary approach because:
- Historical eligibility data can be used for training
- Binary classification (eligible/not eligible) is well-suited for supervised learning
- Supervised learning provides interpretable results and probability scores

**Model Selection Rationale:**
1. **Logistic Regression (Baseline)**: Simple, interpretable, establishes baseline performance
2. **Decision Tree**: Non-linear, interpretable decision rules, handles complex patterns
3. **Random Forest**: Ensemble method, typically achieves highest accuracy, robust to overfitting

### 6.3 System Architecture

The system follows a client-server architecture:
- **Frontend**: HTML, CSS, JavaScript with Chart.js for visualizations
- **Backend**: Flask (Python) web framework
- **ML Models**: scikit-learn library
- **Data Storage**: CSV files and serialized model files (.pkl)

---

## 7. Data Collection and Preprocessing

### 7.1 Data Sources

Due to privacy and ethical considerations, a **synthetic dataset** was generated to represent UTP student population. The dataset was created based on:
- Typical UTP student characteristics
- Common scholarship eligibility criteria
- Realistic distributions of academic and financial metrics

### 7.2 Dataset Description

**Dataset Size**: 2,000 student records

**Features**:
1. **Year of Study** (1-4): Student's current academic year
2. **CGPA** (2.0-4.0): Cumulative Grade Point Average
3. **Family Income** (RM 0-150,000): Annual household income in Malaysian Ringgit
4. **Co-curricular Score** (0-100): Participation score in activities and clubs
5. **Leadership Positions** (0-5): Number of leadership roles held
6. **Community Service Hours** (0-200): Total volunteer hours

**Target Variable**:
- **Eligible** (0 or 1): Binary classification label indicating scholarship eligibility

### 7.3 Eligibility Rules

The dataset was generated based on realistic scholarship eligibility rules:

1. **High CGPA Scholarship**: CGPA ≥ 3.5 AND Income < RM 50,000
2. **Merit Scholarship**: CGPA ≥ 3.7 (any income)
3. **Need-based Scholarship**: Income < RM 30,000 AND CGPA ≥ 2.5
4. **Excellence Scholarship**: CGPA ≥ 3.8 AND Co-curricular ≥ 70
5. **Well-rounded Scholarship**: CGPA ≥ 3.0 AND Co-curricular ≥ 80 AND Leadership ≥ 2
6. **Community Service Scholarship**: Service Hours ≥ 100 AND CGPA ≥ 2.8

### 7.4 Data Preprocessing

**Steps Performed**:
1. **Data Generation**: Created 2,000 synthetic records with realistic distributions
2. **Feature Engineering**: Ensured all features are in appropriate ranges
3. **Label Assignment**: Applied eligibility rules with 5% noise for realism
4. **Data Validation**: Verified data quality and consistency
5. **Train-Test Split**: 80% training (1,600 samples) and 20% testing (400 samples)
6. **Stratified Sampling**: Maintained class distribution in train/test splits

**Dataset Statistics**:
- **Eligible**: 1,218 students (60.9%)
- **Not Eligible**: 782 students (39.1%)
- **Mean CGPA**: 3.21
- **Mean Income**: RM 75,000
- **Mean Co-curricular Score**: 50.5

### 7.5 Data Quality

- **Completeness**: 100% (no missing values)
- **Consistency**: All values within valid ranges
- **Balance**: Reasonable class distribution (60.9% vs 39.1%)
- **Anonymization**: No personal identifiers included

---

## 8. Model Development

### 8.1 Feature Selection

All six features were selected for model training:
- Year of Study
- CGPA
- Family Income
- Co-curricular Score
- Leadership Positions
- Community Service Hours

These features were chosen based on:
- Relevance to scholarship eligibility criteria
- Availability in typical student records
- Discriminative power for classification

### 8.2 Model Training

**Training Procedure**:
1. **Data Splitting**: 80/20 train-test split with stratification
2. **Model Initialization**: Three models with appropriate hyperparameters
3. **Training**: Models trained on training set
4. **Evaluation**: Performance assessed on test set
5. **Persistence**: Trained models saved for deployment

**Model Configurations**:

1. **Logistic Regression**:
   - Algorithm: LogisticRegression
   - Max iterations: 1000
   - Random state: 42

2. **Decision Tree**:
   - Algorithm: DecisionTreeClassifier
   - Max depth: 10
   - Random state: 42

3. **Random Forest**:
   - Algorithm: RandomForestClassifier
   - Number of estimators: 100
   - Max depth: 10
   - Random state: 42

### 8.3 Training Results

**Training Set**:
- Size: 1,600 samples
- Eligible: 974 (60.9%)
- Not Eligible: 626 (39.1%)

**Test Set**:
- Size: 400 samples
- Eligible: 244 (61.0%)
- Not Eligible: 156 (39.0%)

All models successfully completed training without errors.

---

## 9. Model Evaluation

### 9.1 Evaluation Metrics

Models were evaluated using four key metrics:

1. **Accuracy**: Overall percentage of correct predictions
2. **Precision**: Proportion of predicted eligible students who are actually eligible
3. **Recall**: Proportion of actually eligible students correctly identified
4. **F1-Score**: Harmonic mean of precision and recall

### 9.2 Results

#### 9.2.1 Logistic Regression (Baseline)

| Metric | Value |
|--------|-------|
| Accuracy | 70.75% |
| Precision | 71.67% |
| Recall | 86.07% |
| F1-Score | 78.21% |

**Confusion Matrix**:
```
                Predicted
Actual       Not Eligible  Eligible
Not Eligible      73         83
Eligible          34        210
```

**Analysis**: Logistic Regression provides a reasonable baseline with 70.75% accuracy. It shows high recall (86.07%), meaning it correctly identifies most eligible students, but lower precision (71.67%), indicating some false positives.

#### 9.2.2 Decision Tree

| Metric | Value |
|--------|-------|
| Accuracy | 91.00% |
| Precision | 93.33% |
| Recall | 91.80% |
| F1-Score | 92.56% |

**Confusion Matrix**:
```
                Predicted
Actual       Not Eligible  Eligible
Not Eligible     140         16
Eligible          20        224
```

**Analysis**: Decision Tree significantly outperforms the baseline with 91.00% accuracy. It achieves balanced precision (93.33%) and recall (91.80%), indicating good overall performance with fewer false positives and false negatives.

#### 9.2.3 Random Forest

| Metric | Value |
|--------|-------|
| Accuracy | **93.25%** |
| Precision | **94.29%** |
| Recall | **94.67%** |
| F1-Score | **94.48%** |

**Confusion Matrix**:
```
                Predicted
Actual       Not Eligible  Eligible
Not Eligible     142         14
Eligible          13        231
```

**Analysis**: Random Forest achieves the best performance across all metrics:
- Highest accuracy (93.25%)
- Highest precision (94.29%) - fewer false positives
- Highest recall (94.67%) - fewer false negatives
- Highest F1-Score (94.48%) - best overall balance

### 9.3 Model Comparison

**Performance Ranking**:
1. **Random Forest**: 93.25% accuracy (Best)
2. **Decision Tree**: 91.00% accuracy
3. **Logistic Regression**: 70.75% accuracy (Baseline)

**Key Observations**:
- Random Forest outperforms other models by 2.25% over Decision Tree
- Decision Tree shows 20.25% improvement over baseline
- All models achieve recall > 85%, indicating good identification of eligible students
- Random Forest provides the best balance between precision and recall

### 9.4 Model Selection

**Random Forest** was selected as the primary model for deployment because:
1. Highest overall accuracy (93.25%)
2. Best precision (94.29%) - minimizes false positives
3. Best recall (94.67%) - minimizes false negatives
4. Robust ensemble method less prone to overfitting
5. Provides probability scores for uncertainty quantification

---

## 10. System Implementation

### 10.1 System Architecture

The system consists of three main components:

1. **Backend (Flask)**: 
   - Handles HTTP requests
   - Loads trained models
   - Performs predictions
   - Serves API endpoints

2. **Frontend (HTML/CSS/JavaScript)**:
   - User interface for input
   - Displays prediction results
   - Interactive visualizations
   - Responsive design

3. **ML Models**:
   - Serialized model files (.pkl)
   - Feature definitions
   - Performance metrics

### 10.2 Key Features

#### 10.2.1 Prediction Interface
- Input form for student information
- Real-time eligibility prediction
- Probability scores for transparency
- Predictions from all three models for comparison

#### 10.2.2 Dashboard
- Dataset statistics overview
- Eligibility distribution visualization
- CGPA distribution chart
- Family income distribution chart

#### 10.2.3 Model Performance Tab
- Side-by-side model comparison
- Detailed performance metrics
- Interactive performance charts

### 10.3 Technical Stack

- **Backend**: Python 3.11, Flask 3.1.2
- **Machine Learning**: scikit-learn 1.2.2
- **Data Processing**: pandas 2.3.3, numpy 1.26.0
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Visualization**: Chart.js
- **Model Persistence**: joblib

### 10.4 User Interface Design

The interface features:
- **Modern Design**: Gradient backgrounds, card-based layout
- **Responsive**: Works on desktop and mobile devices
- **Intuitive Navigation**: Tab-based interface
- **Visual Feedback**: Color-coded results (green for eligible, red for not eligible)
- **Interactive Charts**: Dynamic visualizations using Chart.js

---

## 11. Results and Discussion

### 11.1 Model Performance Analysis

The Random Forest model achieved excellent performance with 93.25% accuracy, demonstrating the effectiveness of ensemble methods for this classification task. The high precision (94.29%) indicates that when the model predicts a student is eligible, it is correct 94.29% of the time. The high recall (94.67%) means the model identifies 94.67% of all actually eligible students.

### 11.2 Feature Importance

While explicit feature importance analysis was not performed in this iteration, the model's performance suggests that:
- **CGPA** is likely the most important feature (high correlation with eligibility)
- **Family Income** plays a significant role (need-based scholarships)
- **Co-curricular activities** contribute to eligibility (well-rounded scholarships)
- **Leadership and Service** provide additional signals for certain scholarship types

### 11.3 Error Analysis

From the confusion matrices:
- **False Positives**: Students predicted as eligible but actually not eligible
  - Random Forest: 14 cases (3.5% of test set)
  - These may represent edge cases or students close to eligibility threshold

- **False Negatives**: Eligible students predicted as not eligible
  - Random Forest: 13 cases (3.25% of test set)
  - These represent missed opportunities that should be minimized

### 11.4 System Usability

The web application provides:
- **Ease of Use**: Simple form-based input
- **Fast Response**: Real-time predictions (< 1 second)
- **Transparency**: Shows probabilities and all model predictions
- **Visualization**: Clear charts and statistics
- **Accessibility**: Works on standard web browsers

### 11.5 Comparison with Baseline

The Random Forest model shows:
- **22.5% improvement** in accuracy over Logistic Regression
- **2.25% improvement** over Decision Tree
- Significantly better precision and recall
- More robust predictions through ensemble averaging

---

## 12. Ethical Considerations

### 12.1 Data Privacy

- **Anonymization**: No personal identifiers in the dataset
- **Synthetic Data**: Generated dataset prevents privacy concerns
- **Secure Storage**: Models and data stored locally, not in cloud
- **No Tracking**: System does not store user input or predictions

### 12.2 Fairness and Bias

- **Balanced Dataset**: Reasonable distribution of eligible/not eligible (60.9%/39.1%)
- **Transparent Criteria**: Eligibility rules are based on standard scholarship criteria
- **Equal Treatment**: All students evaluated using same criteria
- **Bias Mitigation**: Models trained on diverse student profiles

### 12.3 Transparency

- **Explainable Predictions**: Probability scores provided
- **Model Comparison**: Users can see predictions from all models
- **Performance Metrics**: Model accuracy and metrics are displayed
- **Open Methodology**: All code and methodology documented

### 12.4 Consent and Usage

- **Educational Purpose**: System developed for academic project
- **Informed Use**: Users understand predictions are for guidance only
- **No Guarantee**: Predictions do not guarantee actual scholarship awards
- **Recommendation Only**: System provides recommendations, not final decisions

### 12.5 Future Deployment Considerations

For production deployment:
- Obtain proper consent for data collection
- Implement data encryption
- Regular model retraining with new data
- Bias auditing and mitigation
- Compliance with data protection regulations

---

## 13. Limitations and Future Work

### 13.1 Current Limitations

1. **Synthetic Data**: Dataset is generated, not from real UTP records
2. **Limited Features**: Only 6 features considered; more could improve accuracy
3. **Binary Classification**: Does not recommend specific scholarship types
4. **Static Model**: Models not retrained with new data automatically
5. **No Historical Data**: Cannot learn from actual UTP scholarship awards
6. **Single Institution**: Designed for UTP; may need adaptation for other institutions

### 13.2 Future Enhancements

1. **Real Data Integration**: 
   - Integrate with UTP student database (with proper consent)
   - Use historical scholarship award data
   - Continuous learning from new data

2. **Enhanced Features**:
   - Program of study
   - Extracurricular achievements
   - Awards and honors
   - Financial need indicators

3. **Multi-class Classification**:
   - Predict specific scholarship types
   - Rank scholarships by suitability
   - Provide personalized recommendations

4. **Advanced Models**:
   - Neural networks for complex patterns
   - Deep learning for feature extraction
   - Ensemble of diverse algorithms

5. **System Features**:
   - User accounts and history
   - Email notifications for new scholarships
   - Admin panel for model management
   - Export functionality for reports

6. **Integration**:
   - UTP student portal integration
   - Financial aid office system integration
   - Mobile application development

7. **Evaluation**:
   - A/B testing with real users
   - User satisfaction surveys
   - Impact assessment on scholarship applications

---

## 14. Conclusion

This project successfully developed an AI-powered scholarship eligibility system for UTP students using supervised machine learning. The system demonstrates strong performance with the Random Forest model achieving 93.25% accuracy, significantly outperforming the baseline Logistic Regression model (70.75% accuracy).

**Key Achievements**:
1. Developed three ML models with comprehensive evaluation
2. Created a user-friendly web application with real-time predictions
3. Implemented interactive visualizations and performance dashboards
4. Ensured ethical data handling and transparent predictions

**Impact**:
The system addresses a real-world problem within the UTP environment, potentially improving student access to scholarship opportunities and streamlining the recommendation process. The scalable architecture allows for future enhancements and integration with UTP's financial aid infrastructure.

**Learning Outcomes**:
Through this project, we have:
1. Identified and formulated a real-world problem in the UTP environment
2. Analyzed different AI methods and justified model selection
3. Designed and implemented an AI-based prototype with appropriate algorithms
4. Demonstrated teamwork, responsibility, and ethical conduct in development

The system is ready for demonstration and can serve as a foundation for future development and deployment at UTP.

---

## 15. References

1. Breiman, L. (2001). Random forests. *Machine learning*, 45(1), 5-32.

2. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer.

3. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of machine learning research*, 12(Oct), 2825-2830.

4. Provost, F., & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O'Reilly Media.

5. Witten, I. H., Frank, E., & Hall, M. A. (2011). *Data Mining: Practical Machine Learning Tools and Techniques*. Morgan Kaufmann.

6. Zhang, L., et al. (2020). Machine learning applications in education: A systematic review. *Computers & Education*, 145, 103739.

---

## 16. Appendices

### Appendix A: Dataset Statistics

**Full Dataset (2,000 samples)**:
- Mean CGPA: 3.21
- Mean Family Income: RM 75,029
- Mean Co-curricular Score: 50.5
- Mean Leadership Positions: 2.5
- Mean Community Service Hours: 101.1

**Eligibility Distribution**:
- Eligible: 1,218 (60.9%)
- Not Eligible: 782 (39.1%)

### Appendix B: Code Structure

```
scholarship_eligibility_system/
├── app.py                      # Flask web application
├── generate_dataset.py         # Dataset generation script
├── train_models.py            # Model training script
├── requirements.txt           # Python dependencies
├── scholarship_dataset.csv    # Generated dataset
├── models/                    # Trained models
│   ├── logistic_regression_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── model_results.json
│   └── features.json
├── templates/
│   └── index.html            # Web interface
└── static/
    ├── css/
    │   └── style.css         # Styling
    └── js/
        └── app.js            # Frontend logic
```

### Appendix C: Model Hyperparameters

**Logistic Regression**:
- Solver: 'lbfgs'
- Max iterations: 1000
- Random state: 42

**Decision Tree**:
- Criterion: 'gini'
- Max depth: 10
- Min samples split: 2
- Random state: 42

**Random Forest**:
- Number of estimators: 100
- Max depth: 10
- Min samples split: 2
- Random state: 42

### Appendix D: System Screenshots

*[Note: Include screenshots of the web interface, prediction results, dashboard, and model performance tabs in the actual report]*

### Appendix E: API Endpoints

1. **GET /** - Main page
2. **POST /predict** - Get eligibility prediction
   - Input: JSON with student features
   - Output: JSON with prediction and probabilities
3. **GET /model_info** - Get model performance metrics
4. **GET /dataset_stats** - Get dataset statistics

---

**End of Report**

