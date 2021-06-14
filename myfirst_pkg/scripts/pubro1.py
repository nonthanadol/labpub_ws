#!/usr/bin/env python3
import getch
import rospy
from geometry_msgs.msg import Twist 

def talker():
    infoservo = Twist()
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('pub1', anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        key = ord(getch.getch())
        if (key==119):# w
            infoservo.linear.x = 10
            #infoservo.name = "forward"
        elif (key==97):# a
            infoservo.angular.z = 50
            #infoservo.name = "left"
        elif (key==115):# s
            infoservo.linear.x = -10
           #infoservo.name = "backward"
        elif (key==100):# d
            infoservo.angular.z = -20
            #infoservo.name = "right"
        elif (key==99):# c
            infoservo.linear.x = 0
            #infoservo.name = "stop"
        #rospy.loginfo(infoservo.name)
        print(key)
        print('---')
        pub.publish(infoservo)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
