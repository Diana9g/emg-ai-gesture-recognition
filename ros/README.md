# ROS Integration

This project uses ROS 1 Noetic as a communication layer between the AI system and the Unity-based simulation of the Niryo One robot.

## Functionality

- Receives gesture predictions from the AI model
- Publishes recognized gestures to a ROS topic
- Enables communication between Python (machine learning) and Unity (simulation)
- Triggers robotic actions based on recognized gestures

## Main ROS Topic

- `/recognized_gesture` (std_msgs/Int32)

This topic is used to send predicted gestures from the AI system to the Unity environment.

## External ROS Packages Used

- `ros_tcp_endpoint` – communication between Unity and ROS  
- `niryo_one_ros` / `ned_ros` – robot simulation and control  
- `MoveIt` – trajectory planning  

## Notes

These ROS packages are external dependencies and are not included in this repository.  
This repository focuses on the AI pipeline, data processing, and system integration.
