from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("random_forest_optimized.pkl")

# Create app instance
app = FastAPI(title="Early Disease Detection API")

# Define request structure
class InputData(BaseModel):
    Glucose: float
    BMI: float
    Age: float
    DiabetesPedigreeFunction: float
    risk_score: float  # Remember, we created this feature

@app.get("/")
def read_root():
    return {"message": "Welcome to the Early Disease Detection API"}

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[data.Glucose, data.BMI, data.Age, data.DiabetesPedigreeFunction, data.risk_score]])
    prediction = model.predict(input_array)[0]
    return {
        "prediction": int(prediction),
        "status": "Diabetic" if prediction == 1 else "Not Diabetic"
    }
