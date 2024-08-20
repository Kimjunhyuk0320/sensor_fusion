#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from yolo import YOLOv8 # YOLOv8 모델을 임포트한다고 가정

class YOLOInference:
    def __init__(self):
        self.image_sub = rospy.Subscriber('/camera/color/image_raw', Image, self.image_callback)
        self.yolo = YOLOv8('path/to/weights.pt')  # YOLOv8 모델 로드

    def image_callback(self, data):
        rospy.loginfo("Running YOLO inference")
        # 이미지를 YOLOv8에 전달하고 결과를 얻음
        results = self.yolo.detect(data)
        # 결과 처리 및 맵 업데이트 로직 추가

if __name__ == '__main__':
    rospy.init_node('yolo_inference', anonymous=True)
    inference = YOLOInference()
    rospy.spin()
