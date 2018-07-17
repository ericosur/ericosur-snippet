#include <stdio.h>
#include <math.h>

// calculate e by using basic definition
// but using limited iteration

double calcE()
{
    const int MIN = 10;
    const int MAX = 100000000;
    double v = 0.0;
    for (int i=MIN; i<=MAX; i++) {
        v = pow(1.0 + 1.0 / v, v);
        //printf("%.8f\r", v);
    }
    printf("%.8f\n", v);
	return v;
}

int main()
{
    double mye = calcE();
    printf("diff: %.8f\n", mye - exp(1.0));

    return 0;
}
