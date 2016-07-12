import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Item {
    width: 640
    height: 480

    property alias button1: button1
    property alias button2: button2

    Rectangle {
        width: parent.width
        height: parent.height/2
        x: 0
        y: 0
        color: "steelblue"
        Text {
            id: action
            x: 10
            y: 10
            text: "action"
        }
        Text {
            id: result
            x: 10
            y: 40
            text: "result"
        }
    }

    Rectangle {
        width: parent.width
        height: parent.height/2
        x: 0
        y: parent.height/2
        color: "pink"
        Button {
            x: 0
            y: 0
            id: button1
            text: qsTr("Press Me 1")
            onClicked: {
                action.text = "Press 1";
                myctrl.qmlRunCommand("test");
            }
        }
        Button {
            x: 0
            y: 40
            id: button2
            text: qsTr("Press Me 2")
            onClicked: {
                action.text = "press two";
                myctrl.qmlRunCommand("home");
            }
        }
    }

    Connections {
        target: myctrl
        onSigTest: {
            result.text = "onSigTest!";
        }
        onSigError: {
            result.text = "onSigError!";
        }
    }
}
