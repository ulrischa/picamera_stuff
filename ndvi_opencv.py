from __future__ import (absolute_import, division, print_function)
import sys
import time
import picamera
import picamera.array
import numpy as np
import cv2
import datetime
import requests
from subprocess import check_output

URL_TO_SEND_IMAGE = ""

# Check for Wi-Fi connection
def check_wifi():
    if check_output(['hostname', '-I']):
        return True
    else:
        return False

with picamera.PiCamera() as camera:
    width = 640
    height = 480
    camera.resolution = (width,height)

    with picamera.array.PiRGBArray(camera) as stream:
        camera.start_preview()
        time.sleep(2)
        for foo in  camera.capture_continuous(stream, 'bgr'):
            image = stream.array
            stream.truncate(0)
            RmB = image[:,:,2] - image[:,:,0]
            RpB = image[:,:,2].astype(np.int16) + image[:,:,0].astype(np.int16)
            counter = RmB.astype(np.float32)
            denominator = RpB.astype(np.float32)
            if np.any(denominator): 
                dvir = counter / denominator
                normalized = cv2.normalize(dvir, dvir, 0, 255, cv2.NORM_MINMAX, -1).astype(np.int8)
                date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                ndvi_f_name = '/home/pi/camera/images/ndvi-img-'+date+'.jpg'
                cv2.imwrite(ndvi_f_name, normalized)
                if check_wifi():
                    with open(ndvi_f_name, 'rb') as nf:
                        files = {'fileToUpload': nf}
                        try:
                            resp_u = requests.post(
                                URL_TO_SEND_IMAGE,
                                files=files
                            )
                        except:
                            pass
                        print(resp_u.text)
            # If we press ESC then break out of the loop
            c = cv2.waitKey(7) % 0x100
            if c == 27:
                break
            time.sleep(600) # wait 10 minutes
