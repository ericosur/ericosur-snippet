QT += core
QT -= qui

TARGET = qtcmd
TEMPLATE = app
CONFIG += c++11
CONFIG += console
CONFIG -= app_bundle

SOURCES += main.cpp
HEADERS += wait.h

# retry thread is moved into libqtlib.a
#SOURCES += retry.cpp
#HEADERS += retry.h

SOURCES += pass.cpp
HEADERS += pass.h

INCLUDEPATH += $$PWD/../qtlib
DEPENDPATH  += $$PWD/../qtlib
LIBS += -lqtlib
LIBS += -L$$PWD/../qtlib


