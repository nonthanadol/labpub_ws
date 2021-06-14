#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

g_twist = Twist()

def cb_odom(msg_odom):
	t_pose_x = msg_odom.pose.pose.position.x
	t_pose_y = msg_odom.pose.pose.position.y
	rospy.loginfo('current postion (x,y) = ({:.4f}, {:.4f})'.format(t_pose_x, t_pose_y))

rospy.init_node('nd_move_circle')
pub_twist = rospy.Publisher('cmd_vel', Twist, queue_size=1)
sub_odom = rospy.Subscriber('odom', Odometry, cb_odom)
rate = rospy.Rate(20)

while not rospy.is_shutdown():
	g_twist.linear.x = 0.5
	g_twist.angular.z = 0.6
	pub_twist.publish(g_twist)
	rate.sleep()
