import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.2

ApplicationWindow {
    visible: true
    width: 640; height: 480
    x: 0; y: 0
    title: qsTr("Hello World")

    MainForm {
        width: 640; height: 480
        x: 100; y: 0
    }

    ListView {
        width: 100; height: 100
        x: 0; y: 0
        model: myModel
        delegate: Rectangle {
            height: 25
            width: 100
            Text { text: modelData }
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                var count = myctrl.mylist.length;
                if (count == 0) {
                    console.log("count is zero");
                }

                for(var i=0;i<count; i++) {
                    console.debug("StringList number ->" + (i+1));
                    var string = myctrl.mylist[i];
                    console.debug(string);
                }
            }
        }
    }
}
