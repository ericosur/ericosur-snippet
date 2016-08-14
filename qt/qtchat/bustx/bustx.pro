#-------------------------------------------------
#
# Project created by QtCreator 2015-09-10T16:25:10
#
#-------------------------------------------------

QT += core dbus
QT -= qui
#greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
CONFIG += c++11

TARGET = bustx
TEMPLATE = app

SOURCES += main.cpp

# dbus util
HEADERS += dbusutil.h
SOURCES += dbusutil.cpp
