import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

ApplicationWindow {
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true
/*
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: messageDialog.show(qsTr("Open action triggered"));
            }
            MenuItem {
                text: qsTr("E&xit")
                onTriggered: Qt.quit();
            }
        }
    }
*/

    function myAdd(x, y) {
        return x+y;
    }

    MainForm {
        anchors.fill: parent

        button1.onClicked: {
            var val1 = parseInt(textInput1.text);
            var val2 = parseInt(textInput2.text);
            var str = textInput1.text + '+' + textInput2.text;
            textArea1.append(str);
            textArea1.append(myAdd(val1, val2));
        }

        button2.onClicked: {
            var val1 = parseInt(textInput1.text);
            var val2 = parseInt(textInput2.text);
            var str = val1 + '* sin(' + val2 + ')';
            textArea1.append(str);
            var res = val1 * Math.sin(val2);
            textArea1.append(res);
        }

        button3.onClicked: messageDialog.show(qsTr("Button 3 pressed"))
    }

    MessageDialog {
        id: messageDialog
        title: qsTr("May I have your attention, please?")

        function show(caption) {
            messageDialog.text = caption;
            messageDialog.open();
        }
    }
}
