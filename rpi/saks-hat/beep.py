#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

PIN_NO_BEEP = 11
PIN_NO_LED = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO_BEEP, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN_NO_LED, GPIO.OUT, initial=GPIO.HIGH)

# 单次哔声和LED发光
def beep(seconds):
    GPIO.output(PIN_NO_BEEP, GPIO.LOW)
    GPIO.output(PIN_NO_LED, GPIO.LOW)
    time.sleep(seconds)
    GPIO.output(PIN_NO_BEEP, GPIO.HIGH)
    GPIO.output(PIN_NO_LED, GPIO.HIGH)

# 多次哔声和LED发光封装函数，输入参数分别为“占空时间”以及重复次数
def beepAction(secs, sleepsecs, times):
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)

beep(1)
