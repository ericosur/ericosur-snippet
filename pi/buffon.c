/**
 * buffon.c - Simulating Buffon's Needle Problem
 *
 * Authored by Jim Huang <jserv.tw@gmail.com>
 * Public Domain.  Runtime confirming to POSIX.1-2001.
 */

// gcc -O3 -Wall -o buffon buffon.c -lm

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <math.h>
#include <time.h>

void throw_needle(int trial);

int main( int argc, char **argv )
{
    int repeat = 100;
    int i, t;
    int trial = 10000000;

    for (t=1; t<3; t++)
    {
        printf("trial: %d\n", trial);
	    for (i=0; i<repeat; i++)
    	{
        	sleep(1);
        	throw_needle(trial);
    	}
        trial = trial * 10;
    }

    return 0;
}

void throw_needle(int trial)
{
	int i;
	int ntrial = trial; /* the largest prime number < 100000 */

	int crossing = 0;
	srand48( time( NULL ) );
	/*
	 * ----------------------------------------
	 * ||
	 * || 1
	 * ||                / ) Theta   ||x
	 * -----------------/----------------------
	 * x <= 1/2 * sin( Theta ), when needles cross a crack.
	 */
	for (i = 0; i < ntrial; i++) {
		double theta = M_PI * drand48(); /* 0 <= Theta <= PI */

		double x = drand48(); /* 0 <= x < 1 */
		if (x <= 0.5 * sin(theta))
			crossing++;
	}
//	printf("Needles dropped on floor = %8d \n", ntrial);
//	printf("Those that cross a crack = %8d \n", crossing);
//	printf("\tPI Estimate: ");
	printf("%0.5f \n", (double)ntrial / (double)crossing);
}
