/// main.cpp

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#include "toolbox.h"

void test(byte r)
{
    const size_t BUFFER_SIZE = 1024 * 500;

    byte buffer[BUFFER_SIZE];
    byte md[MD5_DIGEST_LENGTH];

    memset(md, 0, MD5_DIGEST_LENGTH);
    memset(buffer, r, BUFFER_SIZE);
    CalculateBufferMD5(buffer, BUFFER_SIZE, md);
}

int main()
{
    const int repeat = 200000;
    for (int i = 0; i<repeat; i++) {
        byte r = (byte)(i % 255);
        test(r);
    }

    return 0;
}
