#!/usr/bin/env python3
from std_msgs.msg import Float64
import rospy
import getch

def KEY():
    global pub1 
    global pub2
    global pub3
    global pub4
    global pub5
    global pub6
    rospy.init_node('pubArm', anonymous=True)
    pub1 = rospy.Publisher('/joint1_position/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/joint2_position/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/joint3_position/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/joint4_position/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/joint5_position/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/joint6_position/command', Float64, queue_size=10)


    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        # key = input()
        key = ord(getch.getch())
        if (key == 114 or key == 102):
            joint1(key)
        
        elif(key == 116 or key == 103):
            joint2(key)
        
        elif(key == 121 or key == 104):
            joint3(key)

        elif(key == 121 or key == 104):
            joint4(key)

        elif(key == 121 or key == 104):
            joint5(key)

        elif(key == 121 or key == 104):
            joint6(key)

        elif(key ==115):
            zero()
            
        print(key)    
        rate.sleep()

def joint1(key):
    joint1_pos = Float64()
   
    if(key == 114):
        i=i+0.1
        print("r : joint1 increat angle")
        joint1_pos.data = i 
        pub1.publish(joint1_pos)
    elif(key == 102):
        i=i-0.1
        print("f : joint1 Decreat angle")
        joint1_pos.data = i
        pub1.publish(joint1_pos)

def joint2(key):
    joint2_pos = Float64()
    if(key == 116):
        print("t : joint2 increat angle")
        joint2_pos.data = 0.4
        pub2.publish(joint2_pos)
    elif(key == 103):
        print("g : joint2 Decreat angle")
        joint2_pos.data = -0.4 
        pub2.publish(joint2_pos)

def joint3(key):
    joint3_pos = Float64()
    if(key == 121):
        print("y : joint3 increat angle")
        joint3_pos.data = 0.4
        pub3.publish(joint3_pos)
    elif(key == 104):
        print("h : joint3 Decreat angle")
        joint3_pos.data = -0.4 
        pub3.publish(joint3_pos)










def zero():
    print("Set zero!!!")
    joint1_pos = Float64()
    joint2_pos = Float64()
    joint3_pos = Float64()
    joint4_pos = Float64()
    joint5_pos = Float64()
    joint6_pos = Float64()
    joint1_pos.data = 0
    joint2_pos.data = 0
    joint3_pos.data = 0
    joint4_pos.data = 0
    joint5_pos.data = 0
    joint6_pos.data = 0
    pub1.publish(joint1_pos)
    pub2.publish(joint2_pos)
    pub3.publish(joint3_pos)
    pub4.publish(joint4_pos)
    pub5.publish(joint5_pos)
    pub6.publish(joint6_pos)


# def auto():
#     joint1 = Float64()
#     rospy.init_node('pubArm', anonymous=True)
#     pub = rospy.Publisher('/joint1_position/command', Float64, queue_size=10)
#     rate = rospy.Rate(20)
#     while True:
#         joint1.data = 0.8
#         pub.publish(joint1)
#         rospy.sleep(3)
#         joint1.data =-0.8
#         pub.publish(joint1)
#         rospy.sleep(3)


if __name__ == '__main__':
    try:
         KEY()
        #auto()
    except rospy.ROSInterruptException:
        pass

