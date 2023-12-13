#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' file: myutil.py '''

from __future__ import print_function

import subprocess


# use python to run:
# ip addr show eth0 |grep -w inet
def get_iface_ip(iface):
    ''' get_iface_ip '''
    ip = None
    with subprocess.Popen(["/sbin/ip", "addr", "show", iface],
        stdout=subprocess.PIPE) as p1:
        with subprocess.Popen(["/bin/grep", "-iw", "inet"],
            stdin=p1.stdout, stdout=subprocess.PIPE) as p2:
            p1.stdout.close()
            ip = p2.communicate()[0].decode("utf-8").strip()
            #print('p2.returncode:', p2.returncode)
            if p2.returncode:
                # 'iface' not found
                ip = ''
    return ip

def get_ssid():
    ''' get_ssid '''
    ret = None
    with subprocess.Popen(["/sbin/iwgetid", "-r"], stdout=subprocess.PIPE) as p0:
        ret = p0.communicate()[0].decode("utf-8").strip()
    return ret

def get_extip():
    ''' get_extip '''
    ret = None
    with subprocess.Popen(["/usr/bin/wget", "http://ipinfo.io/ip", "-qO", "-"],
                          stdout=subprocess.PIPE) as p0:
        ret = p0.communicate()[0].decode("utf-8").strip()
    return ret

def main():
    ''' main '''
    ifs = ['eth0', 'eno1']
    for i in ifs:
        ret = get_iface_ip(i)
        print(ret)
    #print("ssid: " + get_ssid())
    #print("ssid: " + get_extip())


if __name__ == "__main__":
    main()
