/// random_movies.js
/// 從清單內用亂數挑出一行
///
function main()  {
	var fs = require('fs');
	var fname = 'list.txt';
	var lines = fs.readFileSync(fname, 'utf8').split('\n');

	/*
	for (i in lines)  {
	    console.log(lines[i]);
	}
	*/
	var cnt_lines = lines.length-1;
	var rand_int = getRandomint(0,cnt_lines);
	//console.log(cnt_lines);
	//console.log(rand_int);
	console.log(lines[rand_int]);
}

// between min (included) and max (excluded)
// using Math.round() will give you a non-uniform distribution
function getRandomint(min, max)  {
    return Math.floor(Math.random() * (max - min)) + min;
}

main();
