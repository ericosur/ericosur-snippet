#-------------------------------------------------
#
# Project created by QtCreator 2016-08-26T22:54:07
#
#-------------------------------------------------

QT       -= gui
QT += core

TARGET = qtlib
TEMPLATE = lib
CONFIG += staticlib

SOURCES += retry.cpp
HEADERS += retry.h
unix {
    target.path = /usr/lib
    INSTALLS += target
}
