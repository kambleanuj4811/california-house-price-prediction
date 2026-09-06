from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np


# --------------------------------------------------
# Create FastAPI app
# --------------------------------------------------

app = FastAPI(
    title="California House Price Prediction API",
    description="API for predicting California house prices using Machine Learning",
    version="1.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Load Model and Scaler
# --------------------------------------------------

model = joblib.load("model1.pkl")
scaler = joblib.load("scaler.pkl")


# --------------------------------------------------
# Input Data Structure
# --------------------------------------------------

class HouseData(BaseModel):

    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float

    ocean_proximity_INLAND: float
    ocean_proximity_ISLAND: float
    ocean_proximity_NEAR_BAY: float
    ocean_proximity_NEAR_OCEAN: float


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "California House Price Prediction API is running!"
    }


# --------------------------------------------------
# Prediction Route
# --------------------------------------------------

@app.post("/predict")
def predict(data: HouseData):

    # Keep EXACTLY the same order as training data
    input_data = np.array([[
        data.longitude,
        data.latitude,
        data.housing_median_age,
        data.total_rooms,
        data.total_bedrooms,
        data.population,
        data.households,
        data.median_income,
        data.ocean_proximity_INLAND,
        data.ocean_proximity_ISLAND,
        data.ocean_proximity_NEAR_BAY,
        data.ocean_proximity_NEAR_OCEAN
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Return result
    return {
        "prediction": float(prediction[0])
    }