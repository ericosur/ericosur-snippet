#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
#引脚采用BCM编码
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#配置一个数组，依次对应8个灯的引脚BCM编码
pins = [5, 6, 13, 19, 0, 1, 7, 8] #GPIO ports
#由于SAKS的蓝色LED和数码管共享引脚，此处将数码管位选关闭，只让信号作用于LED
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
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
    i = 0
    while True:
        setp(pins[i], 'on')
        time.sleep(0.1)
        setp(pins[i], 'off')
        time.sleep(0.1)
        i += 1
        if i == len(pins):
            i = 0
except:
    print "except"
    GPIO.cleanup()

