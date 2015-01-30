// simple demo to sum up argv

(function() {
    //console.log(process.argv)
    if (process.argv.length <= 2) {
        console.log("try: argv.js 1 2 3 4 ...");
        return;
    }

    var sum = 0;
    for (var i=2; i<process.argv.length; i++) {
        //console.log(i,process.argv[i]);
        sum = sum + Number(process.argv[i]);
    }
    console.log(sum);
})();
