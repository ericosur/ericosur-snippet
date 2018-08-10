#include "loadutil.h"
#include <stdio.h>

// refer to https://en.wikipedia.org/wiki/Shellsort

// how to generate rand.dat
// dd if=/dev/urandom of=rand.dat bs=2048 count=400

#define VALSIZE     (BUFFERSIZE * 25)

int shellsort(int val[], int n)
{
    int gap, i, j;
    int temp;

    // Start with a big gap, then reduce the gap
    for (gap = n/2; gap > 0; gap /= 2)
    {
        // Do a gapped insertion sort for this gap size.
        // The first gap elements a[0..gap-1] are already in gapped order
        // keep adding one more element until the entire array is
        // gap sorted
        for (i = gap; i < n; i += 1)
        {
            // add a[i] to the elements that have been gap sorted
            // save a[i] in temp and make a hole at position i
            temp = val[i];

            // shift earlier gap-sorted elements up until the correct
            // location for a[i] is found
            for (j = i; j >= gap && val[j - gap] > temp; j -= gap)
                val[j] = val[j - gap];

            //  put temp (the original a[i]) in its correct location
            val[j] = temp;
        }
    }
    return 0;
}

int main()
{
    int vv[VALSIZE];

    if ( load_data(vv, VALSIZE) ) {
        //show(vv, VALSIZE);
        shellsort(vv, VALSIZE);
        fprintf(stderr, "sort complete\n");
        //show(vv, VALSIZE);
    }

    return 0;
}
