#!/usr/bin/env node

/// get propery names from object
// http://stackoverflow.com/questions/2257993/how-to-display-all-methods-in-a-javascript-object

//console.log(Object.getOwnPropertyNames(Date));


var d = new Date();
for (bar in d) {
    console.log('property: ' + bar);
}

console.dir(d);
var n = Object.getOwnPropertyNames(d);
console.log('type: ' + typeof(n));
