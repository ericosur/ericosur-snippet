#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from sense_hat import SenseHat
from instapush import Instapush, App

# appid and secret key for using web service instapush
appid = ''
secret = ''

def read_secret():
    '''
    read appid and secret key from outside file, 
    such value SHOULD NOT be kept at this script
    in json format
    '''
    global appid
    global secret
    file = 'insta.txt'
    # read from json file
    with open(file) as sec_file:
        data = json.load(sec_file)
    appid = data['appid']
    secret = data['secret']
#    print("appid:{0}\nsecret:{1}".format(appid, secret))


def send_via_insta(msg):
    '''
    need correct appid and secret, or this script could not work
    '''
    global appid
    global secret
    app = App(appid=appid, secret=secret)
    # event_name is pre-configured at https://instapush.im
    # 'message' is also pre-configured
    app.notify(event_name='rpi3b', trackers={'message': msg})


def show_tph():
    sense = SenseHat()
    t = 0
    h = 0
    p = 0

    # sometimes it will get 0 from get_pressure(), will retry
    retry = 0
    while p < 1 and retry < 5:
        p = sense.get_pressure()
        time.sleep(1)
        retry = retry + 1

    t = sense.get_temperature()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 0)
    h = round(h, 0)

    msg = "p{0} h{1} t{2}".format(p,h,t)
    return msg


if __name__ == '__main__':
    read_secret()
    msg = show_tph()
    send_via_insta(msg)

