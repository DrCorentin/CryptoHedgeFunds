#src/backtester.py
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tools.utils import calculate_returns

# Load model
model = tf.keras.models.load_model("models/trained_model.h5")
# Load data
df = pd.read_csv("data/historical/data.csv")

# Preprocessing (same as training)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

# Backtesting loop
initial_capital_eur = 5000
initial_capital_btc = 1
predictions = []
for i in range(60, len(scaled_data)): # Start from sequence length
    x_input = scaled_data[i-60:i].reshape(1, -1, 1)
    yhat = model.predict(x_input)
    predictions.append(scaler.inverse_transform(yhat)[0][0])

df_backtest = df[60:].copy()
df_backtest['Predictions'] = predictions
df_backtest = calculate_returns(df_backtest, initial_capital_eur, initial_capital_btc)

df_backtest.to_csv("backtest_results.csv")
print("Backtesting results saved to backtest_results.csv")