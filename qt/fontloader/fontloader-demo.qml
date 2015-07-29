//
// reference: http://stackoverflow.com/questions/15046036/qml-fontloader-not-working
//

import QtQuick 2.0

Item {
    width: 680
    height: 400

    FontLoader {
        id: mincho;
        source: "mincho.otf"
    }

    FontLoader {
        id: notokufi;
        source: "notokufi.ttf"
    }

    FontLoader {
        id: hanamin
        source: "HanaMinB.ttf"
    }

    Text {
        id: text1
        anchors.top: parent.top
        font.pointSize: 24
        font.family: notokufi.name
        text: "وهذا هو أول مبنى مرتفع في العالم" + "\n" + font.family;
    }

    Text {
        id: text2
        anchors.top: text1.bottom
        anchors.margins: 10
        font.pointSize: 24
        font.family: mincho.name
        text: "私は菜食主義者です 小塚明朝\n" + mincho.name;
    }

    Text {
        id: text3
        anchors.top: text2.bottom
        font.pointSize: 24
        //font.family: mincho.name
        text: "𠁙𠁚𠀳𠁀𠁟 وهذا هو أول مبنى مرتفع في العالم" + "\n" + font.family;
    }

    Text {
        id: text4
        anchors.top: text3.bottom
        font.pointSize: 24
        font.family: hanamin.name
        text: "𠁙𠁚𠀳𠁀𠁟" + "\n" + font.family;
    }
}
