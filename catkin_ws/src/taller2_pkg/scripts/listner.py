#!/usr/bin/env python3

########## LIBRERÍAS ##########
##Manejo y conexión de nodos y tópicos
import rospy
from std_msgs.msg import String


import serial

# Variables globales
current_msg = "neutral."
nombre_archivo=''
ruta=''
texto=''
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()
# define key press event callback
#Metodo que se encarga las acciones al robot donde se define el movimiento con las teclas w a s d 

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    # setup roslistener
    print('entra a listener')
    pub = rospy.Suscriber('/turtlebot_cmdVel', String, callback, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('listener', anonymous=True) # name of node: listener

def arduino(data):
    

    if data == "w.":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif data == "s":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif data == "d":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)
		
    elif data == "a":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)

    elif data == "neutral":
        msgg = msg + '.'
        b_msg = bytes(msgg, 'utf-8')
        ser.write(b_msg)


if __name__ == "_main_":
    print('entra name')
    listener()
