TEMPLATE = app
TARGET = capture

# will use Qt modules
#QT       += core
#QT       -= gui
CONFIG -= qt
CONFIG += console
CONFIG -= app_bundle
CONFIG += c++11

SOURCES += main.cpp \
    captureDemo.cpp

# just execute 'pkg-config --libs opencv'' and copy result for LIBS
LIBS += -lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann -lopencv_viz -lopencv_core

macx {
    INCLUDEPATH += /opt/local/include
    LIBS += -L/opt/local/lib
}
