var cnt = 0;
var testDay = new Date();
for (var i=0; i<100; i++)  {
    for (var j=0; j<12; j++)  {
        testDay.setYear(2000+i);
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
