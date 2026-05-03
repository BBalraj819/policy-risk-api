from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Policy Risk Insights API")


class PolicyInput(BaseModel):
    age: int
    claims_count: int
    late_payments: int
    policy_lapse_history: bool


@app.get("/")
def home():
    return {"message": "Welcome to the Policy Risk Insights API"}


@app.get("/health")
def health_check():
    return {"status": "API is running"}


@app.post("/risk-score")
def calculate_risk(data: PolicyInput):
    score = 0

    score += data.claims_count * 20
    score += data.late_payments * 15

    if data.policy_lapse_history:
        score += 25

    if data.age < 25:
        score += 10

    if score < 30:
        risk_level = "Low"
        recommendation = "No immediate action needed."
    elif score < 70:
        risk_level = "Medium"
        recommendation = "Monitor policy and consider customer engagement."
    else:
        risk_level = "High"
        recommendation = "Proactive retention outreach recommended."

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "recommendation": recommendation
    }