#include <stdio.h>
#include <unistd.h>
#include <utils/Log.h>

#define LOG_TAG	"ericosur"
#define REPEAT	100
#define BUF_LEN	100

int main()
{
	unsigned int cnt = 0;
	char msg[BUF_LEN];

	printf("stupid hello world build at %s %s\n", __DATE__, __TIME__);
	memset(msg, 0, BUF_LEN); 
	while (cnt < REPEAT)  {
		sprintf(msg, "(%d) hello, android", cnt);
		printf("%s\n", msg);
		LOGI(msg);
		sleep(1);
		cnt ++;
	}

	return 0;
}

