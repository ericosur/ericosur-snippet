// sample code from api doc

function go(fn)  {
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

function main()  {
    var filename = process.argv[2];
    if (filename)  {
        go(filename);
    } else {
        console.log('please specify a file name');
    }
}

main();
