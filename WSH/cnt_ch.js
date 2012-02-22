/*
利用 regex pattern
*/
function chineseCount(word){
    return word.split(/[\u4e00-\u9fa5]/).length - 1;
}

var word="test中asd文asd字as到底asd有幾asd個?";
//alert(chineseCount(word));
print(chineseCount(word));
