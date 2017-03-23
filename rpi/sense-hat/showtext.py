#!/usr/bin/python
from sense_hat import SenseHat
import sys
import os

rotate_degree = 180

sense = SenseHat()
sense.set_rotation(rotate_degree)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
cadetblue = (95,158,160)

if len(sys.argv) == 1:
   sense.show_message("Hello Melody!", text_colour=red)
   quit()

for i in sys.argv[1:]:
    sense.show_message(i, text_colour=blue)

