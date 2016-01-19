#-------------------------------------------------
#
# Project created by QtCreator 2016-01-05T22:03:42
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = msgq
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    yosemsg.cpp \
    simplenotify.cpp

HEADERS  += mainwindow.h \
    yosemsg.h \
    YoseMessageQueue.h \
    simplenotify.h

FORMS    += mainwindow.ui
