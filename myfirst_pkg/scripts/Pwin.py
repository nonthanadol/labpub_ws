#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
real_pose =Odometry()

def callback(data):
    rospy.loginfo(data.pose.pose.position.x)
    real_pose.pose.pose.position.x = data.pose.pose.position.x
def listener():
    real_pose1 =Odometry()
    real_pose1.pose.pose.position.x = real_pose.pose.pose.position.x
    rospy.init_node('turtle_cmg', anonymous=True)
    rospy.Subscriber('odom', Odometry, callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    

    while not rospy.is_shutdown():
        while  real_pose.pose.pose.position.x <= 3:
                  print("forward : {}".format(real_pose.pose.pose.position.x))
                  Velocity = Twist()
                  Velocity.linear.x = 1
                  pub.publish(Velocity)
                  
        while  real_pose.pose.pose.position.x >= 0:
                  print("backward : {} ".format(real_pose.pose.pose.position.x))
                  Velocity = Twist()
                  Velocity.linear.x = -1
                  pub.publish(Velocity)

    rate.sleep()   

if __name__ == '__main__':
    listener()
