#!/usr/bin/env node

// node.js recipes
// analyzing types of data

var crypto = require('crypto'),
	hashes = crypto.getHashes();

hashes.forEach(function(hash) {
	['The quick brown fox jumps over the lazy dog.'].forEach(function(txt)  {
	var hashed;
	try {
		hashed = crypto.createHash(hash).update(txt).digest('hex');
	} catch (ex) {
		if (ex.message === 'Digest method not supported') {
			// not supported for this algo
			//console.log('not supported');
		} else {
			console.log(ex, hash);
		}
	}

	//console.log('\"' + hash + '\",\"' + hashed + '\"');
	console.log(hash + '\t' + hashed);
	});
});
	
