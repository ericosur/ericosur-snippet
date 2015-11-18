$ qdbuscpp2xml -M radiocontrol.h -o radioctrl.xml

# edit radioctrl.xml

$ qdbusxml2cpp radioctrl.xml -i radiocontrol.h -a radioadapter

# test:

$ dbus-send --dest=local.radiocontrol --type=method_call / local.RadioControl.dump_radio_info

$ dbus-send --dest=local.radiocontrol --type=method_call / local.RadioControl.finish
