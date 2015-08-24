import QtQuick 2.4
import QtQuick.Window 2.2
import QtQuick.Controls 1.3

// Custom types of C++
import com.pega.rasmus.ID3TAG 1.0

ApplicationWindow {
    width : 600; height: 800
    title: "main window"
    id: root;
    visible: true

    property string prev_img;
    property string next_img;

    // C++ class id3tag
    ID3TAG {
        id: id3tag
    }
    function myloadmp3(fn, img) {
        if ( id3tag.getMetaData(fn) ) {
            filename.text = id3tag.filename;
            title.text = 'title: ' + id3tag.title;
            artist.text = 'artist: ' + id3tag.artist;
            album.text = 'album: ' + id3tag.album;
            img.source = "file://" + id3tag.coverpath;
            img.width = 100;
            img.height = 100;
            return id3tag.coverpath;
        }
    }

    Rectangle {
        id: button_area
        x: 0; y: 0
        width: parent.width
        height: 40

        Button {
            id: start;
            text: "load and go";
            anchors.left: parent.left;
            anchors.leftMargin: 4;
            anchors.bottom: parent.bottom;
            anchors.bottomMargin: 4;
            onClicked: {
                var fn = "/Users/ericosur/Downloads/go/testmp3/03.mp3";
                prev_img = "file://" + myloadmp3(fn, img0);
                console.log(prev_img);
                var fn = "/Users/ericosur/Downloads/go/testmp3/04.mp3";
                next_img = "file://" + myloadmp3(fn, img1);

                flipable.visible = true;
                flipable.flipped = !flipable.flipped;
            }
        }

        Button {
            id: quit;
            text: "Quit";
            anchors.left: start.right
            anchors.leftMargin: 20;
            anchors.bottom: start.bottom;
            onClicked: { Qt.quit(); }
        }
    }

    Rectangle {
        id: text_area
        anchors.top: button_area.bottom
        anchors.left: parent.left;
        width: parent.width; height: 100;

        Text {
            id: filename;
            anchors.left: parent.left;
            anchors.leftMargin: 4;
            anchors.top: parent.top;
            anchors.topMargin: 4;
            font.pixelSize: 16;
        }
        Text {
            id: artist;
            anchors.top: filename.bottom
            anchors.leftMargin: 4;
            font.pixelSize: 16;
        }
        Text {
            id: album;
            anchors.top: artist.bottom;
            anchors.leftMargin: 4;
            font.pixelSize: 16;
        }
        Text {
            id: title;
            anchors.top: album.bottom;
            anchors.leftMargin: 4;
            font.pixelSize: 16;
        }
    }

    Rectangle {
        id: area1
        anchors.top: text_area.bottom
        width: parent.width; height: 120; //parent.height

        Image{
            id: img0
        }

        Image {
            id: img1
            anchors.left: img0.right
        }
    }

    Flipable {
        id: flipable
        x: 20; //y: 100
        anchors.top: area1.bottom
        width: 500; height: 500
        visible: false;

        property bool flipped: false

        front: Image {
            id: front_img
            source: prev_img;
            anchors.centerIn: parent;
            width: 500; height: 500
        }
        back: Image {
            id: back_img
            source: next_img;
            anchors.centerIn: parent;
            width: 500; height: 500
        }
        transform: Rotation {
            id: rotation
            origin.x: flipable.width/2
            origin.y: flipable.height/2
            axis.x: 0; axis.y: 1; axis.z: 0     // set axis.y to 1 to rotate around y-axis
            angle: 0    // the default angle
        }
        states: State {
            name: "back"
            PropertyChanges { target: rotation; angle: 180 }
            when: flipable.flipped
        }
        transitions: Transition {
            NumberAnimation { target: rotation; property: "angle"; duration: 3000 }
        }
        MouseArea {
            anchors.fill: parent
            onClicked: flipable.flipped = !flipable.flipped
        }
    }

}
