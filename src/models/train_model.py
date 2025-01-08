import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import datetime
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("path/to/your/data.csv")

# Preprocessing
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

# Create training sequences
def create_sequences(data, seq_length):
  xs = []
  ys = []
  for i in range(len(data)-seq_length-1):
    x = data[i:(i+seq_length)]
    y = data[i+seq_length]
    xs.append(x)
    ys.append(y)
  return np.array(xs), np.array(ys)

SEQ_LEN = 60 # Number of past days to use for prediction
X, y = create_sequences(scaled_data, SEQ_LEN)

# Split data into training and validation sets
train_size = int(len(X) * 0.8)
X_train, y_train = X[:train_size], y[:train_size]
X_val, y_val = X[train_size:], y[train_size:]

# Build LSTM model
model = keras.Sequential()
model.add(keras.layers.LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(keras.layers.LSTM(units=50))
model.add(keras.layers.Dense(units=1))

# Compile the model with optimizer, loss function, and validation metrics
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # Add 'mae' for mean absolute error

# Use TensorBoard for detailed logging (comment out if not desired)
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model with validation split
history = model.fit(X_train, y_train, epochs=25, batch_size=32, validation_data=(X_val, y_val), callbacks=[tensorboard_callback])

# Plot loss curves to visualize learning progress
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Save the trained model
model.save("models/trained_model.h5")