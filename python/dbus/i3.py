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
obj = bus.get_object("org.gnome.Terminal.Display_0", # Connection name
                    "/org/gnome/Terminal/Display_0" # Object's path
        )

# get a particular interface
print ("Introspection data:\n")
print obj.Introspect()

'''
dbus-send --session \
--type=method_call --print-reply \
--dest=org.gnome.Rhythmbox \
/org/gnome/Rhythmbox/Player \
org.freedesktop.DBus.Introspectable.Introspect
'''