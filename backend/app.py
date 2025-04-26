from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)
CORS(app)

# Root route (basic check)
@app.route('/')
def home():
    return 'Heart Disease Prediction API is running.'

# Load the trained model and scaler
with open('models/heart_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features from the request JSON
        features = [
            float(data['age']),
            float(data['sex']),
            float(data['cp']),
            float(data['trestbps']),
            float(data['chol']),
            float(data['fbs']),
            float(data['restecg']),
            float(data['thalach']),
            float(data['exang']),
            float(data['oldpeak']),
            float(data['slope']),
            float(data['ca']),
            float(data['thal'])
        ]

        # Scale the input features
        scaled_features = scaler.transform([features])

        # Make the prediction
        prediction = model.predict(scaled_features)[0]

        # Return the result as JSON
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
