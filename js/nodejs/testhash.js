// sample code from api doc

function calcHash(fn)  {
    var crypto = require('crypto');
    var fs = require('fs');
    var shasum = crypto.createHash('sha1');
    var s = fs.ReadStream(fn);
    s.on('data', function(d) {
        shasum.update(d);
    });

    s.on('end', function() {
        var d = shasum.digest('hex');
        console.log(d + '  ' + fn);
    });
}

(function()  {
    if (process.argv.length <= 2) {
        console.log("please specify files to calculate hash...");
        return;
    }
    process.argv.forEach(function (val, index, array) {
        if (index >= 2) {
            //console.log(index + ': ' + val);
            calcHash(val);
        }
    });
})();
