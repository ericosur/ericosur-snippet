// demo how to use myfilter.js

var qq = require('./myfilter');

qq(process.argv[2], process.argv[3], function(err,data) {
    if (err) throw err;
    data.forEach(function(elem,index,array) {
        console.log(elem);
    });
});
