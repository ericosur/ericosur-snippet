QT += core
QT += gui

TEMPLATE = app
CONFIG += c++11
QMAKE_MAC_SDK = macosx10.12
TARGET = dirtest
CONFIG += console
CONFIG -= app_bundle

DEFINES += USE_YOSETARGET

SOURCES += main.cpp

HEADERS += core.h
SOURCES += core.cpp

HEADERS += travelthread.h
SOURCES += travelthread.cpp
