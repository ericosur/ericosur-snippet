import QtQuick 2.0

Canvas {
    width: 400; height: 200
    contextType: "2d"

    Path {
        id: myPath
        startX: 0; startY: 100

        PathCurve { x: 75; y: 75 }
        PathCurve { x: 200; y: 150 }
        PathCurve { x: 325; y: 25 }
        PathCurve { x: 400; y: 100 }
    }

    onPaint: {
        context.strokeStyle = Qt.rgba(.4,.6,.8);
        context.path = myPath;
        context.stroke();
    }
}
