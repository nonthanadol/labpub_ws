#!/usr/bin/env python3
import getch
import rospy
from myfirst_pkg.msg import mymsg

def talker():
    infoservo = mymsg()
    pub = rospy.Publisher('dir_robot1', mymsg, queue_size=10)
    rospy.init_node('pubro', anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        key = ord(getch.getch())
        if (key==119):# w
            infoservo.degree = 10
            infoservo.name = "forward"
        elif (key==97):# a
            infoservo.degree = 20
            infoservo.name = "left"
        elif (key==115):# s
            infoservo.degree = -10
            infoservo.name = "backward"
        elif (key==100):# d
            infoservo.degree = -20
            infoservo.name = "right"
        elif (key==99):# c
            infoservo.degree = 0
            infoservo.name = "stop"
        rospy.loginfo(infoservo.name)
        print(key)
        print('---')
        pub.publish(infoservo)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
