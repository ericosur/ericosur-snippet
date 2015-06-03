// simple module js that exports one function

var fs = require('fs');
var p = require('path');

module.exports = function(dir, ext, callback) {
    ext = '.' + ext

    fs.readdir(dir, function(err,data) {
        if (err)
            return callback(err);

        var newArray = data.filter(function(elem, index, array) {
            return (p.extname(elem) === ext);
        });

        callback(null,newArray);
    });
}
