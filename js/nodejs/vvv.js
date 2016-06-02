
(function() {
	var p = require('path');
	if ( p.extname(process.argv[1]) === '.js' )
	    console.log('js rocks');

	var gcd;
	try {
		gcd = require("./gcd");
	} catch (err) {
		console.log("cannot load module: gcd.js");
		return;
	}

	console.log(gcd.gcd(1280, 720));

	gcd.hello(5, 10, function(v) {
	    console.log(v);
	});

})();
