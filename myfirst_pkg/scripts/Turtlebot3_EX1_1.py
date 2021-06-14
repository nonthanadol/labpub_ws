#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def Begin():
    rospy.init_node('turtle_cmg', anonymous=True)
    rospy.loginfo("Start!!! GoGoGo!!!")
    global i
    global z
    i = True
    z = False

    Velocity = Twist()

    global pub
    global rate
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    rospy.Timer(rospy.Duration(5), stop, oneshot=True)
    while not rospy.is_shutdown():
        ## linear velocity
        if (i == True):
            Velocity.linear.x = 0.15
        else:
            Velocity.linear.x = 0.0

        ## angular velocity
        if (z == True):
            Velocity.angular.z = 0.15
        else:
            Velocity.angular.z = 0.0

        pub.publish(Velocity)
        rate.sleep()


def stop(even):
    rospy.loginfo("Stop !!!")
    global i
    global z
    i = False
    z = False
    rospy.Timer(rospy.Duration(1),rotation, oneshot=True)

def rotation(even):
    rospy.loginfo("Rotate !!!")
    global i
    global z
    i = False
    z = True
    rospy.Timer(rospy.Duration(3),forward, oneshot=True)

def forward(even):
    rospy.loginfo("Forward !!!")
    global i
    global z
    i = True
    z = False
    rospy.Timer(rospy.Duration(5), stop, oneshot=True)

if __name__ == '__main__':
    Begin()
