#!/usr/bin/env python

'''
https://wiki.python.org/moin/DbusExamples
'''

# You must initialize the gobject/dbus support for threading
# before doing anything.
import gobject
gobject.threads_init()

from dbus import glib
glib.init_threads()

# Create a session bus.
import dbus
bus = dbus.SessionBus()

# Create an object that will proxy for a particular remote object.
remote_object = bus.get_object("org.freedesktop.DBus", # Connection name
                               "/org/freedesktop/DBus" # Object's path
                              )

# Introspection returns an XML document containing information
# about the methods supported by an interface.
print ("Introspection data:\n")
print remote_object.Introspect()
