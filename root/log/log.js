// npm install mathjs
var math = require('mathjs');
// npm install sprintf
var sprintf = require('sprintf').sprintf;

var vals = [1, 2.7182818284, 10, 100, 300];

vals.forEach(function(v) {
    var s = sprintf('%.5f: %.5f -- %.5f', v,
        math.log(v, math.e), math.log(v, 10.0) );
    console.log(s);
});
