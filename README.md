# 🏠 California House Price Prediction

A Machine Learning web application that predicts **California house prices** based on housing and location-related features.

The project uses a trained Machine Learning model with **FastAPI** as the backend and a simple **HTML, CSS, and JavaScript** frontend.

---

## 🚀 Project Overview

This project predicts the median house value of a California district using features such as:

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

The Machine Learning model is served through a FastAPI REST API, while the frontend provides an easy-to-use interface for making predictions.

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* HTML
* CSS
* JavaScript

### Development

* Jupyter Notebook
* Git
* GitHub

---

## 📂 Project Structure

```text
california-house-price-prediction/
│
├── app.py
├── model1.pkl
├── scaler.pkl
├── requirements.txt
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## 🤖 Machine Learning Model

The model takes **12 input features**:

| Feature                      | Description                     |
| ---------------------------- | ------------------------------- |
| `longitude`                  | Longitude of the district       |
| `latitude`                   | Latitude of the district        |
| `housing_median_age`         | Median age of houses            |
| `total_rooms`                | Total number of rooms           |
| `total_bedrooms`             | Total number of bedrooms        |
| `population`                 | Population of the district      |
| `households`                 | Number of households            |
| `median_income`              | Median income                   |
| `ocean_proximity_INLAND`     | One-hot encoded ocean proximity |
| `ocean_proximity_ISLAND`     | One-hot encoded ocean proximity |
| `ocean_proximity_NEAR_BAY`   | One-hot encoded ocean proximity |
| `ocean_proximity_NEAR_OCEAN` | One-hot encoded ocean proximity |

The input data is first transformed using the saved `scaler.pkl`, and then passed to the trained model stored in `model1.pkl`.

---

## 🔄 Application Workflow

```text
User
  │
  ▼
Frontend
HTML + CSS + JavaScript
  │
  │ POST /predict
  ▼
FastAPI Backend
  │
  ▼
scaler.pkl
  │
  ▼
model1.pkl
  │
  ▼
Predicted House Price
  │
  ▼
Frontend
```

---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kambleanuj4811/california-house-price-prediction.git
```

Move into the project:

```bash
cd california-house-price-prediction
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install them manually:

```bash
pip install fastapi uvicorn pydantic joblib numpy scikit-learn
```

---

## ▶️ Run the FastAPI Backend

Start the server:

```bash
uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the `/predict` endpoint directly from the Swagger UI.

---

## 🔮 Prediction API

### Endpoint

```text
POST /predict
```

### Example Request

```json
{
  "longitude": -121.89,
  "latitude": 37.34,
  "housing_median_age": 25,
  "total_rooms": 1800,
  "total_bedrooms": 350,
  "population": 850,
  "households": 320,
  "median_income": 4.5,
  "ocean_proximity_INLAND": 1,
  "ocean_proximity_ISLAND": 0,
  "ocean_proximity_NEAR_BAY": 0,
  "ocean_proximity_NEAR_OCEAN": 0
}
```

### Example Response

```json
{
  "prediction": 250000.0
}
```

The exact prediction depends on the trained model.

---

## 🌐 Frontend

The frontend provides a form where users can enter the housing information and select the ocean proximity.

JavaScript sends the input data to the FastAPI backend using a `POST` request.

```text
Frontend → FastAPI → ML Model → Prediction → Frontend
```

---

## 🔐 CORS

The FastAPI backend is configured with CORS middleware so that the frontend can communicate with the API even when running on a different local port.

---

## 📊 Input Example

For an inland property:

```text
INLAND       = 1
ISLAND       = 0
NEAR BAY     = 0
NEAR OCEAN   = 0
```

For a property near the bay:

```text
INLAND       = 0
ISLAND       = 0
NEAR BAY     = 1
NEAR OCEAN   = 0
```

---

## 💡 Features

* 🏠 California house price prediction
* 🤖 Machine Learning model
* ⚡ FastAPI REST API
* 📊 Scaled input features
* 🌐 Interactive web frontend
* 🔌 Frontend-backend integration
* 📖 Automatic Swagger API documentation
* 📱 Responsive frontend design

---

## 🔮 Future Improvements

* Deploy the application online
* Add model performance metrics
* Add data visualization
* Improve UI/UX
* Add prediction history
* Add multiple ML models for comparison
* Containerize the application using Docker
* Add automated CI/CD deployment

---

## 👨‍💻 Author

**Anuj Kamble**

GitHub:

https://github.com/kambleanuj4811

---

## ⭐ If You Like This Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub!

---
