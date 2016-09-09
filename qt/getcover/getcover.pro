QT += core dbus
QT -= qui

CONFIG += c++11
CONFIG -= app_bundle
TARGET = getcover
TEMPLATE = app

HEADERS += getcover.h \
    yoseshm.h
SOURCES += main.cpp \
    getcover.cpp \
    yoseshm.cpp

HEADERS += tbhash.h
SOURCES += tbhash.cpp

LIBS += -ltag

# add taglib
#INCLUDEPATH += /home/rasmus/taglib/include
#LIBS += -L/home/rasmus/taglib/lib
#LIBS += -ltag

