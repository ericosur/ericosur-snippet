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

    property alias button_zh: button_zh
    property alias button_en: button_en
    property alias button_fr: button_fr

    property alias buttonInit: button4
    property alias textInput1: textInput1
    property alias textInput2: textInput2
    property alias textArea1: textArea1

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
            text: qsTr("Add1") + trans.emptyString
        }

        Button {
            id: button2
            text: qsTr("sin1") + trans.emptyString
        }

        Button {
            id: button3
            text: qsTr("cos1") + trans.emptyString
        }
    }

    TextInput {
        id: textInput1
        x: 174
        y: 18
        width: 117
        height: 20
        text: '0'
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 14
    }

    TextInput {
        id: textInput2
        x: 174
        y: 44
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
        y: 155
        width: 438
        height: 307
        font.family: "Tahoma"
        font.pointSize: 12
        readOnly: true
    }

    Label {
        id: label1
        x: 101
        y: 46
        text: qsTr("Value #21") + trans.emptyString
    }

    Label {
        id: label2
        x: 101
        y: 20
        text: qsTr("Value #11") + trans.emptyString
    }

    Button {
        id: button4
        x: 101
        y: 70
        text: qsTr("Random1") + trans.emptyString
    }

    Button {
        id: button_zh
        x: 435
        y: 103
        text: qsTr("load zh")
    }

    Button {
        id: button_en
        x: 435
        y: 20
        text: qsTr("load en")
    }

    Button {
        id: button_fr
        x: 435
        y: 60
        text: qsTr("load fr")
    }
}
