#!/usr/bin/env python3
from pydoc import text
from vilib import Vilib
from time import sleep, time, strftime, localtime
import readchar


Vilib.camera_start(vflip=False,hflip=False) #
Vilib.display(local=True,web=True)
Vilib.color_detect('green')

while(1):
    n = Vilib.detect_obj_parameter['color_n']
    if n >1:
        print("Go")




# def detect_color(color):
#     detected = False
#     Vilib.color_detect(color)  # red, green, blue, yellow , orange, purple
#     n = Vilib.detect_obj_parameter['color_n']
#     print(n)
#     if n >1:
#         detected = True
#     return detected


# color_list = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# while True:
#     # key = readchar.readkey().lower()
#     # if key == 'q' or  key == readchar.key.CTRL_C:
#     #     Vilib.camera_close()
#     #     break
#     for color in color_list:
#         detected = detect_color(color)
#         if detected:
#             print(f'{color} detected')
#         sleep(0.5)




    
    