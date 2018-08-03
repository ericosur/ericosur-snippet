/*
reference: http://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3
 */

function isNull(value)
{
    if (value == null) {
        console.log("value == null");
    } else {
        console.log("value != null");
    }
}

function exactNull(value)
{
    if (value === null) {
        console.log("value === null");
    } else {
        console.log("value !== null");
    }
}

function isUndefined(value)
{
    if (value == undefined) {
        console.log("value == undefined");
    } else {
        console.log("value != undefined");
    }
}

function exactUndefined(value)
{
    if (value === undefined) {
        console.log("value === undefined");
    } else {
        console.log("value !== undefined");
    }
}

function isTruth(value)
{
    if (value) {
        console.log("value is true");
    } else {
        console.log("value is not true");
    }
}

function test(value)
{
    isNull(value);
    isUndefined(value);
    exactNull(value);
    exactUndefined(value);
    isTruth(value);
    console.log('typeof value: ' + typeof value);
    if (value) {
        console.log('value.length: ' + value.length);
    }

}

console.log("let m = null;");
let m = null;
test(m);

console.log("let n = undefined;");
let n = undefined;
test(n);

console.log('let s = ""');
let s = "";
test(s);

console.log('let s = "qwert"');
let s1 = "qwert";
test(s1);

console.log('let v = 0');
let v = 0;
test(v);

console.log('let w = 97');
let w = 97;
test(w);
