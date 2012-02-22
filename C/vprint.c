#include <stdio.h>
#include <stdarg.h>

void mytrace(char* format, ...)
{
	va_list argptr;
	va_start(argptr, format);
	vprintf(format, argptr);
	va_end(argptr);
}

int main()
{
	mytrace("%d", 5);
	return 0;
}

