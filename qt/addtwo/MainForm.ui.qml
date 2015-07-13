import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

Item {
    id: item1
    width: 640
    height: 480

    property alias button3: button3
    property alias button2: button2
    property alias button1: button1
    property alias buttonInit: button4
    property alias textInput1: textInput1
    property alias textInput2: textInput2
    property alias textArea1: textArea1

    RowLayout {
        x: 50
        y: 50
        width: 190
        height: 26
        spacing: 10
        anchors.verticalCenterOffset: -115
        anchors.horizontalCenterOffset: -24
        anchors.centerIn: parent

        Button {
            id: button1
            text: qsTr("Add1")
        }

        Button {
            id: button2
            text: qsTr("sin1")
        }

        Button {
            id: button3
            text: qsTr("cos1")
        }
    }

    TextInput {
        id: textInput1
        x: 174
        y: 41
        width: 117
        height: 20
        text: '0'
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextInput {
        id: textInput2
        x: 174
        y: 74
        width: 117
        height: 20
        text: '0'
        opacity: 1
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextArea {
        id: textArea1
        x: 101
        y: 165
        width: 438
        height: 249
        font.family: "Verdana"
        font.pointSize: 12
        readOnly: true
    }

    Label {
        id: label1
        x: 101
        y: 76
        text: qsTr("Value #21")
    }

    Label {
        id: label2
        x: 101
        y: 43
        text: qsTr("Value #11")
    }

    Button {
        id: button4
        x: 100
        y: 112
        text: qsTr("Random1")
    }
}
