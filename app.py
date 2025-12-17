from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import logging

app = FastAPI(title="Phishing Website Detection API")
logging.basicConfig(level=logging.INFO)
# Load trained model
model = joblib.load("phishing_model.pkl")

# Input schema matching dataset columns EXACTLY
class PhishingFeatures(BaseModel):
    url_length: int
    n_dots: int
    n_hypens: int
    n_underline: int
    n_slash: int
    n_questionmark: int
    n_equal: int
    n_at: int
    n_and: int
    n_exclamation: int
    n_space: int
    n_tilde: int
    n_comma: int
    n_plus: int
    n_asterisk: int
    n_hastag: int
    n_dollar: int
    n_percent: int
    n_redirection: int
    
@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_phishing(data: PhishingFeatures):
    features = [[
        data.url_length,
        data.n_dots,
        data.n_hypens,
        data.n_underline,
        data.n_slash,
        data.n_questionmark,
        data.n_equal,
        data.n_at,
        data.n_and,
        data.n_exclamation,
        data.n_space,
        data.n_tilde,
        data.n_comma,
        data.n_plus,
        data.n_asterisk,
        data.n_hastag,
        data.n_dollar,
        data.n_percent,
        data.n_redirection
    ]]
    logging.info(f"Incoming features: {features}")
    proba=model.predict_proba(features)[0]
    phishing_prob=proba[1]
    
    prediction="Phishing" if phishing_prob >= 0.6 else "Legitimate"
    logging.info(f"Prediction: {prediction}, Probability: {phishing_prob}")
    
    return {
        "prediction": prediction,
        "phishing_probability": round(phishing_prob,3)
    }