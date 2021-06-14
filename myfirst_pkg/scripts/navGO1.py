#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped

global X
global Y
global W
X = float(input("input x = "))
Y = float(input("input y = "))
W = float(input("input w = "))
pose = PoseStamped()
pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
rospy.init_node('navGO', anonymous=True)
pose.header.frame_id = "map"
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pose.pose.position.x = X
    pose.pose.position.y = Y
    pose.pose.orientation.w = W
    pub.publish(pose)
    rate.sleep()
