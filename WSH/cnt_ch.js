/*
�Q�� regex pattern
*/
function chineseCount(word){
    return word.split(/[\u4e00-\u9fa5]/).length - 1;
}

var word="test��asd��asd�ras�쩳asd���Xasd��?";
//alert(chineseCount(word));
print(chineseCount(word));
