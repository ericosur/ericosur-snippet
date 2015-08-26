#!/usr/bin/env python

'''
This basic example shows use of the Python Pillow library:

sudo pip-3.2 install pillow # or sudo pip install pillow

The tiny 8x8 chars in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License.
'''

import unicornhat as unicorn
from PIL import Image
import signal, numpy, time
from random import randint

img = Image.open('font.png')

def fill(r=0,g=255,b=0):
    for x in range(8):
        for y in range(8):
            unicorn.set_pixel(8-x-1, 8-y-1, r, g, b)
            unicorn.show()
            time.sleep(0.05)
    time.sleep(2)

def fillme():
    for x in range(8):
        for y in range(8):
            unicorn.set_pixel(8-x-1, 8-y-1, 
				randint(0,255), randint(0,255), randint(0,255))
            unicorn.show()
            time.sleep(0.05)
    time.sleep(2)

def draw_char(ch):
    o_x = ord(ch) % 16
    o_y = int(ord(ch) / 16)
    for x in range(8):
        for y in range(8):
            pixel = img.getpixel(((o_x*8)+x,(o_y*8)+y))
            #print(pixel)
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            unicorn.set_pixel(8-x-1, 8-y-1, r, g, b)
    unicorn.show()

def draw_string(str):
    for ii in range(len(str)):
        draw_char(str[ii])
        time.sleep(0.5)

unicorn.rotation(180)
unicorn.brightness(0.03)

draw_string("Hello World")
fillme()
#fill(randint(0,255),randint(0,255),randint(0,255))
draw_string("This is Rasmus")
fillme()


