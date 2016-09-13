TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp

# use local build taglib
INCLUDEPATH += /usr/local/include
LIBS += -L/usr/local/lib
LIBS += -ltag -lz
