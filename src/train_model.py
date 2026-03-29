import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

folder = "."

X_data = []
y_data = []

for label in range(5):
    for subject in range(1, 9):
        file_path = os.path.join(folder, f"subject_{subject}/{label}.txt")
        if os.path.exists(file_path):
            data = np.loadtxt(file_path)
            if data.ndim == 1:
                data = np.expand_dims(data, axis=0)
            X_data.append(data)
            y_data.extend([label] * data.shape[0])

if len(X_data) == 0:
    raise ValueError("No data found. Check your folder and file structure.")

X_data = np.vstack(X_data)
y_data = np.array(y_data)

scaler = StandardScaler()
X_data = scaler.fit_transform(X_data)

timesteps = 10
features = X_data.shape[1]
samples = X_data.shape[0] - timesteps

X_seq = np.array([X_data[i:i+timesteps] for i in range(samples)])
y_seq = y_data[timesteps:]

X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

model = Sequential([
    LSTM(64, input_shape=(timesteps, features)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

model.save('emg_gesture_model.h5')

print("Model saved as emg_gesture_model.h5")
