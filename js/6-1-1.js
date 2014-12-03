// node.js recipes
// hashes

var crypto = require('crypto'),
	hashes = crypto.getHashes();

console.log(hashes.join('\n'));

