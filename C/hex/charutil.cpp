#include "charutil.h"

/**
 * dump() is a simple stupid dump function to see buffer in HEX
 * @param buf  [in] buffer to see
 * @param size [in] buffer size
 */
void dump(const char* buf, int size)
{
    for (int i=0; i<size; i++) {
        printf("%02X ", (unsigned char)buf[i]);
        if (i%16==15) {
            printf("\n");
        }
    }
    printf("\n");
}

uint8_t fetch_two_digits(const char* tok)
{
    uint8_t cc = get_value_from_digits(tok[0])*16 +
        get_value_from_digits(tok[1]);
    return cc;
}

void str2hex(const char* str, char* bytearray, size_t& sz)
{
    size_t len = strlen(str);
    // char tmp[16];
    // bzero(tmp, sizeof(tmp));
    //printf("len:%d\n", (int)len);

    sz = 0;
    for (size_t i=0; i<len; i+=2) {
        uint8_t dd = fetch_two_digits(str+i);
        bytearray[sz] = (char)dd;
        sz ++;
    }
    bytearray[sz] = 00;
}

char* iso88591_to_utf8(const char *str, size_t& ret_sz)
{
    size_t sz = 1 + (2 * strlen(str));
    char *utf8 = (char*)malloc(sz);
    bzero(utf8, sz);

    //printf("utf8 predicted size: %d\n", (int)sz);
    ret_sz = sz;

    if (utf8) {
        char *c = utf8;
        for (; *str; str++) {
            uint8_t ch = (uint8_t)*str;
            //printf("%02x  ", ch);
            if (ch < 0x80) {
                *c++ = ch;
                //printf(".");
            } else {
                *c++ = (char) (0xc0 | ch >> 6);
                *c++ = (char) (0x80 | (ch & 0x3f));
                //printf("#");
            }
        }
        *c++ = '\0';
    }
    return utf8;
}

uint8_t get_value_from_digits(uint8_t cc)
{
    if (cc >= '0' && cc <= '9') {
        cc = cc - '0';
        return cc;
    }
    if (cc >= 'a' && cc <= 'f') {
        cc = (cc - 'a') + 10;
        return cc;
    }
    if (cc >= 'A' && cc <= 'F') {
        cc = (cc - 'A') + 10;
        return cc;
    }
    return 0;
}

int test0()
{
    char szNumbers[] = "2001 60c0c0 -1101110100110100100000 0x6fffff";
    char *pEnd = nullptr;
    long int li1, li2, li3, li4;
    li1 = strtol(szNumbers, &pEnd, 10);
    li2 = strtol(pEnd, &pEnd, 16);
    li3 = strtol(pEnd, &pEnd, 2);
    li4 = strtol(pEnd, nullptr, 0);
    printf ("The decimal equivalents are: %ld, %ld, %ld and %ld.\n", li1, li2, li3, li4);
    return 0;
}
