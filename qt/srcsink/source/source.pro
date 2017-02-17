QT += core
QT -= gui
QMAKE_MAC_SDK = macosx10.12
TARGET = source
CONFIG += c++11 console
CONFIG -= app_bundle
TEMPLATE = app

SOURCES += main.cpp

### msgqrx ###
HEADERS += msgqrx.h
SOURCES += msgqrx.cpp

HEADERS += \
    core.h \
    travelthread.h \
    getcover.h

SOURCES += \
    core.cpp \
    travelthread.cpp \
    getcover.cpp

LIBS += -ltag -lz

INCLUDEPATH += $${PWD}/../mylib
LIBS += -L$${PWD}/../lib -lmylib

unix {
    target.path = $${PWD}/../out/
    INSTALLS += target
}
