# 💳 Credit Risk Prediction Web App

A Flask-based machine learning application that predicts credit risk (safe or risky) based on user input. This project helps banks and financial institutions automate loan approval decisions using a logistic regression model trained on borrower data.

---

## 🚀 Features

- Predicts loan default risk based on:
  - Age
  - Years of Employment
  - Income
  - Debt
- Interactive web form for data entry
- Machine learning model trained with scikit-learn
- Deployed on Heroku

---

## 🧠 Model Overview

- **Algorithm**: Logistic Regression
- **Trained on**: Cleaned dataset with 4 features
- **Saved as**: `credit_risk_model.pkl`

---

## 🛠 Tech Stack

- Python
- Flask
- scikit-learn
- Pandas
- HTML (Jinja2 templating)
- Heroku (for deployment)

---

## 📁 Project Structure

credit_risk_app/
├── app.py # Flask app
├── credit_risk_model.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── Procfile # Heroku startup config
├── templates/
│ └── index.html # Web UI
