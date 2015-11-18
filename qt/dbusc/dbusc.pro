QT += core dbus
QT -= gui

TARGET = dbusc
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    clientIf.cpp \
    myhandler.cpp

HEADERS += \
    clientIf.h \
    myhandler.h

