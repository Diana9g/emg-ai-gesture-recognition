# EMG Gesture Recognition for Robotic Control

This project presents an end-to-end system for controlling a robotic arm using electromyography (EMG) signals and artificial intelligence.

The system processes EMG data, classifies hand gestures using a deep learning model, and integrates the results into a robotic simulation environment using ROS and Unity.

---

## Project Overview

The project implements a complete AI pipeline for real-time gesture recognition and robotic control:

1. EMG signal acquisition  
2. Signal preprocessing and normalization  
3. Feature extraction (RMS, MAV, etc.)  
4. LSTM-based gesture classification  
5. Real-time prediction using Python  
6. Communication with ROS nodes  
7. Execution of actions in Unity simulation (Niryo One robot)

---

## Technologies Used

- **Unity Hub 3.12.1** – Simulation of the Niryo One robot and visualization of movements  
- **ROS 1 Noetic** – Communication between nodes and EMG-based control  
- **Python 3.10** – EMG signal processing, model training, and integration  
- **TensorFlow / Keras 2.8.0** – LSTM model for gesture classification  
- **NumPy 1.22.3** – Numerical computations and array handling  
- **pandas 1.4.2** – Data handling and dataset processing  
- **scikit-learn 1.1.0** – Data splitting and evaluation  
- **matplotlib 3.5.1** – Visualization of training results  

---

## System Architecture

The system connects machine learning with robotic simulation through ROS:

- Python processes EMG signals and performs classification  
- The trained model predicts gestures in real time  
- Predictions are published via ROS (`/recognized_gesture`)  
- Unity subscribes to the topic and triggers robot actions  
- The Niryo One robot executes movements (e.g. pick-and-place)

---

## Key Features

- Real-time EMG signal processing  
- Deep learning-based gesture recognition (LSTM)  
- ROS-based communication between components  
- Unity robotic simulation  
- End-to-end pipeline from biosignal to robot action  

---

## Repository Structure

- `src/` – Python scripts for training and inference  
- `data/` – EMG dataset (sample or structured)  
- `models/` – trained models (`.h5`, `.keras`)  
- `ros/` – ROS integration documentation  
- `unity/` – Unity simulation scripts  
- `docs/` – additional project documentation  

---

## Notes

- Some datasets may not be fully included due to size limitations  
- External ROS packages (MoveIt, Niryo) are required for full functionality  

---

## License

This project is licensed under the MIT License.
