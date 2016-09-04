/** \file testmemset.cpp
	\brief benchmark for memset()
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/// test buffer size is 100MB
#define TEST_BUFFER_SIZE    (100*1024*1024)
#define MAX_REPEAT			100

#ifdef USE_WAIT
#define WAIT_FOREVER() \
	printf("wait here...\n");
	while (1) { (void)0; }
#else
#define WAIT_FOREVER()
#endif

char srcbuffer[TEST_BUFFER_SIZE];
char dstbuffer[TEST_BUFFER_SIZE];

void test()
{
	for (int i = 0; i < MAX_REPEAT; i++) {
		memcpy(dstbuffer, srcbuffer, sizeof(dstbuffer));	
	}
}

int main()
{
    test();
    WAIT_FOREVER();
    return 0;
}
