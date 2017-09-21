#!/usr/bin/env node
/// yql.js


var sprintf
try {
     sprintf = require('sprintf').sprintf;
} catch (err) {
    console.log('require sprintf module, use \'npm install sprintf\'');
    return;
}

var MAXDAYS = 3;
var YQL = require('yql');

var city_name = 'Taipei';
var conditions = ['item.condition', 'astronomy'];
var condition_str = '*';

//where woeid in (select woeid from geo.places(1) where text='Taipei')
var wherestr = sprintf("where woeid in (select woeid from geo.places(1) where text =\'%s\') and u='c'", city_name);
var yqlstr = sprintf("select %s from weather.forecast ", condition_str);

var query_str = yqlstr + wherestr
do_query(query_str);

function do_query(query_str)
{
    // 'select * from weather.forecast where (location = 94089)'
    // 'select item.condition from weather.forecast where woeid = 2487889'
    var query = new YQL(query_str);

    query.exec(function(err, data) {
        print_out(data);
    });
}

function print_out(data)
{
    console.log("print_out....");
    console.log(data.query.results.channel.astronomy);
    console.log(data.query.results.channel.atmosphere);
    console.log(data.query.results.channel.item.condition);
    console.log("\nforecast in " + MAXDAYS + ' days');
    for (var i = 0; i < MAXDAYS; ++i) {
        console.log(data.query.results.channel.item.forecast[i]);
    }

}
