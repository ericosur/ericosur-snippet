// http://stackoverflow.com/questions/6831918/node-js-read-a-text-file-into-an-array-each-line-an-item-in-the-array
// use readFileSync()

var fs = require('fs');
var fname = process.argv[2];

if (fname) {
    var lines = fs.readFileSync(fname).toString().split('\n');

    // no need toString() if using 'utf8' encoding specified
    // var utf8lines = fs.readFileSync(fname, 'utf8').split('\n');

    /*
    // print out line by line
    for (i in lines)  {
        console.log(lines[i]);
    }
    */

    // how many lines
    var ln = lines.length - 1;
    console.log('lines: ' + ln.toString());
} else {
    console.log('please specify file name');
}
