/// fisher-yates shuffle

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

#define MAXDIGITS   10

FILE *fp[MAXDIGITS];

// prepare ten logs for each digits
void init_outputfiles()
{
    char outfn[64];

    memset(outfn, 0, sizeof(outfn)/sizeof(char));
    for (int i=0; i<MAXDIGITS; i++) {
        sprintf(outfn, "fisher%02d.log", i);
        fp[i] = fopen(outfn, "a");
        if (fp[i] == NULL) {
            perror("open file error");
            return;
        }
    }
}

// first digit goes to fisher00.log, and etc...
void output_file(int* arr, size_t array_size)
{
    for (int i=0; i<array_size; i++)  {
        fprintf(fp[i], "%d\n", arr[i]);
    }
}

void close_files()
{
    for (int i=0; i<MAXDIGITS; i++)  {
        fclose(fp[i]);
    }
}

void lisa_shuffle_array(int* arr, size_t array_size)
{
    size_t n = array_size;
    size_t r;
    for (int i = 0; i < n; i ++)  {
        r = rand() % n;
        int t = arr[i];
        arr[i] = arr[r];
        arr[r] = t;
    }
}

// perform fisher-yates shuffle
void fisher_shuffle_array(int* arr, size_t array_size)
{
    size_t n = array_size;
    size_t r;
    while (n > 1)  {
        r = rand() % n;
        if (r >= n) {
            perror("out of bound");
            return;
        }
        n = n - 1;
        int t = arr[n];
        arr[n] = arr[r];
        arr[r] = t;
    }
}

void fill_array(int* arr, size_t max_size = MAXDIGITS)
{
    for (size_t i = 0; i < max_size; ++i)  {
        arr[i] = i;
    }
}

void show_array(int* arr, size_t array_size)
{
    for (size_t i = 0; i < array_size; ++i)  {
        printf("%d ", arr[i]);
    }
    printf("\n");
}


void test()
{
    const size_t REPEAT_TRY = 1000000;
    const size_t ARRAYSIZE = MAXDIGITS;

#define shuffle_array(x, y) fisher_shuffle_array(x, y)

    srand(time(NULL));
    int* ary = (int*)malloc(ARRAYSIZE*sizeof(int));
    for (size_t ii=0; ii<REPEAT_TRY; ++ii) {
        fill_array(ary, ARRAYSIZE);
        //show_array(ary, ARRAYSIZE);
        shuffle_array(ary, ARRAYSIZE);
        if (ii < 80) {
            show_array(ary, ARRAYSIZE);
        }
        output_file(ary, ARRAYSIZE);
    }
#undef shuffle_array
}

int main()
{
    init_outputfiles();
    test();
    close_files();

    return 0;
}
