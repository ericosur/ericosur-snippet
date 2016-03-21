QT += core
QT -= gui

CONFIG += c++11

TARGET = hasApe
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    util.cpp

HEADERS += \
    util.h

# add taglib
INCLUDEPATH += /home/rasmus/taglib/include
LIBS += -L/home/rasmus/taglib/lib
LIBS += -ltag
