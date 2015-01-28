var cnt = 0;
var testDay = new Date();
var y_start = 2015;
var y_end = 2050;
for (var i=y_start; i<=y_end; i++)  {
    for (var j=0; j<12; j++)  {
        testDay.setYear(i);
        testDay.setMonth(j);
        testDay.setDate(13);
        if ( testDay.getDay() == 5 )  {
            //console.log(testDay, "is black Friday");
            cnt ++;
        }
    }
    console.log('year', testDay.getFullYear(), 'has', cnt, 'BF');
    cnt = 0;
}
