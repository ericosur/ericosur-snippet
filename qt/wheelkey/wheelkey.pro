TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp \
    parsestatus.cpp

RESOURCES += qml.qrc

QMAKE_MAC_SDK = macosx10.11

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

HEADERS += \
    parsestatus.h
