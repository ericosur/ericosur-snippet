#!/usr/bin/env python

from sense_hat import SenseHat

sense = SenseHat()

ROW = 8
COL = 8

for r in range(ROW):
    for c in range(COL):
        sense.set_pixel(r, c, 0, 0, 0)

sense.show_message("ok")

