import QtQuick 2.5
//import QtQuick.Window 2.2

Item {
    //visible: true
    //width: 1280
    //height: 800

    property int box_width: 120
    property int box_height: 60
    property int box_gap: 12
    property int box_fontsize: 20

    Rectangle {
        id: rect1
        width: box_width; height: box_height
        x: 10; y: 10
        color: "transparent"
        border.color: "blue"; border.width: 2
        Text {
            anchors.fill: parent
            text: "English"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect1");
            }
        }
    }
    Rectangle {
        id: rect2
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect1.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "العربية"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect2");
            }
        }
    }
    Rectangle {
        id: rect3
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect2.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "português"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect3");
            }
        }
    }
    Rectangle {
        id: rect4
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect3.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "français"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect4");
            }
        }
    }
    Rectangle {
        id: rect5
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect4.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "español"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect5");
            }
        }
    }
    Rectangle {
        id: rect6
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect5.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "русский"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect6");
            }
        }
    }
    Rectangle {
        id: rect7
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect6.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "український"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect7");
            }
        }
    }
    Rectangle {
        id: rect8
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect7.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "Japanese"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect8");
            }
        }
    }

}
