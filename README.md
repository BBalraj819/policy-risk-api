# Policy Risk Scoring API (FastAPI)

A FastAPI-based backend service that calculates and returns insurance policy risk scores based on input data.

## Overview
This project simulates how an insurance system might evaluate policy risk using structured inputs such as customer details, coverage type, and risk factors. The API processes this data and returns a calculated risk score along with explanations.

## Features
- REST API built with FastAPI
- Risk scoring logic based on multiple input factors
- JSON-based request and response handling
- Endpoint testing via Swagger UI
- Clean and modular Python structure

## Tech Stack
- Python
- FastAPI
- Uvicorn
- JSON

## Endpoints

### GET /health
Checks if the API is running.

### POST /risk-score
Accepts policy data and returns a calculated risk score.

## Example Request
```json
{
  "age": 30,
  "policy_type": "home",
  "location": "FL",
  "claim_history": 1
}
## Business Use Case
This project simulates how insurance companies evaluate policy risk before approving coverage. By analyzing structured inputs such as customer profile, location, and claim history, the API generates a risk score that can support underwriting decisions.

This type of system is commonly used in:
- Insurance underwriting platforms
- Risk assessment tools
- Data-driven decision systems

- Translating business rules into backend logic  

This project reflects my ability to combine technical development with business-focused problem solving.
