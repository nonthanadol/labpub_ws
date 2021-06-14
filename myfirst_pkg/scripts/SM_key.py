#!/usr/bin/env python
from std_msgs.msg import String
import rospy
import sys, select, os

if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

def KEY():
    if os.name == 'nt':
      if sys.version_info[0] >= 3:
        return msvcrt.getch().decode()
      else:
        return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key








if __name__=="__main__":
    
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('SM_key')
    pub = rospy.Publisher('SM', String , queue_size=10)
    key_joint = String()
    while(1):
        key = KEY()
        if key == 'r' :
            print("r")
            key_joint = 'r'
            pub.publish(key_joint)
        elif key == 'f' :
            print('f')
            key_joint = 'f'
            pub.publish(key_joint)
        else:pass
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)