#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "map_visualizer");
    ros::NodeHandle nh;

    ros::Publisher marker_pub = nh.advertise<visualization_msgs::Marker>("visualization_marker", 1);

    visualization_msgs::Marker marker;
    marker.header.frame_id = "/map";
    marker.header.stamp = ros::Time::now();
    marker.ns = "basic_shapes";
    marker.id = 0;
    marker.type = visualization_msgs::Marker::CUBE;
    marker.action = visualization_msgs::Marker::ADD;
    marker.pose.position.x = 0;
    marker.pose.position.y = 0;
    marker.pose.position.z = 0;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;
    marker.scale.x = 1.0;
    marker.scale.y = 1.0;
    marker.scale.z = 1.0;
    marker.color.r = 0.0f;
    marker.color.g = 1.0f;
    marker.color.b = 0.0f;
    marker.color.a = 1.0;
    marker.lifetime = ros::Duration();

    while (ros::ok()) {
        marker_pub.publish(marker);
        ros::spinOnce();
    }
    return 0;
}
