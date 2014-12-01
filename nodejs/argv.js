//console.log(process.argv)
var sum = 0;
for (var i=2; i<process.argv.length; i++) {
    //console.log(i,process.argv[i]);
    sum = sum + Number(process.argv[i]);
}
console.log(sum);
