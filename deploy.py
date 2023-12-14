import os
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import joblib
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

class ForecastEnsembler:
    def __init__(self, rnn_model, e2d2_model, n_past, n_features):
        self.rnn_model = rnn_model
        self.e2d2_model = e2d2_model
        self.n_past = n_past
        self.n_features = n_features

    def generate_forecasts(self, last_sales_data):
        forecast_rnn = []
        forecast_e2d2 = []

        current_rnn = last_sales_data
        current_e2d2 = last_sales_data

        for day in range(365):
            predictions_rnn = self.rnn_model.predict(current_rnn)
            predictions_e2d2 = self.e2d2_model.predict(current_e2d2)

            flattened_pred_rnn = predictions_rnn.flatten()
            flattened_pred_e2d2 = predictions_e2d2.flatten()

            forecast_rnn.append(flattened_pred_rnn)
            forecast_e2d2.append(flattened_pred_e2d2)

            current_rnn = np.concatenate([current_rnn[:, 1:, :], predictions_rnn.reshape(1, 1, self.n_features)], axis=1)
            current_e2d2 = np.concatenate([current_e2d2[:, 1:, :], predictions_e2d2.reshape(1, 1, self.n_features)], axis=1)

        forecast_array_rnn = np.array(forecast_rnn)
        forecast_array_e2d2 = np.array(forecast_e2d2)

        ensemble_forecast = (forecast_array_rnn + forecast_array_e2d2) / 2.0

        return ensemble_forecast

rnn_model_path = "rnn_model.joblib"
e2d2_model_path = "e2d2_model.joblib"

# check if model files exist
if not os.path.exists(rnn_model_path) or not os.path.exists(e2d2_model_path):
    raise FileNotFoundError("Model files not found.")

# load models using joblib
rnn_model = joblib.load(rnn_model_path)
e2d2_model = joblib.load(e2d2_model_path)

n_past = past
n_features = features

# Instantiate ForecastEnsembler
forecaster = ForecastEnsembler(rnn_model, e2d2_model, n_past, n_features)
# Define route for the root
@app.route('/')
def home():
    # Render the HTML template
    return render_template('index.html')

# define API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json

    last_sales_data = np.array(data['last_sales_data']).reshape((1, n_past, n_features))

    # generate forecasts using ensemble model
    ensemble_forecast = forecaster.generate_forecasts(last_sales_data)

    # return the forecasts
    return jsonify({'ensemble_forecast': ensemble_forecast.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
