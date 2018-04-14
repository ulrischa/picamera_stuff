#!/usr/bin/env python3
import time
import picamera

with picamera.PiCamera() as camera:
    width = 800
    height = 480
    camera.resolution = (width,height)
    camera.start_preview()
    while True:
        time.sleep(1)

