TEMPLATE = app

QT += qml quick widgets
TARGET = qmlthread
CONFIG += c++11
CONFIG -= app_bundle

HEADERS += \
    mycontroller.h

SOURCES += main.cpp \
    mycontroller.cpp

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =
