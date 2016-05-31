/// os.js
// https://nodejs.org/dist/latest-v6.x/docs/api/os.html#os_os_arch

const os = require('os');
const util = require('util');

console.log('arch: ' + os.arch());
console.log('free: ' + os.freemem());

console.log('os.cpus()');
console.log(os.cpus());
// use util.inspect() to dump object
//console.log('cpus: ' + util.inspect(os.cpus()));
// use JSON.stringify() to dump object
//console.log(JSON.stringify(os.cpus(), null, 2));

console.log('os.networkInterfaces()');
console.log( os.networkInterfaces() );

console.log( os.platform() );
console.log( os.release() );
console.log( os.type() );
console.log( os.uptime() );
