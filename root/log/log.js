
var sprintf
try {
     sprintf = require('sprintf').sprintf;
} catch (err) {
    console.log('require sprintf module, use \'npm install sprintf\'');
    return;
}

var vals = [1, 2.7182818284, 10, 100, 300];

vals.forEach(function(v) {
    var s = sprintf('%.5f: %.5f -- %.5f', v,
        Math.log(v, Math.e), Math.log(v, 10.0) );
    console.log(s);
});
