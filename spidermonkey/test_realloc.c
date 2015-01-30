// gcc -Wall -o test_relloc test_realloc.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char byte;

// try to simulate the behavior of realloc()
void dump(byte* buffer, size_t size)
{
    size_t i;
    char str[255];
    char tok[10];

    memset(str, 0, strlen(str));
    for (i = 0; i < size; i++)
    {
        sprintf(tok, "%02x ", (int)buffer[i]);
        strcat(str, tok);
    }

    strcat(str, "\n");
    printf("%s", str);

}

void* _jsrealloc(void* ptr, size_t size)
{
    void* new_ptr = NULL;

    if (ptr == NULL)
    {
        new_ptr = malloc(size);
        return new_ptr;
    }
    if (ptr && size == 0)
    {
        free(ptr);
        ptr = NULL;
        return NULL;
    }

    // allocate new buffer and release the old one
    new_ptr = malloc(size);
    memcpy(new_ptr, ptr, size);
    free(ptr);
    ptr = NULL;

    return new_ptr;
}

void test()
{
    const size_t init_size = 32;
    const size_t new_size = 64;
    const size_t try_count = 2;
    size_t i;
    byte* buf = NULL;

    for (i = 0; i < try_count; ++ i)
    {
        buf = (byte*)malloc(init_size);
        memset(buf, 0xcc, init_size);
        printf("1....\n");
        dump(buf, init_size);

        buf = (byte*)_jsrealloc(buf, new_size);
        printf("2....\n");
        dump(buf, new_size);
    }
}

int main()
{
    test();
    return 0;
}
