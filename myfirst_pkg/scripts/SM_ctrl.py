#!/usr/bin/env python
from std_msgs.msg import Float64 , String
import rospy

#msg = String()
class SM_ctrl:
    def __init__(self):
    	rospy.init_node('SM_ctrl')
        rospy.loginfo("Node initialized")
     	self.joint1 = Float64 ()
     	self.pub1 = rospy.Publisher('/joint1_position/command', Float64, queue_size=10)
     	
        # self.pub2 = rospy.Publisher('/joint2_position/command', Float64, queue_size=10)
        # self.pub3 = rospy.Publisher('/joint3_position/command', Float64, queue_size=10)
        # self.pub4 = rospy.Publisher('/joint4_position/command', Float64, queue_size=10)
        # self.pub5 = rospy.Publisher('/joint5_position/command', Float64, queue_size=10)
        # self.pub6 = rospy.Publisher('/joint6_position/command', Float64, queue_size=10)
        

    def listener(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            rospy.Subscriber('SM', String, self.ctrl)
            rate.sleep()           


    def ctrl(self , msg ):
    	rospy.loginfo(msg.data)
    	if(msg.data == 'r'):
            print("GO")
            self.joint1.data = 0.3 
            self.pub1.publish(self.joint1.data)
        elif(msg.data == 'f'):
            self.joint1.data = -0.3 
            self.pub1.publish(self.joint1.data)
        else:pass
    		
    

if __name__=="__main__":
    robot = SM_ctrl()
    while not rospy.is_shutdown():
        robot.listener()