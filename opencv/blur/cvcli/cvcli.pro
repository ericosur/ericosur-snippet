TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

LIBS += -lopencv_core -lopencv_highgui -lopencv_imgproc

SOURCES += main.cpp

include(deployment.pri)
qtcAddDeployment()
