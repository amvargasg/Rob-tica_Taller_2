#!/usr/bin/env python3

########## LIBRERÍAS ##########
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
# define key press event callback
#Metodo que se encarga las acciones al robot donde se define el movimiento con las teclas w a s d 
def on_press(key):
    global current_msg
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    current_msg = k
    

    
# define key release event callback
#Metodo que se encarga de las acciones del robot, en donde se si no se presiona tecla se queda quieto
def on_release(key):
    global current_msg
    current_msg = "n"
    # stop on PAUSE
    if key == Key.pause:
        print("quit on PAUSE")
        return False
#Metodo que se encarga de guardar las acciones del robot en un archivo txt

def guaardar():
    
    global vel_lineal
    global current_msg
    global texto
    global ruta
    global vel_angular
    try:
        if str(guardar)=='y':
                
               
                    with open(ruta,'a') as file:
                
                        if current_msg == "d":
                            texto= "right"
                        elif current_msg== "a":
                            texto= "left"
                        elif current_msg== "s":	
                            texto= "down"
                        elif current_msg== "w":
                            texto= "up"
                        elif current_msg == "n":
                            texto= "n"
                        file.write(texto+ "\n")
    except:
        current_msg == "p"

# main section
if __name__ == "__main__":
    
    # setup ros publisher
    pub = rospy.Publisher('/turtlebot_cmdVel', String, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('turtlebot_teleop', anonymous=True) # name of node: /turtlebot_teleop
    rate = rospy.Rate(3) # publish messages at 10Hz
    mensaje=Twist()
    # setup keyboard listener
    listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
    listener.start()
   
    #Se encarga de guardar el archivo
    nombre_archivo=''
    guardar= input("Desea guardar la ruta del robot?(y-n) :")
    print (guardar)
    print (type(guardar))
    if str(guardar) == 'y' :
        nombre_archivo= str(input('Escriba un nombre para el archivo: '))
    ruta = '/home/ubuntu/catkin_ws/src/taller2_pkg/results/' + (nombre_archivo)+'.txt'

    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    while listener.running and not rospy.is_shutdown():
        rospy.loginfo(current_msg)
        pub.publish(current_msg)
        print  (current_msg)
        rate.sleep()
        
        guaardar()
        
