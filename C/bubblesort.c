#include <stdio.h>

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

void show(int val[], int n)
{
	int i;

	for (i=0; i<n; i++) {
	    printf("%d  ", val[i]);
	}
	printf("\n");
}

int main()
{
	int vv[] = {43, 57, 97, 91, 79, 3, 11, 29, 73, 83, 91, 29};
	int nn = sizeof(vv)/sizeof(int);

	show(vv, nn);
	bubblesort(vv, nn);
	show(vv, nn);

	return 0;
}
