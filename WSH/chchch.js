function chineseCount(word){
    v=0
    for(cc=0;cc<word.length;cc++){
       c = word.charCodeAt(cc);
      if (!(c>=32&&c<=126)) v++;
    }
    return v;
}

var word="test��asd��asd�ras�쩳asd���Xasd��?";
//alert(chineseCount(word));
print(chineseCount(word));
