#!/usr/bin/env python
'''
a simple demo for pynotify (under gnome)

code copy/paste from:
	http://blogs.divisibleprime.com/ronin/articles/2008/03/10/command-line-gnome-notification

more example can be found: /usr/share/doc/python-notify/examples
'''

from pynotify import *
import sys

def notify(message=""):
	n = Notification("Command Line Completed", message)
	n.show()

init("cli notify")
if len(sys.argv) > 1:
	notify(sys.argv[1])
else:
	notify()

