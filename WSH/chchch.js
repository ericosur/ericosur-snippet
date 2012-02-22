function chineseCount(word){
    v=0
    for(cc=0;cc<word.length;cc++){
       c = word.charCodeAt(cc);
      if (!(c>=32&&c<=126)) v++;
    }
    return v;
}

var word="test中asd文asd字as到底asd有幾asd個?";
//alert(chineseCount(word));
print(chineseCount(word));
