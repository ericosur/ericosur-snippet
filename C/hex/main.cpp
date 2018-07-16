#include "charutil.h"
#include <stdio.h>
#ifdef USE_GLIB
#include <gmodule.h>
#endif

#define STRING_LEN    20

class GenString
{
public:
    void fill_string(char* str);
private:
    int __start = 0xAE;
    int __end = 0xFF;
    int __char_in_row = 9;
    int __repeat = 0;
};

void GenString::fill_string(char* str)
{
    for (int i=0; i < __char_in_row; ++i) {
        str[i] = __start + __repeat * __char_in_row + i;
    }

    if (__repeat >= __char_in_row) {
        __repeat = 0;
    } else {
        __repeat ++;
    }
}


int main()
{
#if 0
    test0();
#else
    char str[STRING_LEN] = "C0c1C7cBD3d7DA";
    //printf("str:%s\n", str);

    size_t ba_size = strlen(str) / 2 + 1;
    char* ba = (char*)malloc(ba_size);
    bzero(ba, ba_size);

    size_t sz = 0;
    str2hex(str, ba, sz);
    //dump(ba, ba_size);

    size_t ret_sz;
    char* dst = iso88591_to_utf8(ba, ret_sz);
    printf("str:%s\n", str);
    printf("dst:%s\n", dst);
    dump(dst, ret_sz);

#ifdef USE_GLIB
    // dst is null-terminated, so pass 2nd arg as -1
    // and no need to get last validate pos, pass 3nd arg as NULL
    if ( g_utf8_validate(dst, -1, NULL) == TRUE ) {
        printf("g_utf8_validate: ok\n");
    } else {
        printf("g_utf8_validate: fail\n");
    }
#endif

    free(ba);
    free(dst);
#endif
    return 0;
}
