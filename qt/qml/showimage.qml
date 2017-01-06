import QtQuick 2.5

Item {
    width: 800
    height: 600

    Rectangle {
        anchors.fill: parent
        color: "black"
        Image {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            source: "./bg.png"
        }
    }
}
