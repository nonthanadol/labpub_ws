#!/usr/bin/env python3
import rospy
from myfirst_pkg.msg import mymsg
global power
global direction
direction = 'NaN'
power = 0

def callback(data):
    global direction
    global power
    rospy.loginfo((data.name))
    #rospy.logwarn((data.degree))
    direction = data.name
    power = data.degree

def listener():
    global direction
    global power
    rospy.init_node('subro', anonymous=True)
    rospy.Subscriber('dir_robot1', mymsg,callback)
    rate = rospy.Rate(4)
    while True:
      print('robot : {}'.format(direction))
      if(direction=='forward'):
         print('call function forward GO!')
      rate.sleep()
    rospy.spin()
if __name__ == '__main__':
    listener()
