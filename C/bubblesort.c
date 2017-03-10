#include <stdio.h>

// dd if=/dev/urandom of=rand.dat bs=2048 count=400

#define BUFFERSIZE		4096
#define BUBBLESIZE		(BUFFERSIZE*25)
#define DATAFILE		"rand.dat"

typedef unsigned char byte;

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

int load_data(int val[], int n)
{
	FILE *fp = fopen(DATAFILE, "rb");
//	int buffer[BUFFERSIZE];
	size_t cnt = 0;

	if (fp == NULL) {
		fprintf(stderr, "cannot read file: %s\n", DATAFILE);
		return 0;
	}

	while ( cnt < n ) {
		size_t rr = fread(val+cnt, sizeof(int), BUFFERSIZE, fp);
		cnt += rr;
		//fprintf(stderr, "cnt: %d\n", (int)cnt);
	}

	fprintf(stderr, "read finished\n");
	fclose(fp);
	return 1;
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
	int vv[BUBBLESIZE];

	if ( load_data(vv, BUBBLESIZE) ) {
		//show(vv, BUBBLESIZE);
		bubblesort(vv, BUBBLESIZE);
		fprintf(stderr, "sort complete\n");
		//show(vv, BUBBLESIZE);
	}

	return 0;
}
