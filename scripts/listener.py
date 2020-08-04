#!/usr/bin/env python3
# Based on the simple publisher/subscriber tutorial on the ROS tutorial page:
# https://github/ros/ros_tutorials.com
# Software License Agreement (GPLv3 License)

import rospy
import os
from subprocess import Popen, PIPE
from std_msgs.msg import String

package_path = os.environ['ROS_PACKAGE_PATH'] #read the ROS_PACKAGE_PATH environment variable to get an idea where your/src/ directory is for your catkin workspace
src_path,dummy = package_path.split(':') #grab the first entry. this should be the catkin_ws/src file where all your ros packages live. If not, change this line so that it references the directory where your led_test package lives

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

first_flag=True
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback) #subscribe to chatter topic

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    # Popen(['sudo','python3','/home/ubuntu/catkin_ws/src/led_test/python_scripts/blink_test.py'], stdout=PIPE, stderr=PIPE) 
    Popen(['sudo','python3',src_path+'led_test/scripts/blink_test.py'],stdout=PIPE,stderr=PIPE)
    listener()

