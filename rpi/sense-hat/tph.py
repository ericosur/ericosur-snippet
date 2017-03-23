#!/usr/bin/env python

import time
from sense_hat import SenseHat

rotate_degree = 180

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

    msg = "p{0}h{1}t{2}".format(p,h,t)

    sense.set_rotation(rotate_degree)
    cadetblue = (95,158,160)
    sense.show_message(msg, text_colour=cadetblue)

if __name__ == '__main__':
	for i in range(1):
		show_tph()
		time.sleep(3)
