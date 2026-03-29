import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Root folder where dataset is located
folder = "."

# Lists to store input data and labels
X_data = []
y_data = []

# Load EMG data from all subjects and gesture labels
for label in range(5):
    for subject in range(1, 9):
        file_path = os.path.join(folder, f"subject_{subject}/{label}.txt")
        
        if os.path.exists(file_path):
            data = np.loadtxt(file_path)

            # Ensure correct shape if file contains a single sample
            if data.ndim == 1:
                data = np.expand_dims(data, axis=0)

            X_data.append(data)

            # Assign label for each sample
            y_data.extend([label] * data.shape[0])

# Validate that data was loaded successfully
if len(X_data) == 0:
    raise ValueError("No data found. Check your folder and file structure.")

# Combine all loaded data into a single array
X_data = np.vstack(X_data)
y_data = np.array(y_data)

# Normalize features for better model performance
scaler = StandardScaler()
X_data = scaler.fit_transform(X_data)

# Define LSTM sequence parameters
timesteps = 10
features = X_data.shape[1]
samples = X_data.shape[0] - timesteps

# Create sequences using sliding window approach
X_seq = np.array([X_data[i:i+timesteps] for i in range(samples)])
y_seq = y_data[timesteps:]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_seq, y_seq, test_size=0.2, random_state=42
)

# Define LSTM-based neural network model
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

# Train the model on the dataset
model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Save trained model to file
model.save('emg_gesture_model.h5')

print("Model saved as emg_gesture_model.h5")
