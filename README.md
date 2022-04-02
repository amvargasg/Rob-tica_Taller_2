# Rob-tica_Taller_2
Taller 2 de robóticahi
https://uniandes-my.sharepoint.com/:w:/g/personal/jc_ariasc_uniandes_edu_co/EULvgU0VF1BKkjWu-HJvcFsBoSIHR9y0zWnM9Td30Wz7pA?e=fCi29r


Antes de empezar:
Se descarga el archivo y se descomprime. Se asegura de guardar la carpeta descomprimida en el ws

Requerimientos:
Se requiere tener tanto ROS como Copelia SIM instalado para el debido funcionamiento

Pasos:
El primer paso es abrir una terminal, en la cual se debe inicializar ROS con el comando Roscore

En una diferente terminal se abre el workspace cd catkin_ws(el nombre del work space es definido por el usuario utilizando el paquete) y correr el comando source devel/setup.bash el cual carga las dependencias de Ros y del paquete creado

Se deben dirigir a la carpeta contendido los códigos con el comando cd scripts.
Una vez se dan permisos a los archivos .py
- chmod +x malrob.py
- chmod +x leeor.py
- chmod +x escuchador.py


Punto 1 y 3:
Para ejecutar el nodo llamado /turtle_bot_teleop se corre el código malrob.py con el comando rosrun taller2_pkg malrob.py en este inicio se le preguntara al usuario si desea el recorrido y mediante las teclas y n se especificara si desea guardarlo. Si la respuesta es afirmativa se le preguntara el nombre sin incluir el .txt , recuerden cambiar la ruta del archivo para que este mismo quede guardado en la carpeta results, donde quedaran guardados los archivos .txt. Mediante las teclas w a s d el robot se moverá en diferentes direcciones. Cuando ya se quiere terminar de ejecutar o guardar el archivo .txt se debe cerrar forzadamente la terminal utilizando la teclas CTRL+C el archivo txt quedara guardado en la carpeta results

Punto 4:
Para ejecutar este punto se deben correr los scripts leeor.py y escuchador.py, el leeor.pu publica la informaciòn de la ruta almacaneada como texo y el escuchador harà que el robot se mueva como corresponde a las intstrucciones del txt. El comando para correrlos es rosrun taller2_pkg escuhador.py y rosrun taller2_pkg leeor.py Se debe correr el escuchador primero, antes que el leeor para que no se pierda ninguna instrucciòn.

Punto 2:
Para ejecutar el nodo llamado /turtle_bot_interface se corre el código tutrtle_bot_interface.py con el comando rosrun taller2_pkg turtle_bot_interface.py este preguntará el titulo que se le quiere poner a la gráfica. Este nodo se suscribe al \turtlebot_position y grafica en un plot los movimientos. En este plot se tiene un ícono en la parte inferior para guardar, al dar clic ahí permite seleccionar donde se quiere almacenar y con que nombre.
