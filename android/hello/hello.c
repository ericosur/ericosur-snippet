#include <stdio.h>
#include <unistd.h>
#include <utils/Log.h>

#define LOG_TAG	"ericosur"
#define REPEAT	10

int main()
{
	unsigned int cnt = 0;

	printf("stupid hello world build at %s %s\n", __DATE__, __TIME__);
	while (cnt < REPEAT)  {
		ALOGI("***** [%d] hello android from CLI *****\n", cnt);
		sleep(1);
		cnt ++;
	}

	return 0;
}

