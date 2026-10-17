import pytest
import pandas as pd
from src.predict import prepare_input_dataframe

def test_prepare_input_dataframe_shape():
    sample_data = {
        "gender": "Male",
        "senior": "No",
        "partner": "Yes",
        "dependents": "No",
        "tenure": 24,
        "phone_service": "Yes",
        "multiple_lines": "No",
        "internet": "Fiber optic",
        "online_security": "No",
        "online_backup": "Yes",
        "device_protection": "No",
        "tech_support": "No",
        "streaming_tv": "Yes",
        "streaming_movies": "Yes",
        "contract": "Month-to-month",
        "paperless": "Yes",
        "payment": "Electronic check",
        "monthly_charges": 85.5
    }
    df = prepare_input_dataframe(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 1
    assert "TotalCharges" in df.columns
    assert df["TotalCharges"].iloc[0] == 85.5 * 24
    assert df["SeniorCitizen"].iloc[0] == 0

def test_prepare_input_senior_citizen_encoding():
    sample_senior = {"senior": "Yes", "monthly_charges": 50.0, "tenure": 10}
    df = prepare_input_dataframe(sample_senior)
    assert df["SeniorCitizen"].iloc[0] == 1
    assert df["TotalCharges"].iloc[0] == 500.0