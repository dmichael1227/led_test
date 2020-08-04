#!/usr/bin/env python3
# Based on the simple publisher/subscriber tutorial on the ROS tutorial page:
# https://github/ros/ros_tutorials.com
# Software License Agreement (GPLv3 License)

import rospy
import os
from subprocess import Popen, PIPE
from led_test.msg import BME
from gps_stuff.msg import GPS


package_path = os.environ['ROS_PACKAGE_PATH'] #read the ROS_PACKAGE_PATH environment variable to get an idea 
src_path, dummy = package_path.split(':')
def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.temp)
    temp_c = data.temp # read temp
    temp_f = data.temp*9.0/5.0+32.0 # convert to fahrenheit
    rospy.loginfo('T: %s P: %s H: %s ',temp_f,data.pressure,data.humidity) # display temperature, pressure, and humidity
def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + 'Lat: %s Lon %s', # display latitude and longitude
                  round(data.Lat,4),round(data.Lon,4))
    
first_flag=True
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True) #initiate this node

    rospy.Subscriber('bme280', BME, callback1) #subscribe to bme280 topic
    rospy.Subscriber('gps', GPS, callback2) # subscribe to gps topic
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    # Popen(['sudo','python3','/home/ubuntu/catkin_ws/src/led_test/python_scripts/blink_test.py'], stdout=PIPE, stderr=PIPE) 
    Popen(['sudo','python3',src_path+'/led_test/scripts/blink_test.py'],stdout=PIPE,stderr=PIPE) # can comment this out if you like- this script just blinks pin 8 (NOT GPIO8) 3 times
    listener()
