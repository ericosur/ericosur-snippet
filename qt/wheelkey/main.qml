import QtQuick 2.3
import QtQuick.Controls 1.2

ApplicationWindow {
    visible: true
    width: 800
    height: 480
    title: qsTr("Wheel Key Setting")

    property int seperate_line_height: 110
    // width between cell for buttons
    property int seperate_button_space: 145
    property var button_color: "steelblue"
    property var button_color_highlight: "indianred"
    property var button_color_set: "green"
    property var button_color_na: "grey"
    property var button_color_unset: "red"
    property var button_text_highlight: "orange"
    property var button_text_normal: "black"

    Rectangle {
        anchors.fill: parent
        color: "cornsilk"
    }

    Rectangle {
        id: message_box
        anchors.top: parent.top
        width: parent.width - 100
        height: 100
        x: (parent.width - width)/2
        color: "cyan"
        border.width: 2
        border.color: "black"

        Text {
            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 10
            id: message_box_text
            text: "1. Choose the button below to setup\n2. Press the corresponding button on steering wheel\n   until button change to green color"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignLeft
            font.pointSize: 20
        }
    }

    Rectangle {
        id: seperate_hline1
        anchors.top: message_box.bottom
        x: message_box.x
        width: parent.width
        height: 2
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline1
        anchors.top: message_box.bottom
        x: message_box.x
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline2
        anchors.top: message_box.bottom
        x: seperate_vline1.x + seperate_button_space
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline3
        anchors.top: message_box.bottom
        x: seperate_vline2.x + seperate_button_space
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline4
        anchors.top: message_box.bottom
        x: seperate_vline3.x + seperate_button_space
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline5
        anchors.top: message_box.bottom
        x: seperate_vline4.x + seperate_button_space
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_vline6
        anchors.top: message_box.bottom
        x: seperate_vline5.x + seperate_button_space
        width: 2
        height: parent.height - message_box.height
        color: "transparent"
    }
    Rectangle {
        id: seperate_hline2
        y: seperate_hline1.y + seperate_line_height
        width: parent.width
        height: 2
        color: "transparent"
    }
    Rectangle {
        id: seperate_hline3
        y: seperate_hline2.y + seperate_line_height
        width: parent.width
        height: 2
        color: "transparent"
    }
    Rectangle {
        id: seperate_hline4
        y: seperate_hline3.y + seperate_line_height + 40
        width: parent.width
        height: 2
        color: "transparent"
    }

    property int enum_button_unset: 31;
    property int enum_button_set: 32;
    property int enum_button_na: 33;

    function setButtonColor(button, value) {
        if (value == enum_button_na) {
            button.color = button_color_na;
        } else if (value == enum_button_set) {
            button.color = button_color_set;
        } else if (value == enum_button_unset) {
            button.color = button_color_unset;
        }
    }

    Rectangle {
        id: button_areaA1
        anchors.top: seperate_hline1.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline1.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline2.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline2.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_a1
            anchors.fill: parent
            onClicked: {
                //parent.color = button_color_highlight;
                setButtonColor(parent, enum_button_unset);
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxA1_text
            text: "PREV"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_a1.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaA2
        anchors.top: seperate_hline2.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline1.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline2.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline3.top
        anchors.bottomMargin: 20
        radius: 10
        color: {
            return ( (mousearea_a2.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_a2
            anchors.fill: parent
            onClicked: {
                setButtonColor(parent, enum_button_unset);
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxA2_text
            text: "VOL UP"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_a2.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaB1
        anchors.top: seperate_hline1.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline2.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline3.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline2.top
        anchors.bottomMargin: 20
        radius: 10
        color: {
            return ( (mousearea_b1.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_b1
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxB1_text
            text: "NEXT"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_b1.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }

    }
    Rectangle {
        id: button_areaB2
        anchors.top: seperate_hline2.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline2.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline3.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline3.top
        anchors.bottomMargin: 20
        radius: 10
        color: {
            return ( (mousearea_b2.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_b2
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxB2_text
            text: "VOL DOWN"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_b2.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaC1
        anchors.top: seperate_hline1.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline3.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline4.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline2.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_c1
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxC1_text
            text: "HOME"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_c1.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }
    Rectangle {
        id: button_areaC2
        anchors.top: seperate_hline2.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline3.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline4.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline3.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_c2
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxC2_text
            text: "MUTE"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_c2.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaD1
        anchors.top: seperate_hline1.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline4.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline5.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline2.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_d1
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxD1_text
            text: "MODE"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_d1.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaD2
        anchors.top: seperate_hline2.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline4.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline5.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline3.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_d2
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxD2_text
            text: "BACK"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_d2.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaE1
        anchors.top: seperate_hline1.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline5.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline6.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline2.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_e1
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxE1_text
            text: "PHONE"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_e1.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaE2
        anchors.top: seperate_hline2.bottom
        anchors.topMargin: 20
        anchors.left: seperate_vline5.right
        anchors.leftMargin: 20
        anchors.right: seperate_vline6.left
        anchors.rightMargin: 20
        anchors.bottom: seperate_hline3.top
        anchors.bottomMargin: 20
        radius: 10
        color: button_color
        MouseArea {
            id: mousearea_e2
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxE2_text
            text: "NAVI"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_e2.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: hint_message_box
        anchors.top: seperate_hline3.bottom
        anchors.topMargin: 10
        anchors.left: seperate_vline2.right
        anchors.leftMargin: 10
        anchors.right: seperate_vline5.left
        anchors.rightMargin: 10
        height: 40
        border.width: 2
        border.color: "transparent"
        color: "grey"
        Text {
            anchors.top: parent.verticalCenter
            anchors.topMargin: -10
            anchors.left: parent.left
            anchors.leftMargin: 10
            id: hint_message_box_text
            text: "Message:"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
        }
    }

    Rectangle {
        id: button_areaB3
        anchors.top: hint_message_box.bottom
        anchors.topMargin: 15
        anchors.left: seperate_vline2.right
        anchors.leftMargin: 10
        anchors.right: seperate_vline3.left
        anchors.rightMargin: 10
        anchors.bottom: seperate_hline4.top
        anchors.bottomMargin: 15
        radius: width * 0.75
        color: {
            return ( (mousearea_b3.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_b3
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxB3_text
            text: "Save"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_b3.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaC3
        anchors.top: hint_message_box.bottom
        anchors.topMargin: 15
        anchors.left: seperate_vline3.right
        anchors.leftMargin: 10
        anchors.right: seperate_vline4.left
        anchors.rightMargin: 10
        anchors.bottom: seperate_hline4.top
        anchors.bottomMargin: 15
        radius: width * 0.75
        color: {
            return ( (mousearea_c3.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_c3
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxC3_text
            text: "Cancel"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_c3.containsMouse) ? button_text_highlight : button_text_normal );
            }
        }
    }

    Rectangle {
        id: button_areaD3
        anchors.top: hint_message_box.bottom
        anchors.topMargin: 15
        anchors.left: seperate_vline4.right
        anchors.leftMargin: 10
        anchors.right: seperate_vline5.left
        anchors.rightMargin: 10
        anchors.bottom: seperate_hline4.top
        anchors.bottomMargin: 15
        radius: width * 0.75
        color: {
            return ( (mousearea_d3.containsMouse) ? button_color_highlight : button_color );
        }
        MouseArea {
            id: mousearea_d3
            anchors.fill: parent
            onClicked: {
            }
        }
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            id: boxD3_text
            text: "Reset All"
            font.family: "Andale Mono"
            font.bold: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 20
            color: {
                return ( (mousearea_d3.containsMouse) ? button_text_highlight : "red" );
            }
        }
    }

}
