#!/usr/bin/env python3
from pydoc import text
from vilib import Vilib
from time import sleep, time, strftime, localtime
import threading
import readchar
import os


Vilib.camera_start(vflip=False,hflip=False)
Vilib.display(local=True,web=True)
Vilib.qrcode_detect_switch(True)

def qrcode_detect():
    while True:
        text = Vilib.detect_obj_parameter['qr_data']
        print(text)
        sleep(0.5)


qrcode_detect()