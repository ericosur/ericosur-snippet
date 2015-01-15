var p = require('path');
if ( p.extname(process.argv[1]) === '.js' )
    console.log('rocks');

var gg = require('./gcd');
console.log(gg.gcd(1280, 720));

gg.hello(5, 10, function(v) {
    console.log(v);
});

