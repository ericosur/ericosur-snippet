import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

import com.pega.rasmus.MyController 1.0

ApplicationWindow {
    title: qsTr("move to thread test")
    width: 640
    height: 400
    visible: true

    Rectangle {
        id: rect0
        anchors.left: parent.left
        anchors.top: parent.top
        width: parent.width
        height: 40
        MyController {
            id: worker
            onResultChanged: {
                console.log("onResultChanged...")
                txtResult.text = worker.result
                area0.append(worker.result)
            }
        }
        Button {
            id: btn0
            anchors.left: parent.left
            anchors.top: parent.top
            text: "quit"
            onClicked:
            {
                //Qt.quit();
                worker.finish();
            }
        }
        Button {
            id: btn1
            anchors.left: btn0.right
            anchors.top: btn0.top
            text: "test"
            onClicked: {
                txtResult.text = "not yet..."
                worker.invokeWork()
            }
        }
    }

    Rectangle {
        id: rect1
        anchors.left: parent.left
        anchors.top: rect0.bottom
        anchors.leftMargin: 10
        //anchors.fill: parent
        width: parent.width
        height: parent.height - rect0.height
        Text {
            id: txtResult
            text: "null"
        }
        TextArea {
            id: area0
            width: parent.width
            height: parent.height - txtResult.height
            anchors.left: parent.left
            anchors.top: txtResult.bottom
            anchors.topMargin: 15
        }
    }

}
