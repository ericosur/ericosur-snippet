// http://stackoverflow.com/questions/6831918/node-js-read-a-text-file-into-an-array-each-line-an-item-in-the-array
var fs = require('fs');
var fname = process.argv[2];
var lines = fs.readFileSync(fname).toString().split('\n');

// no need toString() if using 'utf8' encoding specified
// var utf8lines = fs.readFileSync(fname, 'utf8').split('\n');

/*
for (i in lines)  {
    console.log(lines[i]);
}
*/
console.log(lines.length-1);
