# train_emg_model_keras.py

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Path to dataset directory
dataset_dir = "./dataset"

# Lists for storing data and labels
X_data = []
y_data = []

# Load EMG data from all subjects and gesture classes
for subject in range(1, 9):
    for label in range(5):
        file_path = os.path.join(dataset_dir, f"subject_{subject}/{label}.txt")
        
        if os.path.exists(file_path):
            data = np.loadtxt(file_path)

            # Ensure data has correct shape (handle single-row files)
            if data.ndim == 1:
                data = np.expand_dims(data, axis=0)

            X_data.append(data)

            # Assign label to each sample
            y_data.extend([label] * data.shape[0])

# Check if data is loaded correctly
if len(X_data) == 0:
    raise ValueError("No data found. Check your folder and file structure.")

# Combine all samples into one array
X_data = np.vstack(X_data)
y_data = np.array(y_data)

# Normalize data (important for neural networks)
scaler = StandardScaler()
X_data = scaler.fit_transform(X_data)

# Define sequence length for LSTM
timesteps = 10
features = X_data.shape[1]
samples = X_data.shape[0] - timesteps

# Create sequences (sliding window approach)
X_seq = np.array([X_data[i:i+timesteps] for i in range(samples)])
y_seq = y_data[timesteps:]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_seq, y_seq, test_size=0.2, random_state=42
)

# Define LSTM model architecture
model = Sequential([
    LSTM(64, input_shape=(timesteps, features)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')
])

# Compile model with optimizer, loss function, and evaluation metric
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Save model in Keras format
model.save('./models/emg_gesture_model.keras')

print("Model saved as ./models/emg_gesture_model.keras")
