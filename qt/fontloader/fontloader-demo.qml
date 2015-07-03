//
// reference: http://stackoverflow.com/questions/15046036/qml-fontloader-not-working
//

import QtQuick 2.0

Item {
    width: 680
    height: 400

    FontLoader {
        id: localFont;
        source: "mincho.otf"
    }

    Text {
        anchors.centerIn: parent
        font.pointSize: 64
        font.family: localFont.name
        text: "我能吞下玻璃\n而不受傷\n南下經三國 東風過四方\n" + localFont.name;
    }
}
