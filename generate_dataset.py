"""
Generate synthetic dataset for Scholarship Eligibility System
"""
import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of samples
n_samples = 2000

# Generate synthetic data
data = []

for i in range(n_samples):
    # Year of study (1-4)
    year_of_study = random.randint(1, 4)
    
    # CGPA (2.0 to 4.0)
    cgpa = round(np.random.normal(3.2, 0.5), 2)
    cgpa = max(2.0, min(4.0, cgpa))  # Clamp between 2.0 and 4.0
    
    # Family income (RM 0 to RM 150,000 per year)
    family_income = random.randint(0, 150000)
    
    # Co-curricular score (0-100)
    cocurricular_score = random.randint(0, 100)
    
    # Additional features
    # Number of leadership positions
    leadership_positions = random.randint(0, 5)
    
    # Community service hours
    community_service_hours = random.randint(0, 200)
    
    # Determine eligibility based on rules
    # Scholarship eligibility rules (simplified):
    eligible = False
    
    # Rule 1: High CGPA scholarship (CGPA >= 3.5, income < 50000)
    if cgpa >= 3.5 and family_income < 50000:
        eligible = True
    
    # Rule 2: Merit scholarship (CGPA >= 3.7, any income)
    if cgpa >= 3.7:
        eligible = True
    
    # Rule 3: Need-based scholarship (income < 30000, CGPA >= 2.5)
    if family_income < 30000 and cgpa >= 2.5:
        eligible = True
    
    # Rule 4: Excellence scholarship (CGPA >= 3.8, cocurricular >= 70)
    if cgpa >= 3.8 and cocurricular_score >= 70:
        eligible = True
    
    # Rule 5: Well-rounded scholarship (CGPA >= 3.0, cocurricular >= 80, leadership >= 2)
    if cgpa >= 3.0 and cocurricular_score >= 80 and leadership_positions >= 2:
        eligible = True
    
    # Rule 6: Community service scholarship (service >= 100 hours, CGPA >= 2.8)
    if community_service_hours >= 100 and cgpa >= 2.8:
        eligible = True
    
    # Add some noise - 5% chance of eligibility even if rules don't match
    if random.random() < 0.05:
        eligible = True
    
    # 5% chance of not being eligible even if rules match (edge cases)
    if random.random() < 0.05 and eligible:
        eligible = False
    
    data.append({
        'student_id': f'STU{i+1:04d}',
        'year_of_study': year_of_study,
        'cgpa': cgpa,
        'family_income': family_income,
        'cocurricular_score': cocurricular_score,
        'leadership_positions': leadership_positions,
        'community_service_hours': community_service_hours,
        'eligible': 1 if eligible else 0
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('scholarship_dataset.csv', index=False)
print(f"Dataset generated successfully with {len(df)} samples")
print(f"Eligible: {df['eligible'].sum()} ({df['eligible'].mean()*100:.1f}%)")
print(f"Not Eligible: {(df['eligible']==0).sum()} ({(df['eligible']==0).mean()*100:.1f}%)")
print("\nDataset Statistics:")
print(df.describe())

