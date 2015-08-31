import QtQuick 2.4
import QtQuick.Window 2.2
import QtQuick.Controls 1.3

// Custom types of C++
import com.pega.rasmus.ID3TAG 1.0

ApplicationWindow {
    width : 600; height: 750
    title: "main window"
    id: root;
    visible: true

    property string prev_img;
    property string next_img;
    property var fn_num: 0;

    // remember appending trailing slash '/' at the end of media_path
    //property var media_path: "/home/ericosur/Music/yoseui/";          // for ubuntu
    property var media_path: "/Users/ericosur/Downloads/go/testmp3/";   // for mac

    function myloadmp3(fn, img) {
        var res = id3tag.getMetaData(fn);

        filename.text = id3tag.filename;
        title.text = 'title: ' + id3tag.title;
        artist.text = 'artist: ' + id3tag.artist;
        album.text = 'album: ' + id3tag.album;
        //img.source = "file://" + id3tag.coverpath;
        //img.width = 100;
        //img.height = 100;
        img.source = "image://myprovider/" + fn;
        if (res) {
            return id3tag.coverpath;
        } else {
            console.log("myloadmp3(): getMetaData() failed")
        }
    }

    // return a number between 0 to 6
    function get_next_num() {
        if (fn_num >= 6) {
            fn_num = 0;
        } else {
            fn_num = fn_num + 1;
        }
        return fn_num;
    }

    // C++ class id3tag
    ID3TAG {
        id: id3tag
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
                var fn = media_path + "02.mp3";
                myloadmp3(fn, front_img);
                //front_img.source = "image://myprovider/" + fn;
                //console.log(prev_img);

                fn = media_path + "05.mp3";
                myloadmp3(fn, back_img);
                //back_img.source = "image://myprovider/" + fn;
                //console.log(next_img);

                flipable.visible = true;
                flipable.flipped = !flipable.flipped;
            }
        }

        Button {
            id: second;
            text: "cycle";
            anchors.left: start.right;
            anchors.leftMargin: 4;
            anchors.bottom: parent.bottom;
            anchors.bottomMargin: 4;
            onClicked: {
                // try to load 0[1-6].mp3, NOTE: some file is not existed
                var new_num = get_next_num();
                var fn = media_path + '0' + new_num + '.mp3';
                //console.log('button: fn: ' + fn);
                if (new_num % 2 == 0) {
                    myloadmp3(fn, img1);
                } else {
                    myloadmp3(fn, img0);
                }
            }
        }

        Button {
            id: quit;
            text: "Quit";
            anchors.left: second.right
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
        width: parent.width; height: 110; //parent.height

        Image{
            id: img0
            width: 100; height: 100;
        }

        Image {
            id: img1
            width: 100; height: 100;
            anchors.left: img0.right
        }
    }

    Flipable {
        id: flipable
        x: 20; //y: 100
        anchors.top: area1.bottom
        width: 420; height: 420
        visible: false;

        property bool flipped: false

        front: Image {
            id: front_img
            source: ""
            anchors.centerIn: parent;
            width: 400; height: 400
        }
        back: Image {
            id: back_img
            source: ""
            anchors.centerIn: parent;
            width: 400; height: 400
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
