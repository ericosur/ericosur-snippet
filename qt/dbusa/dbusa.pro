QT += core dbus
QT -= gui

TARGET = dbusa
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    iface.cpp \
    ifadapter.cpp

HEADERS += \
    iface.h \
    ifadapter.h

