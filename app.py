from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('credit_risk_model.pkl')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Explicitly read the four form inputs
        age = float(request.form['feature1'])
        employ = float(request.form['feature2'])
        income = float(request.form['feature3'])
        debtinc = float(request.form['feature4'])

        # Create a DataFrame with correct column names
        input_data = pd.DataFrame([[age, employ, income, debtinc]],
                                  columns=['Age', 'Years of Employment', 'Income', 'Debt'])

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Risky" if prediction == 1 else "Safe"

        return render_template('index.html', prediction_text=f"Loan Risk Prediction: {result}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")
    
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

