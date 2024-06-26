#!/usr/bin/env python3
from pydoc import text
from vilib import Vilib
from time import sleep, time, strftime, localtime
import readchar
from picarx import Picarx


Vilib.camera_start(vflip=False,hflip=False) #
Vilib.display(local=True,web=True)
Vilib.color_detect('green')
Vilib.qrcode_detect_switch(True)

px = Picarx()

def left_turn():
    px.set_dir_servo_angle(-30)
    px.forward(10)
    sleep(1)
    px.set_dir_servo_angle(0) 
    px.stop()



def right_turn():
    px.set_dir_servo_angle(30)
    px.forward(10)
    sleep(1)
    px.set_dir_servo_angle(0) 
    px.stop()



while(1):
    n = Vilib.detect_obj_parameter['color_n']
    text = Vilib.detect_obj_parameter['qr_data']
    if n >1:
        print("Moving")
        px.forward(10)
        px.set_cam_tilt_angle(0)
        px.set_cam_pan_angle(0)  
        px.set_dir_servo_angle(0) 
        pan_angle = 0
        tilt_angle = 0
        if text == "right":
            print("Turning right")
            right_turn()
        elif text == "left":
            print("Turning Left")
            left_turn()
                  
        sleep(0.5)
    else:
        px.set_cam_tilt_angle(0)
        px.set_cam_pan_angle(0)  
        px.set_dir_servo_angle(0)  
        px.stop()



#     try:
#         pan_angle = 0
#         tilt_angle = 0
#         if text == "right":
#             print("Turning right")
#             px.set_dir_servo_angle(30)
#         elif text == "Left":
#             print("Turning Left")
#             px.set_dir_servo_angle(-30)

#         px.set_cam_tilt_angle(tilt_angle)
#         px.set_cam_pan_angle(pan_angle)                    
#         sleep(0.5)
#     finally:
#         px.forward(5)


# px.set_cam_tilt_angle(0)
# px.set_cam_pan_angle(0)  
# px.set_dir_servo_angle(0)  
# px.stop()
# sleep(.2)