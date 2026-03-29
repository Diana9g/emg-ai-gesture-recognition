using UnityEngine;
using RosMessageTypes.NiryoMoveit;
using RosMessageTypes.Geometry;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class TrajectorySender : MonoBehaviour
{
    ROSConnection ros;

    // Name of the ROS service used for trajectory planning
    public string serviceName = "mover_service";

    // References to objects in the Unity scene
    public GameObject Target;
    public GameObject TargetPlacement;
    public GameObject NiryoOne;

    // Timing parameters for trajectory execution
    public float jointAssignmentWait = 0.11f;
    public float poseAssignmentWait = 0.5f;

    void Start()
    {
        // Initialize ROS connection and register the service
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterRosService<MoverServiceRequest, MoverServiceResponse>(serviceName);
    }

    public void SendTrajectory()
    {
        var request = new MoverServiceRequest();

        // Initialize joint configuration (placeholder values)
        double[] dummyJoints = new double[6] { 0f, 0f, 0f, 0f, 0f, 0f };
        request.joints_input = new NiryoMoveitJointsMsg();
        request.joints_input.joints = dummyJoints;

        // Define pick pose (grasp position)
        request.pick_pose = new PoseMsg
        {
            position = (Target.transform.position).To<FLU>(),
            orientation = Quaternion.Euler(90, Target.transform.eulerAngles.y, 0).To<FLU>()
        };

        // Define place pose (target placement position)
        request.place_pose = new PoseMsg
        {
            position = (TargetPlacement.transform.position).To<FLU>(),
            orientation = Quaternion.identity.To<FLU>()
        };

        // Send request to ROS service and wait for response
        ros.SendServiceMessage<MoverServiceResponse>(serviceName, request, Callback);
    }

    void Callback(MoverServiceResponse response)
    {
        // Log confirmation when trajectory is received from ROS
        Debug.Log("Robot received trajectory.");
    }
}
