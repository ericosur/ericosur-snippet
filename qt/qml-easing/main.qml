import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2

ApplicationWindow {
    title: qsTr("Hello World")
    width: 800
    height: 800
    visible: true

    Item {
        Rectangle {
            id: re1;
            width: 80; height: 80
            x: 40; y: 20;
            color: "green"
            //Behavior on x { PropertyAnimation { properties: "x"; easing.type: Easing.Linear } }
            PropertyAnimation {
                properties: "y"; easing.type: Easing.InOutQuad
            }
        }
        /*
        Component.onCompleted: {
            //re1.x = 400;
            re1.y = 800;
        }
        */
    }
}
