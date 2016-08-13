QT += dbus widgets

HEADERS += chat.h \
    chat_adaptor.h \
    chat_interface.h
SOURCES += chat.cpp \
    chat_adaptor.cpp \
    chat_interface.cpp
FORMS += chatmainwindow.ui

#DBUS_ADAPTORS += com.pega.rasmus.xml
#DBUS_INTERFACES += com.pega.rasmus.xml

# install
target.path = $$[QT_INSTALL_EXAMPLES]/dbus/chat
INSTALLS += target
