/*
   seeif.c: to see value stored in memory is big endian or little endian
*/
#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <stdlib.h>

#include <time.h>

#define STRLEN 10

int main()
{
    int v = 0xdeadbeef;
    unsigned char s[STRLEN] = {0};
    int i;

    memcpy(s, &v, sizeof(v));
    for (i=0; i<sizeof(v); i++) {
        printf("%02x ", s[i]);
    }
    printf("\n");

    unsigned char s2[] = {0xef, 0xbe, 0xad, 0xde};
    memcpy(&v, s2, 4);
    printf("v = %x\n", v);

    //time_t t;
    printf("sizeof(time_t) = %d\n", sizeof(time_t));
    // should be same as "date +%s"
    printf("time: %ld\n", (long)time(NULL));

    return 0;
}
