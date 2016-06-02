/// yql.js

var YQL = require('yql');

// 'select * from weather.forecast where (location = 94089)'
// 'select item.condition from weather.forecast where woeid = 2487889'
var query = new YQL('select item.condition from weather.forecast where woeid = 2487889');

query.exec(function(err, data) {

	console.log(data);
	var ch = data.query.results.channel;
	console.log(ch);
	// var location = data.query.results.channel.location;
	// var condition = data.query.results.channel.item.condition;

	// console.log('The current weather in ' + location.city + ', '
	// 	+ location.region + ' is ' + condition.temp + ' degrees.');
});
