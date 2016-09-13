TEMPLATE = app

QT += qml quick widgets multimedia

SOURCES += main.cpp

RESOURCES += qml.qrc

OTHER_FILES += $${QML_FILES}

QML_FILES += $$files(/mp3/*.mp3,true)

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)
