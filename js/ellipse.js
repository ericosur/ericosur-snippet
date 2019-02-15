// for loop and sum up

function rad2deg(rad)
{
    return rad * 180.0 / Math.PI;
}

function deg2rad(deg)
{
    return deg * Math.PI / 180.0;
}

var limit = 360;

for (var i = 0; i < limit; i+=30) {

    console.log('ans = ' + i + ' ==> ' + Math.sin(deg2rad(i)))
}

