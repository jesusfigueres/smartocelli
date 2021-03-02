#!pip install python-vlc) and play the stream:

import vlc
import time
from cv import find_people
from itertools import product
from random import choice
from time import sleep
from sense_hat import SenseHat
from conway import *

sense = SenseHat()

#player=vlc.MediaPlayer('rtsp://admin:FRCOQZ@192.168.1.106:554/H.264')
player=vlc.MediaPlayer('rtsp://admin:FRCOQZ@192.168.0.8:554/H.264') #h264_stream
player.play()
i = 0

while 1:
    i += 1
    millis = int(round(time.time() * 1000))    
    time.sleep(1)
    player.video_take_snapshot(0, f'images/entrada_{i}_{millis}.png', 0, 0)
    num_people = find_people(f'images/entrada_{i}.png')
    print(f'Imagen {i} -> {num_people} personas')