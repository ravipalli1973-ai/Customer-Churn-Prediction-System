import streamlit as st
import pandas as pd
import pickle
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Churn Prediction System")

st.markdown("""
### Predict whether a telecom customer is likely to **Stay** or **Churn**
Fill in the customer details below and click **Predict Churn**.
""")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📌 About")

st.sidebar.info("""
**Customer Churn Prediction System**

**Model**
- Random Forest Classifier

**Accuracy**
- 80%

**Developed By**
- Ravipalli Tirumala Kumar
""")

# -----------------------------
# Load Model
# -----------------------------
model_path = os.path.join("models", "customer_churn_pipeline.pkl")

with open(model_path, "rb") as file:
    pipeline = pickle.load(file)

# -----------------------------
# Customer Details
# -----------------------------
st.subheader("Customer Information")

gender = st.selectbox("Gender", ["Female", "Male"])

senior = st.selectbox("Senior Citizen", ["No", "Yes"])

partner = st.selectbox("Partner", ["No", "Yes"])

dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)

phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = monthly_charges * tenure

# -----------------------------
# Predict
# -----------------------------
if st.button("🔍 Predict Churn"):

    user_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [1 if senior == "Yes" else 0],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    prediction = pipeline.predict(user_data)
    probability = pipeline.predict_proba(user_data)

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.error("🔴 High Risk of Churn")

        st.metric(
            "Churn Probability",
            f"{probability[0][1]*100:.2f}%"
        )

        st.warning("""
### Recommendation

✅ Offer a discount

✅ Recommend a yearly/two-year contract

✅ Contact the customer

✅ Improve customer support
""")

    else:

        st.success("🟢 Customer is likely to Stay")

        st.metric(
            "Stay Probability",
            f"{probability[0][0]*100:.2f}%"
        )

        st.balloons()

        st.info("""
### Recommendation

✅ Customer appears satisfied

✅ Continue providing quality service

✅ Offer loyalty rewards
""")