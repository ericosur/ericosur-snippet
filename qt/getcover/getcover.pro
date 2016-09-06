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

exists(../../product.sh) {
    message("product.sh found ==> HOST build")
    CONFIG -= use_target
} else {
    message("product.sh not found ==> TARGET build")
    CONFIG += use_target
}

use_target {
    DEFINES += USE_YOSETARGET
    INCLUDEPATH += ../
} else {

}

# add taglib
#INCLUDEPATH += /home/rasmus/taglib/include
#LIBS += -L/home/rasmus/taglib/lib
#LIBS += -ltag

