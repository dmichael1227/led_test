#!/usr/bin/env python3
# Based on the simple publisher/subscriber tutorial on the ROS tutorial page:
# https://github/ros/ros_tutorials.com
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.

import rospy
import time
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('ledstuff', Bool, queue_size=10) #publish to ledstuff topic
    rospy.init_node('talker', anonymous=True) #initiate talker node
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        command_input = float(input("LED COMMAND: ")) #query for command and convert to float
        led_command = bool(command_input) #convert to boolean
        print("led_command is : %s" % led_command) 
        rospy.loginfo(led_command) #log the entered command
        pub.publish(led_command) #publish command to ledstuff topic
        rate.sleep() #sleep (10ms)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
