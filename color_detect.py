#!/usr/bin/env python3
from pydoc import text
from vilib import Vilib
from time import sleep, time, strftime, localtime


Vilib.camera_start(vflip=False,hflip=False) #
Vilib.display(local=True,web=True)




def detect_color(color):
    detected = Vilib.color_detect(color)  # red, green, blue, yellow , orange, purple
    return detected


color_list = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

while True:
    for color in color_list:
        detected = detect_color(color)
        if detected:
            print(f'{color} detected')
        else:
            print(f'{color} not detected')
        sleep(1)
    
    