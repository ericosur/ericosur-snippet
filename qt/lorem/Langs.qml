import QtQuick 2.5
//import QtQuick.Window 2.2
import com.rasmus 1.0

Item {
    //visible: true
    //width: 800
    //height: 600

    property int box_width: 120
    property int box_height: 60
    property int box_gap: 12
    property int box_fontsize: 18

    FontLoader {
        id: noto
        //C:\Windows\Fonts\NotoSans-Regular.ttf
        //source: "qrc:///NotoSans-Regular.ttf"
        //source: "https://fonts.googleapis.com/css?family=Noto+Sans"
        source: "qrc:///VC1.otf"
    }
    // FontLoader {
    //     id: kufi
    //     //source: "qrc:///NotoKufiArabic-Regular.ttf"
    //     source: "qrc:///VC1.otf"
    // }

    Rectangle {
        id: text_area
        anchors.top: rect1.bottom
        anchors.topMargin: 28
        anchors.left: rect1.left
        anchors.leftMargin: 12
        anchors.right: rect8.right
        anchors.rightMargin: 12
        //width: 500
        height: 500
        color: "transparent"
        border.color: "hotpink"; border.width: 2
        Text {
            id: text_area_text
            anchors.fill: parent
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignLeft
            font.pixelSize: box_fontsize
            text: mytext.message
            wrapMode: Text.WordWrap
            font.family: noto.name
        }
    }

    Rectangle {
        id: rect1
        width: box_width; height: box_height
        x: 10; y: 10
        color: "transparent"
        border.color: "blue"; border.width: 2
        Text {
            anchors.fill: parent
            text: "English"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect1");
                mytext.getTextWithId(LoadText.LangEn);
            }
        }
    }
    Rectangle {
        id: rect2
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect1.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "العربية"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect2");
                mytext.getTextWithId(LoadText.LangAr);
            }
        }
    }
    Rectangle {
        id: rect3
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect2.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "português"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect3");
                mytext.getTextWithId(LoadText.LangPt);
            }
        }
    }
    Rectangle {
        id: rect4
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect3.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "français"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect4");
                mytext.getTextWithId(LoadText.LangFr);
            }
        }
    }
    Rectangle {
        id: rect5
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect4.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "español"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect5");
                mytext.getTextWithId(LoadText.LangEs);
            }
        }
    }
    Rectangle {
        id: rect6
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect5.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "русский"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect6");
                mytext.getTextWithId(LoadText.LangRu);
            }
        }
    }
    Rectangle {
        id: rect7
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect6.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "український"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect7");
                mytext.getTextWithId(LoadText.LangUk);
            }
        }
    }
    Rectangle {
        id: rect8
        width: box_width; height: box_height
        anchors.top: rect1.top
        anchors.left: rect7.right
        anchors.leftMargin: box_gap
        color: "transparent"
        border.color: "black"; border.width: 2
        Text {
            anchors.fill: parent
            text: "Japanese"
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: box_fontsize
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("rect8");
                mytext.getTextWithId(LoadText.LangJa);
            }
        }
    }

}
