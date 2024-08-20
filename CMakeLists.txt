cmake_minimum_required(VERSION 3.0.2)
project(lidar_camera_mapping)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  pcl_ros
  cv_bridge
  image_transport
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(map_visualizer src/map_visualizer.cpp)
target_link_libraries(map_visualizer ${catkin_LIBRARIES})
