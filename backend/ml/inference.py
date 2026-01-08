import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "artifacts/model.joblib")
vectorizer = joblib.load(BASE_DIR / "artifacts/vectorizer.joblib")

def predict_ticket(text):
    vec = vectorizer.transform([text])
    category = model.predict(vec)[0]

    text_lower = text.lower()
    sentiment = "Negative" if any(w in text_lower for w in ["failed", "refund", "error"]) else "Neutral"
    priority = "High" if sentiment == "Negative" else "Medium"

    return {
        "category": category,
        "sentiment": sentiment,
        "priority": priority
    }
