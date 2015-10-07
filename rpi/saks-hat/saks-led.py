#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

# board numbering, based on pin#
gpio.setmode(gpio.BOARD)
# output mode
gpio.setup(24, gpio.OUT)

while True:
    gpio.output(24, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(24, gpio.LOW)
    time.sleep(0.5)

