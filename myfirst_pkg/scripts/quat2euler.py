#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from tf2_msgs.msg import TFMessage


def callback(data):
    #rospy.loginfo(data.transforms[0].transform.rotation.z)           
    quaternion_to_euler(data.transforms[0].transform.rotation.w,data.transforms[0].transform.rotation.x,
                        data.transforms[0].transform.rotation.y,data.transforms[0].transform.rotation.z)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/tf", TFMessage, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def quaternion_to_euler(x, y, z, w):

        import math
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))

        rospy.loginfo(X)
        rospy.loginfo(Y)
        rospy.loginfo(Z)

        return X, Y, Z




if __name__ == '__main__':
    listener()
