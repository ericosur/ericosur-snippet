TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

LIBS += -lopencv_core -lopencv_highgui -lopencv_imgproc

SOURCES += main.cpp

include(deployment.pri)
qtcAddDeployment()
