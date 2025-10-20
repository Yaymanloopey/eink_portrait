#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
print(f'picdir: {picdir}')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
print(f'libdir: {libdir}')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3e
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import random

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in3e posting image")

    epd = epd7in3e.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    # read bmp file 
    logging.info("1.read bmp file")

    # Get a list of image files from the pic directory
    image_files = [f for f in os.listdir(picdir) if f.lower().endswith(('.bmp', '.jpg', '.jpeg', '.png'))]

    if not image_files:
        logging.error("No image files found in the pic directory.")
        sys.exit(1)
    
    # Choose one at random
    random_image = random.choice(image_files)
    logging.info(f"Selected image: {random_image}")

    Himage = Image.open(os.path.join(picdir, 'mimi_flat_800x480.jpg'))
    Himage = Image.open(os.path.join(picdir, random_image))
    epd.display(epd.getbuffer(Himage))
    time.sleep(3)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3e.epdconfig.module_exit(cleanup=True)
    exit()
