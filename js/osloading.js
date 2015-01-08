// cpu usage
var os = require('os');

var printCPULoad = function() {
	var load = os.loadavg();
	var message = "1 min: %" + Math.floor(load[0]*100) +
		"5 min: %" + Math.floor(load[1]*100) +
		"15 min: %" + Math.floor(load[2]*100);
	console.log(message);
}

var printMemLoad = function() {
	var freemem = os.freemem();
	var totalmem = os.totalmem();
	var message = "Free Mem: " + Math.floor(freemem/1000000000) +
		" Total Mem: " + Math.floor(totalmem/1000000000);
	console.log(message);
}

printCPULoad();
printMemLoad();

