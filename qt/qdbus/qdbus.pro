QT += core dbus
QT -= gui

TARGET = qdbus
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    radiocontrol.cpp \
    tef6638_radio.cpp \
    radioadapter.cpp

DISTFILES +=

HEADERS += \
    radioAdapter.h \
    radiocontrol.h \
    tef6638_radio.h \
    radioadapter.h

