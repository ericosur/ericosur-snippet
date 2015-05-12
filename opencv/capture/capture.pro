#-------------------------------------------------
#
# Project created by QtCreator 2015-05-12T13:35:09
#
#-------------------------------------------------

QT       += core

QT       -= gui

TARGET = capture
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

LIBS += -lopencv_core -lopencv_highgui -lopencv_imgproc


SOURCES += main.cpp \
    captureDemo.cpp
