#!/usr/bin/env python3

########## LIBRERÍAS ##########
##Manejo y conexión de nodos y tópicos
import keyring
# from numpy import True_
import rospy

##Manejo de las acciones del teclado 
from pynput.keyboard import Key, Listener
from std_msgs.msg import String
from geometry_msgs.msg import Twist

##Manejo de conexion serial con arduino
import serial

# Variables globales
current_msg = "z"
nombre_archivo=''
ruta=''
texto=''

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
        msgg = current_msg + '.'
		
    elif current_msg== "s":
        msgg = current_msg + '.'
		
    elif current_msg == "d":
        msgg = current_msg + '.'
		
    elif current_msg == "a":
        msgg = current_msg + '.'
		
	

   
            
    
# define key release event callback
#Metodo que se encarga de las acciones del robot, en donde se si no se presiona tecla se queda quieto
def on_release(key):
    global current_msg
    global msgg
    current_msg = "z"

    if current_msg == "z":
        msgg = current_msg + '.'
		# b_msg = bytes(msg, 'utf-8')
		# ser.write(b_msg)
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
                
#                 # file = open(ruta,'w')
#                 # file.write(str(vel_lineal)+'\n')
#                 # file.write(str(vel_angular)+'\n')
#                 # file.close
#                 # # with open(ruta,'w') as file:
#                 # #     file.write(str(vel_lineal)+'\n')
#                 # #     file.write(str(vel_angular)+'\n')
#                 # if file.close == True:
#                     with open(ruta,'a') as file:
                
#                         if current_msg == "d":
#                             texto= "right"
#                         elif current_msg== "a":
#                             texto= "left"
#                         elif current_msg== "s":	
#                             texto= "down"
#                         elif current_msg== "w":
#                             texto= "up"
#                         elif current_msg == "z":
#                             texto= "neutral"
#                         file.write(texto+ "\n")
#     except:
#         current_msg == "p"
			
# def mensaje():
# 	if (current_msg=='w,a,s,d'):  # Write the character pressed if available
# 		msg = current_msg + '.'
# 		b_msg = bytes(msg, 'utf-8')
# 		ser.write(b_msg)
# 		line = ser.readline().decode('utf-8').rstrip()
# 		print(line)
# 		time.sleep(1)

# 	    else:  # If anything else was pressed, write [<key_name>]
# 		print("Press a valid key (f b r l)")

# main section
if __name__ == "_main_":
    print("entra aqui")
    # setup ros publisher
    #pub = rospy.Publisher('/turtlebot_cmdVel', Twist, queue_size=10) # name of topic: /ctrl_cmd
    pub = rospy.Publisher('/turtlebot_cmdVel', String, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('turtlebot_teleop', anonymous=True) # name of node: /turtlebot_teleop
    rate = rospy.Rate(10) # publish messages at 10Hz
    mensaje=Twist()
    # setup keyboard listener
    listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
    listener.start()
    #Se encarga de definir las velocidades del robot
    # vel_lineal=float(input("Ingrese la velocidad lineal:" ))
    # vel_angular=float(input("Ingrese la velocidad angular: "))
    # #Se encarga de guardar el archivo
    # nombre_archivo=''
    # guardar= input("Desea guardar la ruta del robot?(y-n) :")
    # print (guardar)
    # print (type(guardar))
    # if str(guardar) == 'y' :
    #     nombre_archivo= str(input('Escriba un nombre para el archivo: '))
    # ruta = '/home/robotica/Robotica_ws/src/taller1_pkg/results/' + (nombre_archivo)+'.txt'


    

    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    print("llega")
    while listener.running and not rospy.is_shutdown():
        print("LLEGA")
        rospy.loginfo(current_msg)
        pub.publish(msgg)
        print(msgg)
        #pub.publish(mensaje)
        #print  (mensaje)
        #print(ruta)
        #print(current_msg)
        rate.sleep()
        # guaardar()
