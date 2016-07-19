import QtQuick 2.5
import QtQuick.Controls 1.4

ApplicationWindow {
    visible: true
    width: 640; height: 480
    x: 10; y: 10
    title: qsTr("Hello World")

    Rectangle {
        id: rectupper
        width: 320; height: 240
        x: 0; y: 0
        color: "steelblue"
        Text {
            text: "hello world"
        }
    }

    Rectangle {
        id: rectlower
        width: 320; height: 240
        x: 0; y: 240
        color: "burlywood"
        Text {
            text: "lower part"
        }
    }

    Rectangle {
        id: rectcommand
        width: 320; height: 480
        x: 320; y: 0
        color: "dimgrey"
        Text {
            id: greytext
            text: "image here"
        }
        Button {
            id: greybutton1
            anchors.top: greytext.bottom
            anchors.topMargin: 10
            anchors.left: greytext.left
            text: "load..."
            onClicked: {
                console.log("grey button1");
                mydatasource.loadAction();
            }
        }
        Button {
            id: greybutton2
            anchors.top: greybutton1.bottom
            anchors.topMargin: 10
            anchors.left: greytext.left
            text: "check..."
            onClicked: {
                console.log("grey button2");
                mydatasource.checkAction();
            }
        }
    }
}
