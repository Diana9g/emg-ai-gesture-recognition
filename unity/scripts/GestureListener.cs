using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;
using RosMessageTypes.Std;

public class GestureListener : MonoBehaviour
{
    ROSConnection ros;

    // Reference to the script responsible for generating and sending robot trajectories
    public TrajectoryPlanner planner;

    void Start()
    {
        // Initialize ROS connection
        ros = ROSConnection.GetOrCreateInstance();

        // Subscribe to the gesture topic published by the AI system
        ros.Subscribe<Int32Msg>("/recognized_gesture", OnGestureReceived);
    }

    void OnGestureReceived(Int32Msg msg)
    {
        // Log received gesture value for debugging
        Debug.Log("Gesture received: " + msg.data);

        // If gesture equals 3, trigger robot movement
        if (msg.data == 3)
        {
            planner.PublishJoints();
        }
    }
}
