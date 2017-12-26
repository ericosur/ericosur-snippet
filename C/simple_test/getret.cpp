#include <stdio.h>
#include <stdlib.h>

// stupid test to get ret from system()

int main()
{
    printf("start a bash shell, use 'exit'\n");
    int ret = system("/bin/bash");
    printf("ret:%d\n", ret);
    return 0;
}
