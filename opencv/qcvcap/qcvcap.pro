TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp \
    demo_capture.cpp \
    core.cpp

HEADERS += \
    demo_capture.h \
    core.h

RESOURCES += qml.qrc

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =


# run 'pkg-config --libs opencv' to update the following LIBS
LIBS += \
-lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann -lopencv_viz -lopencv_core
