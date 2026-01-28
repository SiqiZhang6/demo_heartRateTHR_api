from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define what the incoming data looks like
class HeartRateData(BaseModel):
    heart_rate: int

@app.get("/")
def home():
    return {"message": "Heart Health API is Live!"}

@app.post("/predict")
def predict_health(data: HeartRateData):
    # Your "Most Simple Model Possible"
    threshold = 100
    
    if data.heart_rate > threshold:
        status = "High"
        recommendation = "Please rest and hydrate."
    elif data.heart_rate < 60:
        status = "Low"
        recommendation = "Monitor for dizziness."
    else:
        status = "Normal"
        recommendation = "Your heart rate is within a healthy range."

    return {
        "heart_rate": data.heart_rate,
        "status": status,
        "recommendation": recommendation
    }