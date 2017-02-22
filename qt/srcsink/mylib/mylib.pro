#-------------------------------------------------
#
# Project created by QtCreator 2016-08-26T22:54:07
#
#-------------------------------------------------

QT -= gui
QT += core
CONFIG += c++11
CONFIG += staticlib

TARGET = mylib
TEMPLATE = lib

SOURCES += \
    util.cpp \
    commonutil.cpp \
    idhash.cpp \
    fileitem.cpp

HEADERS += \
    util.h \
    commonutil.h \
    idhash.h \
    fileitem.h


unix {
    target.path = $${PWD}/../lib/
    INSTALLS += target
}
