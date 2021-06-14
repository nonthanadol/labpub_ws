#!/usr/bin/env python3

import rospy
import time
def forward_callback(event):
    global rotate
    global forward
    global i
    i = i+1
    if i % 2 == 1:
        forward = False
        rotate = True
    else:
        forward = True
        rotate = False

# def rotate_callback(event):
#   global rotate
#   global forward
#     forward = True
#     rotate = False


if __name__ == '__main__':
    global stop
    global i
    # stop = False
    rotate = False
    forward = True
    i = 0
    rospy.init_node('turtle_cmg', anonymous=True)
    #time.sleep(1)
    rate = rospy.Rate(10)
    print("start")
    rospy.Timer(rospy.Duration(2), forward_callback, oneshot=False)
    while True:
        # forward
        if forward == True:
            print("forward")
            
        # rotoe
        if (rotate == True):
            print("rotate")


        rate.sleep()
