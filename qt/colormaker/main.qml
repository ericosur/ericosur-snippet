import QtQuick 2.4
import QtQuick.Window 2.2
import QtQuick.Controls 1.2

// Custom types of C++
import an.qt.ColorMaker 1.0
import com.pega.rasmus.ID3TAG 1.0

ApplicationWindow {
    width : 720; height: 480
    title: "main window"
    id: root;
    visible: true

    Rectangle {
        id: area0
        //anchors.fill: parent
        x: 0; y: 0;
        width: parent.width/2; height: parent.height;
        Text {
                id: timeLabel;
                anchors.left: parent.left;
                anchors.leftMargin: 4;
                anchors.top: parent.top;
                anchors.topMargin: 4;
                font.pixelSize: 18;
        }
        ColorMaker {
            id: colorMaker;
            //color: Qt.green;
        }
        Rectangle {
            id: colorRect
            //anchors.centerIn: parent;
            //anchors.horizontalCenter: parent;
            x: 40; y: 40;
            width: 40; height: 40;
            color: "blue";
        }
        Button {
            id: start;
            text: "start";
            anchors.left: parent.left;
            anchors.leftMargin: 4;
            anchors.bottom: parent.bottom;
            anchors.bottomMargin: 4;
            onClicked: {
                textarea1.append("Button start");
                colorMaker.start();
            }
        }
        Button {
            id: stop;
            text: "stop";
            anchors.left: start.right;
            anchors.leftMargin: 4;
            anchors.bottom: start.bottom;
            signal mySignal;
            onClicked: {
                colorMaker.stop();
            }
        }
        function changeAlgorithm(button, algorithm) {
            switch(algorithm) {
                case 0:
                    button.text = "RandomRGB";
                    break;
                case 1:
                    button.text = "RandomRed";
                    break;
                case 2:
                    button.text = "RandomGreen";
                    break;
                case 3:
                    button.text = "RandomBlue";
                    break;
                case 4:
                    button.text = "LinearIncrease";
                    break;
             }
        }
        Button {
            id: colorAlgorithm;
            text: "RandomRGB";
            anchors.left: stop.right;
            anchors.leftMargin: 4;
            anchors.bottom: start.bottom;
            onClicked: {
                var algorithm = (colorMaker.algorithm() + 1) % 5;
                parent.changeAlgorithm(colorAlgorithm, algorithm);
                colorMaker.setAlgorithm(algorithm);
            }
        }
        Button {
            id: quit;
            text: "Quit";
            anchors.left: colorAlgorithm.right;
            anchors.leftMargin: 4;
            anchors.bottom: start.bottom;
            onClicked: { Qt.quit(); }
        }
        ID3TAG {
            id: id3tag
        }
        Button {
            id: load
            text: "Load tag"
            anchors.left: quit.right
            anchors.leftMargin: 4;
            anchors.bottom: start.bottom;
            onClicked: {
                if ( id3tag.getMetaData("/Users/ericosur/Downloads/go/testmp3/01.mp3") ) {
                    textarea1.append(id3tag.filename);
                    textarea1.append(id3tag.title);
                    textarea1.append(id3tag.artist);
                    textarea1.append(id3tag.album);
                    img.source = "file:///Users/ericosur/Downloads/tmp.jpg";
                }
            }
        }

        signal mySignal;
        Component.onCompleted: {
            colorMaker.color = Qt.rgba(255, 0, 0, 255);
            colorMaker.setAlgorithm(colorMaker.LinearIncrease);
            changeAlgorithm(colorAlgorithm, colorMaker.algorithm());
            mySignal();
        }
        Connections {
            target: colorMaker;
            onCurrentTime: {
                timeLabel.text = strTime;
                timeLabel.color = colorMaker.timeColor;
            }
        }
        Connections {
            target: colorMaker;
            onColorChanged: {
                colorRect.color = color;
            }
        }

        TextArea {
            id: textarea1
            anchors.top: colorRect.bottom
            anchors.topMargin: 20
            anchors.bottom: start.top
            anchors.bottomMargin: 20
            width: parent.width
        }
    }

    Rectangle {
        id: area1
        anchors.left: area0.right
        width: parent.width/2; height: parent.height;
        Image{
            anchors.fill: parent
            id: img
        }

    }
}
