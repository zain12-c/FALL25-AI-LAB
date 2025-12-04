
NutriTrack - AI-Powered Food Calorie Estimator
==============================================

Files included:
- nutritrack_dataset_600.xlsx   : Synthetic dataset (600 rows) with meal_description, cooking_method, estimated_calories.
- model_training.py             : Script to train a regression model (RandomForest) and save a model bundle.
- nutritrack_model_bundle.joblib: Generated after running model_training.py (NOT included by default).
- app.py                        : Flask app with a /predict endpoint and a basic UI (templates/index.html).
- templates/index.html          : Web UI for testing the app.
- help.json                     : Simple usage notes.
- README.md                     : This file.
- requirements.txt              : Python dependencies

How to run:
1. Create a Python environment (Anaconda or venv) and install requirements:
   pip install -r requirements.txt
2. (Optional) Train the model:
   python model_training.py
   This will produce nutritrack_model_bundle.joblib
3. Run the Flask app:
   python app.py
4. Open http://127.0.0.1:5000 in your browser.

Created programmatically.
