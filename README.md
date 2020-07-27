Please refer to the README.pdf document found here:https://github.com/amichael1227/ros_led_test/blob/master/README.pdf



This is a ROS Package for testing an LED & BME 280 sensor. This was done with a Raspberry Pi Running Ubuntu and ROS. Currently this is only confirmed to support ROS Noetic and Ubuntu 20.04


# NOTE: 
To get this ROS package to work properly, you must first run the command __*catkin_create_pkg led_test std_msgs rospy roscpp*__ from the __*~/catkin_ws*__ directory created in the beginner tutorials. From there, you should clone the GitHub repository into a different folder, and then copy the contents of that folder in the __*~/catkin_ws/src/led_test folder*__. Finally, change the directory back to __*~/catkin_ws*__ and run the __*catkin_make*__ command to build the package.
