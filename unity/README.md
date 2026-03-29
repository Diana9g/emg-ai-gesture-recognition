# Unity Integration

This folder contains the Unity-side scripts used for simulating the Niryo One robot and visualizing gesture-driven robotic actions.

Main components:
- `GestureListener.cs` – subscribes to `/recognized_gesture` and triggers robot actions
- `TargetPlacement.cs` – manages target cube placement logic
- `TrajectoryPlanner.cs` – generates robot trajectories based on gesture input and target position
- `TrajectorySender.cs` – sends trajectory requests to the simulated robot

Environment:
- Unity Hub 3.12.1
