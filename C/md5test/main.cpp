/// main.cpp

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#include "toolbox.h"

#define BUFFER_SIZE     (1024 * 500)
#define DEFAULT_REPEAT  (20000)

byte buffer[BUFFER_SIZE];

void test(byte r)
{
    byte md[MD5_DIGEST_LENGTH];

    memset(md, 0, MD5_DIGEST_LENGTH);
    memset(buffer, r, BUFFER_SIZE);
    CalculateBufferMD5(buffer, BUFFER_SIZE, md);
}

int main(int argc, char** argv)
{
    int repeat = DEFAULT_REPEAT;
    if (argc > 1) {
        repeat = atoi(argv[1]);
    }
    fprintf(stderr, "will repeat md5sum %d times\n", repeat);
    for (int i = 0; i<repeat; i++) {
        if (i%1000 == 0) {
            fprintf(stderr, ".");
        }
        byte r = (byte)(i % 255);
        test(r);
    }
    fprintf(stderr, "\n");

    return 0;
}
