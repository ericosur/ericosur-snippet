// script to calculate black friday
var tryThirteen = 13;   // black
var tryFriday = 5;     // Friday
var y_start = 2015;
var y_end = y_start + 20;

var testDay = new Date();
var bfdates = [];

for (var i=y_start; i<=y_end; i++)  {
    for (var j=0; j<12; j++)  {
        testDay.setYear(i);
        testDay.setMonth(j);
        testDay.setDate(tryThirteen);
        if ( testDay.getDay() == tryFriday )  {
            bfdates.push(j+1);
            //console.log(testDay, "is black Friday");
        }
    }
    console.log('year', testDay.getFullYear(), 'has', bfdates.length, 'BF', bfdates);
    bfdates = [];
}
