TEMPLATE = app
TARGET = sink
QT += core
QT -= gui
CONFIG += c++11 console
CONFIG -= app_bundle
QMAKE_MAC_SDK = macosx10.12

HEADERS += \
    flowctrl.h \
    readthread.h

SOURCES += main.cpp \
    flowctrl.cpp \
    readthread.cpp

### msgq ####
HEADERS += msgqsend.h
SOURCES += msgqsend.cpp

INCLUDEPATH += $${PWD}/../mylib
LIBS += -L$${PWD}/../lib -lmylib

unix {
    target.path = $${PWD}/../out/
    INSTALLS += target
}
