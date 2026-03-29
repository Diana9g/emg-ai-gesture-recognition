# Project Overview

This project implements an EMG-based gesture recognition pipeline for AI-driven robotic control.

The system combines machine learning, ROS communication, and Unity-based simulation.

## Main workflow

1. EMG signals are collected and processed in Python
2. A neural network model (LSTM) is trained using TensorFlow/Keras
3. Real-time gesture recognition is performed
4. Recognized gestures are published through ROS
5. Unity subscribes to the gesture topic and triggers robotic actions
6. The Niryo One robot performs simulated motion based on planned trajectories

## Technologies

- Python 3.10
- TensorFlow / Keras 2.8.0
- NumPy 1.22.3
- pandas 1.4.2
- scikit-learn 1.1.0
- matplotlib 3.5.1
- ROS 1 Noetic
- Unity Hub 3.12.1
