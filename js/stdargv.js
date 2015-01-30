// http://stackoverflow.com/questions/4351521/how-to-pass-command-line-arguments-to-node-js
// process argv without library

// print process.argv
process.argv.forEach(function (val, index, array) {
    console.log(index + ': ' + val);
});
