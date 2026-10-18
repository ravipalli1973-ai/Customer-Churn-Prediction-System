# 📊 Telecom Customer Churn Prediction System

[![CI Pipeline](https://github.com/ravipalli1973-ai/Customer-Churn-Prediction-System/actions/workflows/ci.yml/badge.svg)](https://github.com/ravipalli1973-ai/Customer-Churn-Prediction-System/actions/workflows/ci.yml)

![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Framework](https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white)
![ML](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Testing](https://img.shields.io/badge/pytest-passing-brightgreen)

## 📌 Overview
An end-to-end Machine Learning web application designed to forecast customer attrition for telecommunications providers. The system identifies churn risk probabilities in real time and suggests actionable retention strategies.

---

## 🏗️ Project Architecture
```text
Customer-Churn-Prediction-System/
├── app/
│   └── app.py               # Streamlit web dashboard
├── data/                    # Dataset storage
├── models/
│   └── customer_churn_pipeline.pkl  # Trained ML pipeline
├── notebooks/
│   └── churn_pipeline.ipynb # EDA & model training
├── src/
│   └── predict.py           # Preprocessing & inference pipeline
├── tests/
│   └── test_predict.py      # Automated unit tests
├── requirements.txt         # Project dependencies
└── README.md