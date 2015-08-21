TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt
CONFIG += localtaglib

CONFIG(localtaglib) {
    macx {
        INCLUDEPATH += /Users/ericosur/taglib/include/taglib
        LIBS += -L/Users/ericosur/taglib/lib
    } else {
        INCLUDEPATH += /home/rasmus/taglib/include/taglib
        LIBS += -L/home/rasmus/taglib/lib
    }
} else {
    INCLUDEPATH += /usr/include/taglib
}

LIBS += -ltag

SOURCES += main.cpp

include(deployment.pri)
qtcAddDeployment()

