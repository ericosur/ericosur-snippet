#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
#引脚采用BCM编码
GPIO.setmode(GPIO.BCM)
#配置一个数组，依次对应8个灯的引脚BCM编码
pins = [5, 6, 13, 19, 0, 1, 7, 8] #GPIO ports
#定义一个便捷地设置引脚的方法
def setp(n, status='off'):
    if status == 'on':
        GPIO.output(n, GPIO.LOW)
    else:
        GPIO.output(n, GPIO.HIGH)
#遍历数组，将数组中8个LED引脚初始化
for i in pins:
    GPIO.setup(i, GPIO.OUT)
    setp(i, 'off')

try:
    #遍历数组，将数组中8个LED引脚置为ON同时点亮LED
    for i in pins:
        setp(i, 'off')
except:
    print "except"
    GPIO.cleanup()
