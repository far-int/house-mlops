from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

@app.post("/predict")
def predict(area: float, rooms: int):
    prediction = model.predict([[area, rooms]])
    return {"predicted_price": prediction[0]}