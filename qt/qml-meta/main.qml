import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

import QtMultimedia 5.0

ApplicationWindow
{
    id: root
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true

   property string audioSrc;
   //property Image coverArtImage;

    Audio {
        id: audio
        source: audioSrc
        autoPlay: false
    }

    FileDialog {
        id: fileDialog
        title: "Please choose a file."
        visible: true
        folder: shortcuts.home
        onAccepted: {
            textArea1.append("You choose: " + fileDialog.fileUrl)
            audioSrc = fileUrl;
            textArea1.append(audio.metaData.albumArtist+" -- "+audio.metaData.title);
            cover.source = audio.metaData.coverArtUrlSmall;
        }
        onRejected: {
            console.log("Canceled")
            Qt.quit()
        }
    }

    function openFile(path) {
        root.audioSrc = path
    }

    Component.onCompleted: {}

    Button {
        id: play
        x: 23; y:436
        text: qsTr("play")
    }
    MouseArea {
        anchors.fill: parent
        onClicked:  {
            textArea1.append(audio.metaData.albumArtist+" -- "+audio.metaData.title);
            textArea1.append(audio.metaData.coverArtUrlSmall);
            cover.source = audio.metaData.coverArtUrlSmall;
        }
        TextArea {
            id: textArea1
            x: 316; y: 20
            width: 300; height: 399
        }
    }
    Image {
        id: cover
        x: 23; y: 20
        width: 267; height: 287
    }

}
