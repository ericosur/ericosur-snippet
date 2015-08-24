import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2
import Qt.labs.folderlistmodel 2.1
import QtMultimedia 5.0


ApplicationWindow {
    id:root
    title: qsTr("Hello World")
    width: 640+400
    height: 480+100
    visible: true

    property alias folder: folderModel.folder;
    property string audioSrc;
    property int index : -1;
    property int foldercount: folderModel.count;
    property bool repeat : false;
    property bool shuffle_on : false;
    property bool next_or_prev : false;
    property int index_prev : index-1;
    property int index_next : index+1;


    property var playbackstate : audio.playbackState;

    onIndex_prevChanged: {
        //if (repeat)
    }

    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }

    function setplaylist(){
        //foldercount = folderModel.count;
        for (var i =0;i <=foldercount-1 ;i++){
            console.log("setplaylist");
            playlist.append({ "url": folderModel.get(i,"fileURL")});
        }
    }

    function getlistlog(){
        for (var i =0;i <=foldercount-1 ;i++){
            console.log("get_playlist",playlist.get(i).url);
        }
        var buffercount = bufferlist.count;
        for (var i =0;i <=buffercount-1 ;i++){
            console.log("get_bufferlist",bufferlist.get(i).index_play);
        }
        for (var i =0;i <=foldercount-1 ;i++){
            console.log("get_shufflelist",playlist_shuffle.get(i).index_play);
        }
        console.log("list count ="+playlist.count);
    }

    function shuffle(){
        playlist_shuffle.clear();

        foldercount = playlist.count;
        for (var i =0; i <= foldercount-1;i++){
            bufferlist.append({ "index_play": i});
            console.log("1_bufferlist_count",bufferlist.count);
        }

        for (var j = 0; j <= foldercount-1; j++){
            var buffercount =  bufferlist.count;
            console.log("2_bufferlist_count", bufferlist.count);
            var R = getRandomInt(0,buffercount-1);
            playlist_shuffle.append({ "index_play": bufferlist.get(R).index_play});
            bufferlist.remove(R);
        }
    }

    function goNext(){
       next_or_prev = true;
       if (repeat && index == foldercount - 1) {
           index = 0;
       } else {
           index += 1;
       }
       next_or_prev = false;
    }

    function goPrev() {
        next_or_prev = true;
        if (repeat && index == 0) {
            index = foldercount - 1;
        } else {
            index -= 1;
        }
        next_or_prev = false;
   }

    onFolderChanged: {
        playlist.clear();
        setplaylist();
    }

    onPlaybackstateChanged:{
        console.log("next_or_prev = "+next_or_prev);
        if (next_or_prev){
            return;
        }

        if (repeat) {
            console.log("repeat");
            if(index = foldercount){
                index =0;
            }else{
                index += 1;
            }
        }
    }

    function play(index) {
        audio.stop()
        audioSrc = playlist.get(index).url;
        audio.play();
    }

    function playShuffle(index) {
        audio.stop()
        var index_playlist = playlist_shuffle.get(index).index_play;
        audioSrc = playlist.get(index_playlist).url;
        audio.play();
    }

    onIndexChanged:{
        if (shuffle_on){
            root.playShuffle(index);
        }
        else{
            root.play(index);
        }
    }


    FileDialog {
        id: fileDialog
        title: "Choose a folder with some images"
        selectFolder: true
        //visible: true
        onAccepted: {
            folderModel.folder = fileUrl + "/";
        }
    }

    Audio {
        id: audio
        source: audioSrc
    }

    FolderListModel {
       id: folderModel
        objectName: "folderModel"
        showDirs: true
        nameFilters: ["*.mp3"]
        folder:"file:///home/south/playlist_0819/mp3"
        showDirsFirst: true
    }

    ListModel {
        id: playlist
        objectName: playlist
        dynamicRoles:true
    }

    ListModel {
        id: bufferlist
        objectName: bufferlist
        dynamicRoles:true
    }

    ListModel {
        id: playlist_shuffle
        objectName: playlist_shuffle
        dynamicRoles:true
    }

    Image {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.margins: 10
        source: "back.png"
        MouseArea {
            anchors.rightMargin: -12
            anchors.bottomMargin: 0
            anchors.leftMargin: -8
            anchors.topMargin: -20
            anchors.fill: parent
            anchors.margins: -10
            onClicked: {
                console.log("count of list numbers = "+folderModel.count);
                console.log("list location = "+folderModel.folder);
                //console.log("fileUri = "+folderModel.get(1,"fileURL"));
                console.log("getRandomInt ="+getRandomInt(0,100));
                console.log("audio.playbackState ="+audio.playbackState);
                getlistlog();
            }
        }

        Item {
            id: next
            x: 514
            y: 410
            width: 155
            height: 129
            MouseArea {
                anchors.fill:parent
                onClicked: {
                root.goNext();
                }
            }
        }

        Item {
            id: play
            x: 355
            y: 410
            width: 148
            height: 140
            MouseArea {
                anchors.fill:parent
                onClicked: {
                   index = 0;
                   //audioSrc = folderModel.get(0,"fileURL")
                   audioSrc = playlist.get(0).url
                   audio.play();
                   foldercount = folderModel.count;
                   //setplaylist();
                }
            }
        }

        Item {
            id: prev
            x: 208
            y: 410
            width: 135
            height: 140
            MouseArea {
                anchors.fill:parent
                onClicked: {
                   root.goPrev();
                }
            }
        }

        Item {
            id: repeat_item
            x: 675
            y: 413
            width: 147
            height: 132
            MouseArea {
                anchors.rightMargin: 8
                anchors.bottomMargin: 29
                anchors.leftMargin: -8
                anchors.topMargin: -19
                anchors.fill:parent
                onClicked: {
                    repeat = true;
                }
            }
        }

        Item {
            id: random
            x: 827
            y: 404
            width: 164
            height: 127
            MouseArea {
                anchors.fill:parent
                onClicked: {
                    shuffle_on = true;
                    root.shuffle();
                }
            }
        }
    }

    Button{
           width:30
           height:30
           onClicked: {
               fileDialog.open();
           }
           Image{
               source: "folder.png"
           }
     }

}




