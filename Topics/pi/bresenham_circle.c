#include <stdio.h>

/*
from comment:
http://programmingpraxis.com/2009/10/09/calculating-pi/2/

Bresenham circle algorithm
45 degree angle ( pi/8 )
*/

double pi(int n)
{
    int f = 1 - n;
    int ddF_x = 1;
    int ddF_y = -2 * n;
    int x = 0;
    int y = n;
    long long int in = 0;
    while (x < y) {
        if (f >= 0) {
            --y;
            ddF_y += 2;
            f += ddF_y;
        }
        x++;
        ddF_x += 2;
        f += ddF_x;
        in += y - x;
    }
    return 8.0 * in / ((double)n * n);
}

int main()
{
    int i;

    for (i = 1; i <= 1000000000; i *= 10)
        printf("%10d: %.15g\n", i, pi(i));

    return 0;
}
