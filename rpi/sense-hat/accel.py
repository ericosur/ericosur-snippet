#!/usr/bin/env python

import time
from sense_hat import SenseHat

sense = SenseHat()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)
    print("x={:<10},y={:<10},z={:<10}".format(x,y,z))

