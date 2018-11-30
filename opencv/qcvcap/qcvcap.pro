TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp \
    demo_capture.cpp \
    core.cpp \
    BinaryCvMat.cpp

HEADERS += \
    demo_capture.h \
    core.h \
    BinaryCvMat.h

RESOURCES += qml.qrc

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
} else {
    # run 'pkg-config --libs opencv' to update the following LIBS
    INCLUDEPATH += $$system(pkg-config --cflags opencv)
    LIBS += $$system(pkg-config --libs opencv)
    message($$INCLUDEPATH)
    message($$LIBS)
}

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =


# if opencv is built with opencv_world turned on, may link only one lib file
# LIBS += -lopencv_world
