#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char str[128] = "0123456789abcdefghijklmnopqrstuvwxyz";
	int move_len = 2;
	int i;

	for (i = 0; i < 4; i++)
	{
		printf("%s\n", str);
		memmove(str, str + move_len, strlen(str) - move_len + 1);
	}

	return 0;
}
