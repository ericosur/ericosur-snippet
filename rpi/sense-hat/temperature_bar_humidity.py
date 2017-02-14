#!/usr/bin/env python

import time
from sense_hat import SenseHat

sense = SenseHat()
repeat = 1

while repeat > 0:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    th = sense.get_temperature_from_humidity()
    tp = sense.get_temperature_from_pressure()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    th = round(th, 1)
    tp = round(tp, 1)

    msg = "temperature: {0}, pressure: {1}, humidity: {2}".format(t,p,h)
    print msg
    print("temp from humidity: %s C" % th)
    print("temp from pressure: %s C" % tp)
    time.sleep(5)
    
    repeat = repeat - 1

