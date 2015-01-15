var fs = require('fs');
var path = require('path');
var dirname = process.argv[2];
var fileext = '.' + process.argv[3];

//console.log('dir: ' + dirname + ', ext: ' + fileext);
fs.readdir(dirname, function(err,data) {
    if (err) throw err;
    data.forEach(function(elem,index,array) {
        //console.log(elem);
        if (path.extname(elem) == fileext) {
            console.log(elem);
        }
    });
});
