#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def Begin():
    rospy.init_node('turtle_cmg', anonymous=True)
    rospy.loginfo("Start!!! GoGoGo!!!")
    global i 
    global z 
    i = True
    z = False
    
    global pub
    global rate
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    rospy.Timer(rospy.Duration(5), stop,oneshot=True)
    while  True:
      if i == True and z == False :
        Velocity = Twist()
        Velocity.linear.x = 0.15
        print("forward {}".format(Velocity.linear.x))
        pub.publish(Velocity)
        rate.sleep()
      


def  stop(even):
    rospy.loginfo("Stop !!!")
    global i 
    global z 
    i = False
    z = False
    rospy.Timer(rospy.Duration(1),rotation,oneshot=True)
    while  True :
      if i == False and z == False :
        Velocity = Twist()
        Velocity.linear.x = 0
        Velocity.angular.z = 0
        print("stop {}".format(Velocity.linear.x))
        pub.publish(Velocity)
        rate.sleep()
      
    

def rotation(even):
    rospy.loginfo("Rotate !!!")
    global i 
    global z 
    i = False
    z = True
    rospy.Timer(rospy.Duration(3),forward,oneshot=True)
    while  True:
      if z == True and i == False:
        Velocity = Twist()
        Velocity.angular.z = 0.15
        print("rotate {} ",Velocity.angular.z)
        pub.publish(Velocity)
        rate.sleep()
      

def forward(even):
    rospy.loginfo("Forward !!!")
    global i 
    global z 
    i = True
    z = False
    rospy.Timer(rospy.Duration(5), stop,oneshot=True)
    while  True:
      if i == True and z == False :
        Velocity = Twist()
        Velocity.angular.z = 0
        Velocity.linear.x = 0.15
        print("forward {}".format(Velocity.linear.x))
        pub.publish(Velocity)
        rate.sleep()
      




if __name__ == '__main__':
    Begin()
