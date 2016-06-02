// script to calculate black friday
const THIRTEEN = 13;   // black
const FRIDAY = 5;     // Friday
const RANGE = 5;

var thisYear = (new Date()).getFullYear();
var y_start = thisYear - RANGE;
var y_end = thisYear + RANGE;

var testDay = new Date();
var bfdates = [];

for (var i=y_start; i<=y_end; i++)  {
    for (var j=0; j<12; j++)  {
        testDay.setYear(i);
        testDay.setMonth(j);
        testDay.setDate(THIRTEEN);
        if ( testDay.getDay() == FRIDAY )  {
            bfdates.push(j+1);
            //console.log(testDay, "is black Friday");
        }
    }
    console.log('year', testDay.getFullYear(), 'has', bfdates.length, 'BF', bfdates);
    bfdates = [];
}
