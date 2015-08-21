import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

import QtMultimedia 5.0

ApplicationWindow
{
    id: root
    title: qsTr("Hello World")
    width: 800
    height: 800
    visible: true

    //property string audioSrc;

    Flipable {
        id: flipable
        x: 100; y: 100
        width: 500; height: 500

        property bool flipped: false

        front: Image { source: "prev.jpg"; anchors.centerIn: parent }
        back: Image { source: "next.jpg"; anchors.centerIn: parent }

        transform: Rotation {
            id: rotation
            origin.x: flipable.width/2
            origin.y: flipable.height/2
            axis.x: 0; axis.y: 1; axis.z: 0     // set axis.y to 1 to rotate around y-axis
            angle: 0    // the default angle
        }
        states: State {
            name: "back"
            PropertyChanges { target: rotation; angle: 180 }
            when: flipable.flipped
        }
        transitions: Transition {
            NumberAnimation { target: rotation; property: "angle"; duration: 3000 }
        }
        MouseArea {
            anchors.fill: parent
            onClicked: flipable.flipped = !flipable.flipped
        }
    }
}
