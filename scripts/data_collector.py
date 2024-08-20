#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2, Image

class DataCollector:
    def __init__(self):
        self.lidar_sub = rospy.Subscriber('/velodyne_points', PointCloud2, self.lidar_callback)
        self.image_sub = rospy.Subscriber('/camera/color/image_raw', Image, self.image_callback)

    def lidar_callback(self, data):
        rospy.loginfo("LiDAR data received")
        # LiDAR 데이터 처리 로직 추가

    def image_callback(self, data):
        rospy.loginfo("Camera image received")
        # 카메라 이미지 처리 로직 추가

if __name__ == '__main__':
    rospy.init_node('data_collector', anonymous=True)
    collector = DataCollector()
    rospy.spin()
