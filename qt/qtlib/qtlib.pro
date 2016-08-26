#-------------------------------------------------
#
# Project created by QtCreator 2016-08-26T22:54:07
#
#-------------------------------------------------

QT       -= gui

TARGET = qtlib
TEMPLATE = lib
CONFIG += staticlib

SOURCES += qtlib.cpp

HEADERS += qtlib.h
unix {
    target.path = /usr/lib
    INSTALLS += target
}
