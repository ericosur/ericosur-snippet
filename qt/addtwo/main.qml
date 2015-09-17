import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

import com.pega.rasmus 1.0

ApplicationWindow {
    id: mainwindow
    title: qsTr("Hello World") + trs.empty
    width: 640
    height: 480
    visible: true

    MyTranslation {
        id: trs;
    }

    // between min (inclusive) and max (exclusive)
    function getRandom(min, max)  {
        return Math.random() * (max - min) + min;
    }

    // not good
    function getRandomCeil(min, max)  {
        return Math.ceil(Math.random() * (max - min)) + min - 1;
    }

    function myAdd(x, y) {
        return x+y;
    }

    Image {
        id: bgm
        anchors.fill: parent
        source: "/image/1.png"
        z: 10
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("clicked");
                main_form.visible = true;
                bgm.visible = false;
            }
        }
    }

    MainForm {
        id: main_form
        anchors.fill: parent
        visible: false
        z: 1
        function myInit() {
            textInput1.text = getRandomCeil(1, 9999);
            textInput2.text = getRandomCeil(1, 9999);
        }

        Component.onCompleted: {
            myInit();
            // show system locale name at title
            textArea1.append('system locale: ' + Qt.locale().name);
        }

        buttonInit.onClicked: {
            myInit();
            textArea1.append(qsTr("lorem"))
        }


        comboLang.onCurrentIndexChanged: {
            if (comboLang.currentText) {
                //textArea1.append(comboBox1.currentText + comboBox1.currentIndex.toString());
                //textArea1.append(comboBox1.model.get(comboBox1.currentIndex).loc);
                //textArea1.append(comboBox1.model.get(0).loc);  // if access via 'var'
                trs.selectLanguage( comboLang.model.get(comboLang.currentIndex).loc );
                //messageDialog.show('set to ' + comboBox1.currentText, qsTr("May I have your attention, please?"));
                textArea1.append(qsTr("May I have your attention, please?"));

                comboAction.currentIndex = -1;
                //comboAction.currentText = "";

            }
        }

        comboAction.onCurrentIndexChanged: {

            comboAction.model.set(0, {"Text": qsTr("n/a")});
            comboAction.model.set(1, {"Text": qsTr("Add")});
            comboAction.model.set(4, {"Text": qsTr("clear")});

            if (comboAction.currentIndex == 4) {
                textArea1.remove(0, textArea1.length);
            } else if (comboAction.currentIndex != 0) {
                var val1 = parseInt(textInput1.text);
                var val2 = parseInt(textInput2.text);
                var str;
                var res;
                if (comboAction.currentIndex == 1) {
                    str = textInput1.text + '+' + textInput2.text;
                    res = myAdd(val1, val2);
                } else if (comboAction.currentIndex == 2) {
                    str = val1 + '* sin(' + val2 + ')';
                    res = val1 * Math.sin(val2);
                } else if (comboAction.currentIndex == 3) {
                    str = val1 + '/ cos(' + val2 + ')';
                    res = val2 / Math.cos(val2);
                }
                textArea1.append(str);
                textArea1.append(res);
            }
        }

        btnFullscreen.onClicked: {
            mainwindow.visibility = Window.FullScreen
        }

        btnNormal.onClicked: {
            mainwindow.visibility = Window.Windowed
        }

    }

    MessageDialog {
        id: messageDialog
        //title: 'title'

        function show(inn, cap) {
            messageDialog.text = inn;
            messageDialog.title = cap;
            messageDialog.open();
        }
    }
}
