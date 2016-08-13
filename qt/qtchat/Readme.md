qtchat
======

This program is modified from qt dbus example application.
It is QtWidget application with GUI to interact.


dbus1
-----

At subfolder [dbus1][2], there is a simple dbus signal sender/receiver 
to test qtchat application. Enter this sub folder and run __make__ to 
build this simple CLI application. You need package 
libdbus-1-dev installed.
```
sudo apt-get install libdbus-1-dev
```
Run a DBus signal receiver by:
```
./ds receive
```
Will run forever to listen the signal.
You may send signal by:
```
./ds send "Hello world"
```
And the receiver (both ds and chat) will quit if you send
```
./ds send quit
```


DBus Interface
--------------

DBus interface used by qtchat is defined at [com.pega.rasmus.xml][1]

**DO NOT MODIFY chat_adaptor.* and chat_interface.* manually**

Use the following commands to generate them:
```
$ qdbusxml2cpp -c ChatAdaptor -a chat_adaptor.h:chat_adaptor.cpp com.pega.rasmus.xml
$ qdbusxml2cpp -p chat_interface.h:chat_interface.cpp com.pega.rasmus.xml
```

[1]: ./com.pega.rasmus.xml
[2]: ./dbus1/

How To Test
-----------
Run chat application twice:
```
./chat &
./chat &
```
They will have different UUID to tell from.
Input text into text field and send _broadcast DBus signal_ out.

Also you may use *ds* mentioned at section "dbus1". Chat application will 
receive text from *ds*.

Also you may use standard dbus-send to test:
```
dbus-send --session --type=signal /qtapp com.pega.rasmus.foobar string:"Hello World!"
```
If something wrong, may use dbus-monitor:
```
dbus-monitor interface=com.pega.rasmus path=/qtapp
```
If you see nothing by this command, maybe "path" is wrong.
Broaden the filter setting:
```
dbus-monitor interface=com.pega.rasmus
```

Will both received by chat application and "ds receive"
