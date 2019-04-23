#include <stdio.h>
#include <string.h>
#include <stdarg.h>

int jsnprintf(char *out, size_t n, const char *format, ...);

int test(const char* str)
{
    const size_t BUFFERSIZE = 512;
    char buf[BUFFERSIZE];

    int res = jsnprintf(buf, BUFFERSIZE-1,
        "'name': %s", "事情'總'/沒/我\"想\\的\"簡單");
    if (res > 0) {
        printf("{\n%s\n}\n", buf);
    } else {
        printf("Fail\n");
    }

    return 0;
}

int main(int argc, char** argv)
{
    if (argc == 1) {
        test(argv[0]);
    } else {
        test(argv[1]);
    }
    return 0;
}
