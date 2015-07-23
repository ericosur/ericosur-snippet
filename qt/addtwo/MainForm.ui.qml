import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

import com.pega.rasmus 1.0

Item {
    id: item1
    width: 640
    height: 480

    property alias button1: button1
    property alias button2: button2
    property alias button3: button3

    property alias buttonInit: button4
    property alias textInput1: textInput1
    property alias textInput2: textInput2
    property alias textArea1: textArea1

    property alias comboBox1: comboBox1
    //property var combo123: comboBox1

    RowLayout {
        x: 50
        y: 50
        width: 268
        height: 26
        spacing: 10
        anchors.verticalCenterOffset: -124
        anchors.horizontalCenterOffset: -85
        anchors.centerIn: parent

        Button {
            id: button1
            text: qsTr("Add1") + trans.empty
        }

        Button {
            id: button2
            text: qsTr("sin1") + trans.empty
        }

        Button {
            id: button3
            text: qsTr("cos1") + trans.empty
        }
    }

    TextInput {
        id: textInput1
        x: 174
        y: 23
        width: 117
        height: 20
        text: '0'
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextInput {
        id: textInput2
        x: 174
        y: 52
        width: 117
        height: 20
        text: '0'
        opacity: 1
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextArea {
        id: textArea1
        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.top: parent.top
        anchors.topMargin: 150
        font.family: "Tahoma"
        font.pointSize: 14
        readOnly: false
    }

    Label {
        id: label1
        x: 40
        y: 52
        text: qsTr("Value #21") + trans.empty
    }

    Label {
        id: label2
        x: 40
        y: 25
        text: qsTr("Value #11") + trans.empty
    }

    Button {
        id: button4
        x: 365
        y: 52
        text: qsTr("Random1") + trans.empty
    }

    ComboBox {
        id: comboBox1
        x: 478
        y: 20
        width: 131
        height: 26
        model: ListModel {
            //id: cbItems
            ListElement { text: "French"; loc: "fr" }
            ListElement { text: "English"; loc: "en" }
            ListElement { text: "Chinese"; loc: "zh" }
        }
    }

    Label {
        id: label3
        x: 381
        y: 25
        width: 96
        height: 16
        text: qsTr("Set Language")
    }
}
