TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

HEADERS +=

lupdate_only {
    SOURCES += main.qml MainForm.ui.qml
}

TRANSLATIONS = lang_zh_TW.ts lang_en_US.ts

DISTFILES +=
