import os
from picamera import PiCamera
from time import sleep
import time

# time at start of script
time_at_start = time.time()

# the path where the raspberry pi will store its file
RASPI_PATH = "/home/pi/{}/".format(time_at_start)
os.makedirs(RASPI_PATH)

# seconds between captures
INTERVAL = 1
# seconds in the air
SESSION_LENGTH = 10

with PiCamera() as camera:
    for file_type in ['yuv', 'bgr', 'bgra', 'bmp']:
        try:
            for filename in camera.capture_continuous(RASPI_PATH + 'image{counter}.{}'.format(file_type)):
                time.sleep(INTERVAL)

                # time.time() is time at this point of the script
                if time.time() - time_at_start >= SESSION_LENGTH:
                    break
        except:
            pass
