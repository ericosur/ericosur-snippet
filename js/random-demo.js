// example code from
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
// http://blog.tompawlak.org/how-to-generate-random-values-nodejs-javascript
// http://liaosankai.pixnet.net/blog/post/19382531-%E4%BA%82%E6%95%B8-javascript-math.random()

// between 0 (inclusive) and 1 (exclusive)
function getRandom()  {
    return Math.random();
}

// between min (inclusive) and max (exclusive)
function getRandomArbitrary(min, max)  {
    return Math.random() * (max - min) + min;
}

// between min (included) and max (excluded)
// using Math.round() will give you a non-uniform distribution
function getRandomint(min, max)  {
    return Math.floor(Math.random() * (max - min)) + min;
}

// not good
function getRandomCeil(min, max)  {
    return Math.ceil(Math.random() * (max - min)) + min - 1;
}

// not good
function getRandomRound(min, max)  {
    return Math.round(Math.random() * (max - min)) + min;
}

/*
console.log(getRandom())
console.log(getRandomArbitrary(1, 10))
console.log(getRandomint(1, 10))
*/

function empty(v)  {
    for (var i=0; i<v.length; i++)  {
        v[i] = 0;
    }
}

function show(v)  {
    for (var i=0; i<v.length; i++) {
        console.log(i+": "+ v[i]/n);
    }
}

var n = 100000;
var size = 11;
var p = new Array(size);
var q = new Array(size);
var r = new Array(size);
//console.log(v.length);

empty(p);
for (var i=0; i<n; i++)  {
    p[getRandomint(0,10)] += 1;
}
console.log('random int by floor');
show(p);

empty(q);
for (var i=0; i<n; i++)  {
    q[getRandomCeil(0, 10)] += 1;
}
console.log('random int by ceiling');
show(q);

empty(r);
for (var i=0; i<n; i++)  {
    r[getRandomRound(0, 10)] += 1;
}
console.log("random int by round");
show(r);


