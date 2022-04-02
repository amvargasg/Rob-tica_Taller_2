#!/usr/bin/env python3
from numpy import rate
import rospy
from std_msgs.msg import String
import serial

# Variables globales
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.reset_input_buffer()


def callback(data):
    msg = data.data
    if msg == "w":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif msg == "s":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif msg == "d":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif msg == "a":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)

    elif msg == "n":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('/turtlebot_cmdVel',String,callback,queue_size=10,buff_size=2**28)
    rospy.spin()

if __name__=='__main__':
   
    while not rospy.is_shutdown():
        listener()
        
