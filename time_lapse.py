import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time

# time at start of script
time_at_start = time.time()

# the path where the raspberry pi will store its file
RASPI_PATH = f"/home/raspberrypi/{time_at_start}"

# time between captures
INTERVAL = 1
SESSION_LENGTH = 60

with PiCamera() as camera:
    camera.start_preview()

    try:
        for filename in camera.capture_continuous(RASPI_PATH + '/image{timestamp}.png'):
            time.sleep(INTERVAL)

            # time.time() is time at this point of the script
            if time.time() - time_at_start >= SESSION_LENGTH:
                break
    finally:
        camera.stop_preview()