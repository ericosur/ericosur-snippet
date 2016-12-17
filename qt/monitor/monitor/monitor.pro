QT += core
QT -= gui
QMAKE_MAC_SDK = macosx10.12
TARGET = monitor
CONFIG += c++11 console
CONFIG -= app_bundle
TEMPLATE = app

SOURCES += main.cpp

### msgqrx ###
HEADERS += msgqrx.h
SOURCES += msgqrx.cpp

### FLOCK ###
INCLUDEPATH += $$PWD/../../qtlib
DEPENDPATH  += $$PWD/../../qtlib
LIBS += -lqtlib
LIBS += -L$$PWD/../../qtlib

## thread to wait flock ##
HEADERS += flock_wait.h \
    core.h
SOURCES += flock_wait.cpp \
    core.cpp
