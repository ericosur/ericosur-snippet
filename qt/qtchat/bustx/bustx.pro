# bustx.pro

TARGET = bustx
TEMPLATE = app

QT += core dbus
QT -= qui
CONFIG += c++11

# test
CONFIG += console
CONFIG -= app_bundle


SOURCES += main.cpp

# dbus util
HEADERS += dbusutil.h
SOURCES += dbusutil.cpp
