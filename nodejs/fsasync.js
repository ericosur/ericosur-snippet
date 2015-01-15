var fs = require('fs');
var fname = process.argv[2];
var lines = fs.readFile(fname, 'utf8', function(err,data) {
    if (err) {
        throw err;
    } else {
        var lines = data.split('\n');
        console.log(lines.length-1);
    }
});
