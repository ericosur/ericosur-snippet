# noise.pro

QT += core dbus
QT -= qui

CONFIG += c++11
CONFIG -= app_bundle
TARGET = noise
TEMPLATE = app

HEADERS += mynoise.h \
    actionhandler.h

SOURCES += main.cpp \
    mynoise.cpp \
    actionhandler.cpp

# line noise
HEADERS += linenoise.h
SOURCES += linenoise.c
