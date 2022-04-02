#!/usr/bin/env python3

########## LIBRERÍAS ##########
##Manejo y conexión de nodos y tópicos
import rospy
from geometry_msgs.msg import Twist
##Para graficar
import numpy as np
import matplotlib.pyplot as plt

current_msg=''

def handle_close(evt):
    global closed
    closed = True
    
def graficar(x,y, titulo_g):
    plt.axis(0,3,0,3)
    plt.scatter(x, y, color='r')
    if len(x) >= 2 :
        plt.plot(x, y, color='b')  
    else:
        pass
    plt.title(titulo_g)
    plt.show()
    fig.canvas.flush_events()
    
#Funcion que se encarga de transformar el mensaje en coordenadas y agregarlas a las listas que se grafican    
def callback(data):
    x.append(data.linear.x)
    y.append(data.linear.y)
    
# main section
if __name__ == "_main_":
   
    # setup ros suscriber
    pub = rospy.Suscriber('/turtlebot_position', Twist, callback) # name of topic: /turtlebot_position
    rospy.init_node('turtle_bot_interface', anonymous=True) # name of node: /turtlebot_position
    rate = rospy.Rate(10) # publish messages at 10Hz
    mensaje=Twist()
    #Se encarga de escoger el nombre de la grafica
    titulo=str(input('Escriba un nombre para la grafica: '))


    x = [0] # Las coordenadas de los dos puntos a conectar
    y = [0]
    
    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    while not rospy.is_shutdown():
        fig = plt.figure()
        closed = False
        fig.canvas.mpl_connect('close_event', handle_close)
        r = np.linspace(0,20,101)
        plt.ion()
        rospy.loginfo(current_msg)
        rospy.spin()