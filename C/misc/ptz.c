#define _GNU_SOURCE /* for tm_gmtoff and tm_zone */

#include <stdio.h>
#include <time.h>

/* Checking errors returned by system calls was omitted for the sake of readability. */
void print_timezone()
{
	time_t t = time(NULL);
	struct tm lt = {0};

	localtime_r(&t, &lt);
	int offset_hour = lt.tm_gmtoff / 3600;
	int offset_min = (lt.tm_gmtoff % 3600) / 60;
	printf("Offset to GMT is %lds.\n", lt.tm_gmtoff);
	printf("The time zone is '%s'.\n", lt.tm_zone);
	printf("%02d %02d\n", offset_hour, offset_min);

    // will same as "date +%s"
    printf("%d\n", (int)t);
}

int main()
{
	print_timezone();
	return 0;
}
