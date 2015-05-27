TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}

LIBS += -lopencv_calib3d -lopencv_contrib -lopencv_core \
    -lopencv_features2d -lopencv_flann -lopencv_gpu -lopencv_highgui \
    -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_nonfree \
    -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_superres \
    -lopencv_ts -lopencv_video -lopencv_videostab

SOURCES += main.cpp \
    faceDemo.cpp

include(deployment.pri)
qtcAddDeployment()

