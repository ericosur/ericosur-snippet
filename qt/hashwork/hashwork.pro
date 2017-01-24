# this project works only on target

QT += core
QT -= gui

TEMPLATE = app
CONFIG += c++11
QMAKE_MAC_SDK = macosx10.12
TARGET = hashwork
CONFIG += console
CONFIG -= app_bundle

SOURCES += main.cpp

HEADERS += core.h
SOURCES += core.cpp

HEADERS += pollthread.h \
    worker.h
SOURCES += pollthread.cpp \
    worker.cpp

LIBS += ${CXXFLAGS}
