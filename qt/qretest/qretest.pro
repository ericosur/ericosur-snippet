QT += core
QT -= gui

CONFIG += c++11
QMAKE_MAC_SDK = macosx10.12
TARGET = qretest
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp

## TESTS ##
HEADERS += testcases.h
SOURCES += testcases.cpp

## QIBLA ##
HEADERS += qibla.h
SOURCES += qibla.cpp

### FLOCK ###
INCLUDEPATH += $$PWD/../qtlib
DEPENDPATH  += $$PWD/../qtlib
LIBS += -lqtlib
LIBS += -L$$PWD/../qtlib
