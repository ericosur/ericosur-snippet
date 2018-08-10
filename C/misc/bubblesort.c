#include "loadutil.h"
#include <stdio.h>

// dd if=/dev/urandom of=rand.dat bs=2048 count=400

#define BUBBLESIZE		(BUFFERSIZE*25)

void bubblesort(int val[], int n)
{
	int i, j, tmp;

	for (i=0; i<(n-1); i++)  {
	    for (j=0; j<(n-i-1); j++)  {
	        if ( val[j] > val[j+1] ) {
	            tmp = val[j];
	            val[j] = val[j+1];
	            val[j+1] = tmp;
	        }
	    }
	}
}

int main()
{
	int vv[BUBBLESIZE];

	if ( load_data(vv, BUBBLESIZE) ) {
		//show(vv, BUBBLESIZE);
		bubblesort(vv, BUBBLESIZE);
		fprintf(stderr, "sort complete\n");
		//show(vv, BUBBLESIZE);
	}

	return 0;
}
