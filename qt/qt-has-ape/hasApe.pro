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
INCLUDEPATH += /usr/local/include
LIBS += -L/usr/local/lib
LIBS += -ltag -lz
