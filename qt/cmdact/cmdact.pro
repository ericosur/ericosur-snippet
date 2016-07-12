TEMPLATE = app

QT += qml quick widgets

CONFIG += c++11

HEADERS += \
    msgqcommand.h

SOURCES += main.cpp \
    msgqcommand.cpp

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)
