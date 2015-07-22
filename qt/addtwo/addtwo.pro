TEMPLATE = app

QT += qml quick widgets

SOURCES += main.cpp

RESOURCES += qml.qrc

# Additional import path used to resolve QML modules in Qt Creator code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

HEADERS += \
    mytranslation.hpp

lupdate_only {
    SOURCES += main.qml MainForm.ui.qml
}

TRANSLATIONS = \
	lang_zh_TW.ts \
    lang_en_US.ts \
    lang_fr_FR.ts \
    lang_ar_AR.ts

DISTFILES +=
