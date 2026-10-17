import streamlit as st
import pickle
import os
import sys

# Ensure src module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import prepare_input_dataframe, make_prediction

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction System")

st.markdown("""
### Predict whether a telecom customer is likely to **Stay** or **Churn**
Fill in the customer details below and click **Predict Churn**.
""")

st.divider()

st.sidebar.title("📌 About")
st.sidebar.info("""
**Customer Churn Prediction System**

**Model**
- Random Forest Classifier (~80% accuracy)

**Developed By**
- Ravipalli Tirumala Kumar
""")

@st.cache_resource
def load_churn_model(path: str = os.path.join("models", "customer_churn_pipeline.pkl")):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}")
    with open(path, "rb") as file:
        return pickle.load(file)

try:
    pipeline = load_churn_model()
except Exception as e:
    st.error(f"⚠️ Error loading model pipeline: {e}")
    st.stop()

st.subheader("Customer Information")

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=12)
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)

if st.button("🔍 Predict Churn"):
    customer_dict = {
        "gender": gender,
        "senior": senior,
        "partner": partner,
        "dependents": dependents,
        "tenure": tenure,
        "phone_service": phone_service,
        "multiple_lines": multiple_lines,
        "internet": internet,
        "online_security": online_security,
        "online_backup": online_backup,
        "device_protection": device_protection,
        "tech_support": tech_support,
        "streaming_tv": streaming_tv,
        "streaming_movies": streaming_movies,
        "contract": contract,
        "paperless": paperless,
        "payment": payment,
        "monthly_charges": monthly_charges
    }

    input_df = prepare_input_dataframe(customer_dict)
    prediction, churn_prob = make_prediction(pipeline, input_df)

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🔴 High Risk of Churn")
        st.metric("Churn Probability", f"{churn_prob * 100:.2f}%")
        st.warning("""
### Recommended Retention Actions
- ✅ Offer a targeted discount or promotional rate
- ✅ Recommend transitioning to a long-term contract
- ✅ Schedule proactive outreach via customer success
""")
    else:
        st.success("🟢 Customer is likely to Stay")
        st.metric("Stay Probability", f"{(1 - churn_prob) * 100:.2f}%")
        st.balloons()
        st.info("""
### Recommended Actions
- ✅ Maintain service standards and monitor support logs
- ✅ Consider enrolling customer in loyalty incentives
""")