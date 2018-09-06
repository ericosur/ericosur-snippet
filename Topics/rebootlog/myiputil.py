#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' file: myutil.py '''

from __future__ import print_function
import subprocess

# use python to run:
# ip addr show eth0 |grep -w inet
def get_iface_ip(iface):
    p1 = subprocess.Popen(["/sbin/ip", "addr", "show", iface], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["/bin/grep", "-iw", "inet"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    ip = p2.communicate()[0].decode("utf-8").strip()
    return ip

def get_ssid():
    p0 = subprocess.Popen(["/sbin/iwgetid", "-r"], stdout=subprocess.PIPE)
#    p0.stdout.close()
    ssid = p0.communicate()[0].decode("utf-8").strip()
    return ssid

def get_extip():
	p0 = subprocess.Popen(["/usr/bin/wget", "http://ipinfo.io/ip", "-qO", "-"], stdout=subprocess.PIPE)
	extip = p0.communicate()[0].decode("utf-8").strip()
	return extip

if __name__ == "__main__":
    print("iface: " + get_iface_ip("eth0"))
    print("ssid: " + get_ssid())
    print("ssid: " + get_extip())
