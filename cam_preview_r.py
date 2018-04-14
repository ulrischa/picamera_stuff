#!/usr/bin/env python3
"""GPU based preview, only red channel enabled"""
import time
import picamera

with picamera.PiCamera() as camera:
    width = 800
    height = 480
    camera.resolution = (width,height)
    camera.image_effect = 'colorbalance'
    camera.image_effect_params = (0.0, 1.0,0.0,0)
    camera.start_preview()
    while True:
        time.sleep(1)

