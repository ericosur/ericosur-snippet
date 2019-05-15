#include <stdio.h>

/*
(d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7
 */

int dow(int y, int m, int d)
{
    return ((d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7);
}

int dow2(int y, int m, int d)
{
    d += m<3 ? y-- : y-2;
    return ((23*m/9+d+4+y/4-y/100+y/400)%7);
}


void show(int y, int m, int d)
{
    printf("dow of %d/%d/%d is %d\n", y, m, d, dow(y,m,d));
    printf("dow2 of %d/%d/%d is %d\n", y, m, d, dow2(y,m,d));
}

int main()
{
    show(2017, 6, 19);
    show(1975, 6, 17);

    //printf("value:%d\n", (2017,1953));
    return 0;
}
