using UnityEngine;
using RosMessageTypes.NiryoMoveit;
using RosMessageTypes.Geometry;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class TrajectorySender : MonoBehaviour
{
    ROSConnection ros;
    public string serviceName = "mover_service";

    public GameObject Target;
    public GameObject TargetPlacement;
    public GameObject NiryoOne;

    public float jointAssignmentWait = 0.11f;
    public float poseAssignmentWait = 0.5f;

    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterRosService<MoverServiceRequest, MoverServiceResponse>(serviceName);
    }

    public void SendTrajectory()
    {
        var request = new MoverServiceRequest();

        // Вземане на текущи стави
        double[] dummyJoints = new double[6] { 0f, 0f, 0f, 0f, 0f, 0f };
        request.joints_input = new NiryoMoveitJointsMsg();
        request.joints_input.joints = dummyJoints;


        // Поза за хващане (pick)
        request.pick_pose = new PoseMsg
        {
            position = (Target.transform.position).To<FLU>(),
            orientation = Quaternion.Euler(90, Target.transform.eulerAngles.y, 0).To<FLU>()
        };

        // Поза за поставяне (place)
        request.place_pose = new PoseMsg
        {
            position = (TargetPlacement.transform.position).To<FLU>(),
            orientation = Quaternion.identity.To<FLU>()
        };

        ros.SendServiceMessage<MoverServiceResponse>(serviceName, request, Callback);
    }

    void Callback(MoverServiceResponse response)
    {
        Debug.Log(" Robot received trajectory.");
    }
}

