#include "loadutil.h"

#include <stdio.h>

#define BUFFERSIZE      4096
#define DATAFILE        "rand.dat"

int load_data(int val[], int n)
{
    FILE *fp = fopen(DATAFILE, "rb");
//  int buffer[BUFFERSIZE];
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
