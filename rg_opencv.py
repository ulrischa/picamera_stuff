#!/usr/bin/env python2.7
"""Get R and G bands, average and display as greyscale"""
from __future__ import (absolute_import, division,  # Python3 compatibility
                        print_function)
import time
import picamera
from picamera.array import PiRGBArray
import cv2
import numpy as np

with picamera.PiCamera() as camera:
    width = 800
    height = 480
    camera.resolution = (width,height)
    camera.framerate = 30
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

    with picamera.array.PiRGBArray(camera) as output:
        for foo in  camera.capture_continuous(output, 'bgr', use_video_port=True):
                image = output.array
                output.truncate(0)
                # Do something
                RpG = image[:,:,2].astype(np.int16) + image[:,:,1].astype(np.int16)
                avgd = RpG / 2
                cv2.imshow("window", avgd.astype(np.uint8))
                # Sleep until next frame
                #cv2.waitKey(int(1000/30))
                cv2.waitKey(1)
    cv2.destroyAllWindows()
