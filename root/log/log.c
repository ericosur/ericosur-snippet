/*
$ gcc -o lg log.c -lm
*/

#include <stdio.h>
#include <math.h>

void test()
{
    double vals[] = {1, 2.7182818284, 10, 100, 300};
    int i;

    for (i=0; i<5; i++)
    {
        printf("%.5f: %.5f -- %.5f\n", vals[i],
            log(vals[i]), log10(vals[i]));
    }
}

int main()
{
    test();
    return 0;
}
