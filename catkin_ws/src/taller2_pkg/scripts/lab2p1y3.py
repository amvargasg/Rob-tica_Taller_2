#!/usr/bin/env python3

########## LIBRERÍAS ##########
##Conexion con Arduino
from re import T
import time
import serial
##Manejo y conexión de nodos y tópicos
import keyring
from numpy import True_
import rospy

##Manejo de las acciones del teclado 
from pynput.keyboard import Key, Listener
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Variables globales
current_msg = "neutral"
nombre_archivo=''
ruta=''
texto=''
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# define key press event callback
#Metodo que se encarga las acciones al robot donde se define el movimiento con las teclas w a s d 
def on_press(key):
    global current_msg
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    current_msg = k
    
    if current_msg == "w":
        toArduino('w')

    elif current_msg== "s":
        toArduino('s')
        
    elif current_msg == "d":
        toArduino('d')
        
    elif current_msg == "a":
        toArduino('a')

# define key release event callback
#Metodo que se encarga de las acciones del robot, en donde se si no se presiona tecla se queda quieto
def on_release(key):
    global current_msg
    current_msg = "neutral"

    if current_msg == "neutral":
        toArduino('z')
        
    # stop on PAUSE
    if key == Key.pause:
        print("quit on PAUSE")
        return False
#Metodo que se encarga de guardar las acciones del robot en un archivo txt
# def guaardar():
    
#     global vel_lineal
#     global current_msg
#     global texto
#     global ruta
#     global vel_angular
#     try:
#         if str(guardar)=='y':
                
#             with open(ruta,'a') as file:  
#                 if current_msg == "d":
#                     texto= "right"
#                 elif current_msg== "a":
#                     texto= "left"
#                 elif current_msg== "s":	
#                     texto= "down"
#                 elif current_msg== "w":
#                     texto= "up"
#                 elif current_msg == "neutral":
#                     texto= "neutral"
#                 file.write(texto+ "\n")
                
    # except:
    #     current_msg == "p"
			
def toArduino(key):
    msg = key + '.'
    b_msg = bytes(msg, 'utf-8')
    ser.write(b_msg)
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

# main section
if _name_ == "_main_":
    
    # setup ros publisher
    pub = rospy.Publisher('/turtlebot_cmdVel', Twist, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('turtlebot_teleop', anonymous=True) # name of node: /turtlebot_teleop
    rate = rospy.Rate(10) # publish messages at 10Hz
    mensaje=Twist()
    # setup keyboard listener
    listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
    listener.start()
     
    #Se encarga de definir las velocidades del robot
    vel_lineal=float(input("Ingrese la velocidad lineal:" ))
    vel_angular=float(input("Ingrese la velocidad angular: "))
    #Se encarga de guardar el archivo
    nombre_archivo=''
    guardar= input("Desea guardar la ruta del robot?(y-n) :")
    print (guardar)
    print (type(guardar))
    if str(guardar) == 'y' :
        nombre_archivo= str(input('Escriba un nombre para el archivo: '))
    ruta = '/home/robotica/Robotica_ws/src/taller1_pkg/results/' + (nombre_archivo)+'.txt'


    

    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    while listener.running and not rospy.is_shutdown():
        rospy.loginfo(current_msg)
        pub.publish(mensaje)
        print  (mensaje)
        print(ruta)
        print(current_msg)
        rate.sleep()
        guaardar()