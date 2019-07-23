import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time

# the path where the raspberry pi will store its file
RASPI_PATH = f"/home/raspberrypi/{time.time()}"

INTERVAL = 1 # the time interval (in seconds) between pictures
SESSION_LENGTH = 60 # the duration of the script (in seconds)
time_at_start = time.time() # time at start of script

with PiCamera() as camera:
    camera.start_preview()

    try:
        for filename in camera.capture_continuous(RASPI_PATH + '/image{timestamp}.png'):
            print(filename)
            time.sleep(INTERVAL)

            # time.time() is time at this point of the script
            if time.time() - seconds_passed >= SESSION_LENGTH:
                break
    finally:
        camera.stop_preview()