@echo off
echo Setting up UTP Scholarship Eligibility System...
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
echo.

echo Step 2: Generating dataset...
python generate_dataset.py
echo.

echo Step 3: Training models...
python train_models.py
echo.

echo Setup complete!
echo.
echo To run the application, execute: python app.py
echo Then open your browser to: http://localhost:5000
pause

