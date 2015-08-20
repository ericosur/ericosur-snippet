import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2
import Qt.labs.folderlistmodel 2.1

ApplicationWindow {
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true

    //Component.onCompleted: fileDialog.open();
/*
    FileDialog {
        id: fileDialog
        title: "Choose a folder with some images"
        folder: '/';
        selectFolder: true
        onAccepted: folderModel.folder = fileUrl + "/"
    }*/
    Component {
        id: highlight
        Rectangle {
            width: 180; height: 40
            color: "lightsteelblue"; radius: 5
            y: filelist.currentItem.y
            Behavior on y { SpringAnimation { spring: 3; damping: 0.2 } }
        }
    }
    ListView {
        id: list0
        width: 200; height: 400

        FolderListModel {
            id: l0folderModel
            folder: '/Users/ericosur/Downloads/'
            nameFilters: ["*.*"]
        }

        Component {
            id: l0fileDelegate
            Text { text: fileName }
        }

        model: l0folderModel
        delegate: l0fileDelegate
    }
    ListView {
        id: filelist
        x: 0; y: 200;
        //anchors.fill: parent
        highlight: highlight
        highlightFollowsCurrentItem: false
        focus: true
        model: ListModel {
            ListElement { fileName: "a.txt" }
            ListElement { fileName: "b.txt" }
            ListElement { fileName: "c.txt" }
            ListElement { fileName: "d.txt" }
            ListElement { fileName: "e.txt" }
            ListElement { fileName: "f.txt" }
            ListElement { fileName: "g.txt" }
        }

        /*
        model: FolderListModel {
            id: folderModel
            objectName: "folderModel"
            showDirs: false
            nameFilters: ["*.png", "*.jpg", "*.gif"]
        }
        */
        /*
        header: Component {
            Text { text: currentIndex }
        }
        */

        delegate: Component {
            id: fileDelegate
            Text { text: fileName }
        }
        //Component.onCompleted: { highlightItem: 0 }
    }

}
