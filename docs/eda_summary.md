# Customer Churn Prediction System

## Exploratory Data Analysis (EDA) Summary

### Dataset Information

- Total Records (Original): 7043
- Total Records (After Cleaning): 7032
- Total Features: 21

---

## Data Cleaning

### Missing Values

- Initially, no missing values were detected because the `TotalCharges` column contained blank spaces (" ") instead of actual null values.
- Found 11 blank spaces in `TotalCharges`.
- Replaced blank spaces with `NaN`.
- Converted `TotalCharges` from string to float.
- Removed 11 rows containing missing values using `dropna()`.

### Duplicate Rows

- Duplicate rows found: 0

---

# Exploratory Data Analysis (EDA)

## 1. Customer Churn Distribution

Business Question:
How many customers stayed and how many left?

Result:

- Stayed: 5163
- Churned: 1869

Business Insight:

Approximately 73.4% of customers stayed, while 26.6% churned.

---

## 2. Gender vs Churn

Business Question:

Does gender affect customer churn?

Observation:

- Female Churn: 939
- Male Churn: 930

Business Insight:

Both genders have almost identical churn counts.

Conclusion:

Gender is not a strong predictor of customer churn.

---

## 3. Contract Type vs Churn

Business Question:

Does contract type affect customer churn?

Observation:

Month-to-month

- Stayed: 2220
- Churned: 1655

One Year

- Stayed: 1306
- Churned: 166

Two Year

- Stayed: 1637
- Churned: 48

Business Insight:

Customers with month-to-month contracts have the highest churn.

Customers with two-year contracts have the lowest churn.

Business Recommendation:

Encourage customers to switch to long-term contracts through discounts and loyalty rewards.

---

## 4. Tenure vs Churn

Business Question:

Does tenure affect customer churn?

Observation:

Stayed Customers

Average Tenure: 37.65 months

Churned Customers

Average Tenure: 17.98 months

Business Insight:

Customers who remain with the company longer are much less likely to churn.

Business Recommendation:

Focus retention campaigns on new customers during their first year.

---

## 5. Monthly Charges vs Churn

Business Question:

Do higher monthly charges increase churn?

Observation:

Stayed Customers

Average Monthly Charges: 61.31

Churned Customers

Average Monthly Charges: 74.44

Business Insight:

Customers paying higher monthly charges are more likely to churn.

Business Recommendation:

Offer discounts or value-added benefits to customers on expensive plans.

---

## 6. Internet Service vs Churn

Business Question:

Which internet service has the highest churn?

Observation:

DSL

- Stayed: 1957
- Churned: 459

Fiber Optic

- Stayed: 1799
- Churned: 1297

No Internet

- Stayed: 1407
- Churned: 113

Business Insight:

Fiber Optic customers show the highest churn.

Business Recommendation:

Investigate pricing, service quality, and customer satisfaction for Fiber Optic users.

---

## 7. Payment Method vs Churn

Business Question:

Does payment method affect churn?

Observation:

Bank Transfer

- Churned: 258

Credit Card

- Churned: 232

Electronic Check

- Churned: 1071

Mailed Check

- Churned: 308

Business Insight:

Electronic Check customers have the highest churn.

Business Recommendation:

Encourage customers to use automatic payment methods.

---

## 8. Senior Citizen vs Churn

Business Question:

Are senior citizens more likely to churn?

Observation:

Non-Senior Churn Rate:

23.7%

Senior Citizen Churn Rate:

41.7%

Business Insight:

Senior citizens churn much more frequently than non-senior customers.

Business Recommendation:

Provide special offers and dedicated customer support for senior citizens.

---

## 9. Correlation Analysis

Key Findings

- Tenure and TotalCharges show a strong positive correlation (0.826).
- MonthlyCharges and TotalCharges show a positive correlation (0.651).
- SeniorCitizen has almost no correlation with tenure.

Business Insight:

Longer customer relationships naturally lead to higher total charges.

---

# Overall EDA Conclusion

The most important features influencing customer churn are:

- Contract Type
- Tenure
- Monthly Charges
- Internet Service
- Payment Method
- Senior Citizen

Gender was found to have very little influence on customer churn.

These insights will be used to build machine learning models in the next phase of the project.