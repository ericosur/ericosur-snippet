// nodejs recipes
// reviewing ciphers

var crypto = require('crypto');
var ciphers = crypto.getCiphers();
console.log(ciphers.join(', '));

