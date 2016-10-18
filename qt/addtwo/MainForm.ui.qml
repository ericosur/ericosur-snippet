import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

import com.pega.rasmus 1.0

Item {
    id: item1
    width: 640
    height: 480

    property alias buttonInit: button4
    property alias textInput1: textInput1
    property alias textInput2: textInput2
    property alias textArea1: textArea1

    property alias comboLang: comboLang
    property alias comboAction: comboAction

    property alias btnNormal: btnNormal
    property alias btnFullscreen: btnFullScreen

    property alias editTest: editTest
    property alias labelTest: labelTest

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
        anchors.rightMargin: 0
        anchors.left: parent.left
        anchors.leftMargin: 0
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.top: parent.top
        anchors.topMargin: 158
        font.family: "Tahoma"
        font.pointSize: 14
        readOnly: false
    }

    Label {
        id: label1
        x: 40
        y: 52
        text: qsTr("Value #21") + trs.empty
    }

    Label {
        id: label2
        x: 40
        y: 25
        text: qsTr("Value #11") + trs.empty
    }

    Button {
        id: button4
        x: 397
        y: 84
        text: qsTr("Random1") + trs.empty
    }

    ComboBox {
        id: comboLang
        x: 478
        y: 20
        width: 131
        height: 26
        model: ListModel {
            //id: cbItems
            ListElement { text: QT_TR_NOOP("le français"); loc: "fr" }
            ListElement { text: QT_TR_NOOP("English"); loc: "en" }
            ListElement { text: QT_TR_NOOP("中文"); loc: "zh" }
        }
    }

    Label {
        id: label3
        x: 381
        y: 25
        width: 96
        height: 16
        text: qsTr("Set Language") + trs.empty
    }

    Button {
        id: btnNormal
        x: 8
        y: 84
        text: qsTr("origin") + trs.empty
    }

    Button {
        id: btnFullScreen
        x: 202
        y: 84
        text: qsTr("fullscreen") + trs.empty
    }

    Label {
        id: label4
        x: 381
        y: 56
        width: 96
        height: 16
        text: qsTr("Operation") + trs.empty
    }

    ComboBox {
        id: comboAction
        x: 478
        y: 52
        width: 131
        height: 26
        model: ListModel {
            ListElement { text: QT_TR_NOOP("n/a") }
            ListElement { text: QT_TR_NOOP("Add") }
            ListElement { text: QT_TR_NOOP("sin()") }
            ListElement { text: QT_TR_NOOP("cos()") }
            ListElement { text: QT_TR_NOOP("clear") }
        }
    }

    TextEdit {
        id: editTest
        x: 40
        y: 127
        width: 146
        height: 20
        text: qsTr("empty string") + trs.empty
        font.pixelSize: 14
    }

    Label {
        id: labelTest
        x: 197
        y: 129
        width: 163
        height: 17
        text: qsTr("test label") + trs.empty
    }
}
