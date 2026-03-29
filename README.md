# emg-ai-gesture-recognition
EMG-based gesture recognition project using Python, TensorFlow, ROS, and Unity for real-time AI-driven control.

## Technologies Used

- **Unity Hub 3.12.1** – Simulation of the Niryo One robot and visualization of movements  
- **ROS 1 Noetic** – Communication between nodes and implementation of EMG-based control node  
- **Python 3.10** – Main language for EMG signal processing, model training, and ROS integration  
- **TensorFlow / Keras 2.8.0** – Training and inference of LSTM model for EMG classification  
- **NumPy 1.22.3** – Numerical operations and array processing  
- **pandas 1.4.2** – Handling CSV datasets and tabular data  
- **scikit-learn 1.1.0** – Train/test split and evaluation metrics  
- **matplotlib 3.5.1** – Visualization of training results (accuracy, loss)

## System Architecture

The project follows a complete AI pipeline:

1. EMG signal acquisition  
2. Signal preprocessing and normalization  
3. Feature extraction (RMS, MAV, etc.)  
4. LSTM-based gesture classification  
5. Real-time prediction using Python  
6. Communication with ROS nodes  
7. Execution of actions in Unity simulation (Niryo One robot)

## Key Features

- Real-time EMG signal processing  
- LSTM-based gesture recognition  
- Integration with ROS for robotic control  
- Unity simulation of Niryo One robot  
- End-to-end pipeline from signal to action

  ## Repository Structure

- `src/` – training and ML scripts
- `data/` – sample EMG dataset
- `models/` – trained model notes or files
- `ros/` – ROS integration notes
- `unity/` – Unity simulation scripts
- `docs/` – project overview and technical documentation
