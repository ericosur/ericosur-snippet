#!/usr/bin/env python

import time
from sense_hat import SenseHat

def show_tph():
    sense = SenseHat()
    t = 0
    h = 0
    p = 0
    while p < 1:
        p = sense.get_pressure()
        time.sleep(1)

    t = sense.get_temperature()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 0)
    h = round(h, 0)

    msg = "t{0} p{1} h{2}".format(t,p,h)

    sense.set_rotation(270)
    cadetblue = (95,158,160)
    sense.show_message(msg, text_colour=cadetblue)

if __name__ == '__main__':
	for i in range(2):
		show_tph()
		time.sleep(3)
