TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp \
    Source.cpp

RESOURCES += qml.qrc

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

LIBS += -lopencv_core -lopencv_highgui -lopencv_imgproc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

HEADERS +=
