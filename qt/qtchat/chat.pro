QT += dbus widgets

HEADERS += chat.h \
    chat_adaptor.h

SOURCES += chat.cpp \
    chat_adaptor.cpp \
    main.cpp

FORMS += chatmainwindow.ui

# chat interface
HEADERS += chat_interface.h
SOURCES += chat_interface.cpp

# dvd adaptor
#DEFINES += USE_DVD
#HEADERS += DvdAdaptor.h
#SOURCES += DvdAdaptor.cpp

#DBUS_ADAPTORS += com.pega.rasmus.xml
#DBUS_INTERFACES += com.pega.rasmus.xml

DISTFILES += com.pega.rasmus.xml \
    hu.dvd.xml

# install
target.path = $$[QT_INSTALL_EXAMPLES]/dbus/chat
INSTALLS += target
