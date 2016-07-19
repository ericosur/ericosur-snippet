TEMPLATE = app

QT += qml quick

CONFIG += c++11

SOURCES += main.cpp \
    mydatasource.cpp \
    ../yosemsg.cpp

HEADERS += \
    mydatasource.h \
    ../msgqdef.h \
    ../yosemsg.h

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)
