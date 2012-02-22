#include <stdio.h>

void testMD5();
void testAES();

void show(unsigned char* buf, size_t len)
{
	for (size_t i=0; i<len; i++)
	{
		printf("%02x", buf[i]);
	}
	printf("\n");
}

int main()
{
	testMD5();

	testAES();	


	return 0;
}
