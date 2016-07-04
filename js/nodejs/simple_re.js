#!/usr/bin/env node

// simple re test
var ar = ['apple', 'ball', 'cat', 'dog', 'egg', 'fish',
    'goat', 'hippo', 'ink', 'joker', 'king', 'limon',
    'moon', 'noodle'];
var re = /(.)\1/;

ar.forEach(function(elem, index, array) {
    if (elem.match(re)) {
        console.log(elem);
    }

});
