Trouble Shooting
================

pi@rpi ~/src/snippet/qt/qtchat/dbus1 ()$ ./ds send h
Sending signal with value h
Connection Error (Unable to autolaunch a dbus-daemon without a $DISPLAY for X11)

solution:
Manually run a copy of dbus-daemon:
```
DBUS_VERBOSE=1 dbus-daemon --session --print-address
```
will get address like:
```
unix:abstract=/tmp/dbus-RT9ZnLY2Jj,guid=d666b44cd6a6016184556f8e57aeac92
```
set it into DBUS_SESSION_BUS_ADDRESS and run
```
DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-RT9ZnLY2Jj,guid=d666b44cd6a6016184556f8e57aeac92  \
./ds receive
```

