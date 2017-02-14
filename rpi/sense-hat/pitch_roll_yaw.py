#!/usr/bin/env python

import time
from sense_hat import SenseHat

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']

    p = round(pitch,2)
    r = round(roll,2)
    y = round(yaw,2)
    print("pitch={:<10},roll={:<10},yaw={:<10}".format(p,y,r))

