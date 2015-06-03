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
    property alias textInput1: textInput1
    property alias textInput2: textInput2
    property alias textEdit1: textEdit1
    property alias textEdit2: textEdit2
    property alias textArea1: textArea1

    RowLayout {
        x: 50
        y: 50
        spacing: 10
        anchors.verticalCenterOffset: -115
        anchors.horizontalCenterOffset: -124
        anchors.centerIn: parent

        Button {
            id: button1
            text: qsTr("Add")
        }

        Button {
            id: button2
            text: qsTr("sin")
        }

        Button {
            id: button3
            text: qsTr("cos")
        }
    }

    TextInput {
        id: textInput1
        x: 174
        y: 41
        width: 117
        height: 20
        text: qsTr("1024")
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextInput {
        id: textInput2
        x: 174
        y: 74
        width: 117
        height: 20
        text: qsTr("399")
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

    TextEdit {
        id: textEdit1
        x: 344
        y: 41
        width: 80
        height: 20
        text: textInput1.text
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextEdit {
        id: textEdit2
        x: 344
        y: 74
        width: 80
        height: 20
        text: textInput2.text
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    Label {
        id: label1
        x: 101
        y: 76
        text: qsTr("Value #2")
    }

    Label {
        id: label2
        x: 101
        y: 43
        text: qsTr("Value #1")
    }
}
