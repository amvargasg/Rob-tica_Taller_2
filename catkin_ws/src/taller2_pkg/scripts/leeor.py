#!/usr/bin/env python3

########## LIBRERÍAS ##########
# Manejo y conexión de nodos y tópicos
from multiprocessing.connection import wait
import keyring
import rospy
import time

# Manejo de las acciones del teclado

from std_msgs.msg import String


# main section
if __name__ == "__main__":
    
    # setup ros publisher
    pub = rospy.Publisher('/turtlebot_cmdVel', String, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('turtlebot_player', anonymous=True) # name of node: /turtlebot_player
    rate = rospy.Rate(1) # publish messages at 10Hz

    #Se encarga de definir las velocidades del robot

    file_name=str(input("Inserte el nombre del archivo: " ))
    ruta = '/home/ubuntu/catkin_ws/src/taller2_pkg/results/' +(file_name)+'.txt'
    
    # MAIN LOOP
    while not rospy.is_shutdown():
        # Se abre el archivo
        f = open(ruta, 'r')
        # Se recorre cada una de las lineas presentes en el archivo y se busca a qué movimiento
        # corresponde para así asignar las velocidades.
        mensaje = ""
        for line in f:
            value = line.strip()
            # Velocidades si el robot debe moverse hacia 'arriba'
            if value == 'up':
                mensaje = "w"
            # Velocidades si el robot debe moverse hacia 'abajo'
            elif value == 'down':
                mensaje = "s"
            # Velocidades si el robot debe moverse hacia la 'izquierda'
            elif value == 'left':
               mensaje = "a"
            # Velocidades si el robot debe moverse hacia la 'izquierda'
            elif value == 'right':
               mensaje = "s"
            # Velocidad si el robot debe permanecer quieto
            elif value == 'neutral':
               mensaje = "n"
            
            
            print(mensaje)
            pub.publish(mensaje)
            # Tiempo adicional para evitar cruce entre ordenes al robot
            time.sleep(0.5)
        # Se cierra el lector de archivos
        f.close()
        # time.sleep(5)
        # quit()
        rate.sleep()