#!pip install python-vlc) and play the stream:
import os
#os.add_dll_directory(os.getcwd())
#os.add_dll_directory(r"C:/Program Files (x86)/VideoLAN/VLC/")

import vlc
import time
from cv_detection import find_people
from itertools import product
from random import choice
from time import sleep
from PIL import Image

player=vlc.MediaPlayer('rtsp://admin:FRCOQZ@192.168.0.8:554/H.264') #h264_stream
player.play()
time.sleep(1)
i = 0

while 1:
    i += 1
    millis = int(round(time.time() * 1000))  
    player.video_take_snapshot(0, f'images/frame_{i}_{millis}.png', 0, 0)      
    time.sleep(1)
    n_people = find_people(f'images/frame_{i}.png')
    print(f'Imagen {i} -> {n_people} personas')
    if n_people > 0:
    	img_PIL = Image.open(f'images/frame_{i}_{millis}.png')
    	img_PIL.save(f'images/detection_{i}_{n_people}.png')