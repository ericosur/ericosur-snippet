/// os.networkInterfaces()
const os = require("os");

var n = os.networkInterfaces();

if ( n["eth0"] ) {
	console.log("eth0: ");
	console.log( n["eth0"]["0"]["address"] );
	console.log( n["eth0"]["0"]["mac"] );
}
if ( n["wlan0"] ) {
	console.log("wlan0: ");
	console.log( n["wlan0"]["0"]["address"] );
	console.log( n["wlan0"]["0"]["mac"] );
}

// demo how to get keys in js objects
var keys = Object.keys(n);
console.log(keys);
