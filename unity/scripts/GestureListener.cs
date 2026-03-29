
using UnityEngine; 
using Unity.Robotics.ROSTCPConnector; 
using Unity.Robotics.ROSTCPConnector.MessageGeneration; 
using RosMessageTypes.Std; 
public class GestureListener : MonoBehaviour 
{ 
ROSConnection ros; 
public TrajectoryPlanner planner;  // връзка към скрипта, който изпраща траектория 
void Start() 
{ 
ros = ROSConnection.GetOrCreateInstance(); 
ros.Subscribe<Int32Msg>("/recognized_gesture", OnGestureReceived);
    } 
 
    void OnGestureReceived(Int32Msg msg) 
    { 
        Debug.Log("Gesture received: " + msg.data); 
        if (msg.data == 3) 
        { 
            planner.PublishJoints(); 
 
        } 
    } 
}
