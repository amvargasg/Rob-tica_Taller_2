#!/usr/bin/env python3
from numpy import rate
import rospy
from std_msgs.msg import String


def callback(data):
    msg = data.data
    if msg == "w":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        print(b_msg)
		
    elif msg == "s":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        print(b_msg)
		
    elif msg == "d":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        print(b_msg)

    elif msg == "a":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        print(b_msg)

    elif msg == "n":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        print(b_msg)

    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('/turtlebot_cmdVel',String,callback,queue_size=10,buff_size=2**28)
    rospy.spin()

if __name__=='__main__':
   
    while not rospy.is_shutdown():
        listener()
        
