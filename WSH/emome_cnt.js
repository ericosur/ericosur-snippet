<script src="http://websms1.emome.net/sms//js/big5.js" type="text/javascript"></script>
function chineseCount(word){

    var v = 0;
    for(var i=0;i<word.length;i++){
      var c = word.charAt(i);
      var c2= word.charCodeAt(i);
      if(c2 > 0x7f) {
        tmp1 = false;
        for(var t=0;t<14832;t++) {
          if(c2==big5define[t]) {
            tmp1 = true;
            v++;
          }

        }
      }
    }
    return v;

}
var word="test中asd文asd字as到底asd有幾asd個?";
//alert(chineseCount(word));
print(chineseCount(word));