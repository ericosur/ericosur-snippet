/** \file testmemset.cpp
	\brief benchmark for memset()
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/// test buffer size is 100MB
#define TEST_BUFFER_SIZE    (100*1024*1024)
char testbuffer[TEST_BUFFER_SIZE];

void test()
{
    for (int b=0; b<=0xff; b++) {
        memset(testbuffer, b, TEST_BUFFER_SIZE);    
    }
}

int main()
{
    test();
    return 0;
}
