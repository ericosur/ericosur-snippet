import QtQuick 2.0

Item {
    width: 1280; height: 800

    property var startpx: 200
    property var startpy: 400
    property var startpw: 880
    property var startph: 200
    property var controlpx: startpx + startpw / 2
    property var controlpy: startpy  200

    Rectangle {
        x: startpx; y: startpy
        width: startpw; height: startph
        border.color: "hotpink"; border.width: 2
    }
    Rectangle {
        x: controlpx; y: controlpy
        width: 2; height: 100
        border.color: "lightgreen"; border.width: 2
    }
    Canvas {
        width: parent.width; height: parent.height
        contextType: "2d"

        Path {
            id: myPath
            startX: startpx; startY: startpy
            PathQuad { x: startpx+startpw; y: startpy;
                controlX: controlpx; controlY: controlpy
            }
        }

        onPaint: {
            context.strokeStyle = Qt.rgba(.4,.6,.8);
            context.path = myPath;
            context.stroke();
        }
    }
}
