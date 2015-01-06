#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
    monte carlo method to get pi
*/

double pi(int n)
{
    int sum = 0;
    int i;

    srand48( time( NULL ) );
    for (i=0; i<n; i++)
    {
        double x = drand48();
        double y = drand48();
        if ((x*x + y*y) <= 1)
            sum ++;
    }
    return 4.0 * (double)sum / (double)n;
}

int main()
{
    int i;

    for (i=100; i<1000000000; i*=10)
    {
        printf("%-10d: %.8g\n", i, pi(i));
    }
    return 0;
}
