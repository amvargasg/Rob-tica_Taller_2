#!/usr/bin/env python3

########## LIBRERÍAS ##########
import time
import serial
from pynput.keyboard import Listener, Key

filename = "key_log.txt"  # The file to write characters to

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()


def on_press(key):
    f = open(filename, 'a')  # Open the file

    if hasattr(key, 'char'):  # Write the character pressed if available
        f.write(key.char)
        msg = key.char + '.'
        b_msg = bytes(msg, 'utf-8')
        ser.write(b_msg)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

    else:  # If anything else was pressed, write [<key_name>]
        print("Press a valid key (f b r l)")

    f.close()  # Close the file


with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread