function shuffle(arr) {
    var n = arr.length;
    var r;
    while (n>1) {
        r = Math.floor(Math.random() * (n--));
        arr[n] = [arr[r], arr[r] = arr[n]][0];
    }
    return arr;
}

var arr = [1,2,3,4,5,6,7,8];
console.log(shuffle(arr));
