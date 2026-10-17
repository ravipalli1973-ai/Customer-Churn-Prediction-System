import pandas as pd
from typing import Dict, Any, Tuple

def prepare_input_dataframe(data: Dict[str, Any]) -> pd.DataFrame:
    """Formats raw customer input fields into a single-row DataFrame expected by the pipeline."""
    return pd.DataFrame({
        "gender": [data.get("gender", "Female")],
        "SeniorCitizen": [1 if data.get("senior") == "Yes" else 0],
        "Partner": [data.get("partner", "No")],
        "Dependents": [data.get("dependents", "No")],
        "tenure": [int(data.get("tenure", 0))],
        "PhoneService": [data.get("phone_service", "No")],
        "MultipleLines": [data.get("multiple_lines", "No")],
        "InternetService": [data.get("internet", "DSL")],
        "OnlineSecurity": [data.get("online_security", "No")],
        "OnlineBackup": [data.get("online_backup", "No")],
        "DeviceProtection": [data.get("device_protection", "No")],
        "TechSupport": [data.get("tech_support", "No")],
        "StreamingTV": [data.get("streaming_tv", "No")],
        "StreamingMovies": [data.get("streaming_movies", "No")],
        "Contract": [data.get("contract", "Month-to-month")],
        "PaperlessBilling": [data.get("paperless", "No")],
        "PaymentMethod": [data.get("payment", "Electronic check")],
        "MonthlyCharges": [float(data.get("monthly_charges", 0.0))],
        "TotalCharges": [float(data.get("monthly_charges", 0.0) * int(data.get("tenure", 0)))]
    })

def make_prediction(pipeline, input_df: pd.DataFrame) -> Tuple[int, float]:
    """Runs inference and returns the predicted label and churn probability."""
    prediction = int(pipeline.predict(input_df)[0])
    probabilities = pipeline.predict_proba(input_df)[0]
    churn_prob = float(probabilities[1])
    return prediction, churn_prob