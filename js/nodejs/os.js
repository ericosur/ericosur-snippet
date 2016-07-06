#!/usr/bin/env node

/// os.js
// https://nodejs.org/dist/latest-v6.x/docs/api/os.html#os_os_arch

function dump(myobj) {
	const util = require('util');
	//use util.inspect() to dump object
	console.log(util.inspect(myobj));
	//use JSON.stringify() to dump object
	//console.log(JSON.stringify(myobj, null, 2));
	// var keys = Object.keys(myobj);
	// console.log(keys);
}


(function() {
	const os = require('os');

	console.log('arch: ' + os.arch());
	console.log('free: ' + os.freemem());
	console.log('total: ' + os.totalmem());
	console.log( 'platform: ' + os.platform() );
	console.log( 'release: ' + os.release() );
	console.log( 'os type: ' + os.type() );
	console.log( 'uptime: ' + os.uptime() );

	console.log('os.cpus()');
	//dump(os.cpus());
	console.log(os.cpus());
})();
