function gcd(x, y) {
    if (y == 0) {
        return x;
    }
    return gcd(y, (x%y));
}

var m = 1920;
var n = 1080;
var g = gcd(m, n);
console.log('gcd (', m, ',', n, '): ', g);
console.log(m/g+ ':'+n/g);

