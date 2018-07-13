/*
    using iconv function to do character transcoding
 */

#include <stdio.h>
#include <string.h>
#include <iconv.h>

char* ConvertEnc(const char* encFrom, const char* encTo, const char* in)
{
    static char  bufout[1024], *sin, *sout;
    int lenout, ret;
    size_t lenin;
    iconv_t c_pt;

    if ((c_pt = iconv_open(encTo, encFrom)) == (iconv_t)-1) {
        printf("iconv_open false: %s ==> %s\n", encFrom, encTo);
        return NULL;
    }
    iconv(c_pt, NULL, NULL, NULL, NULL);
    lenin  = strlen(in) + 1;
    lenout = 1024;
    sin    = (char *)in;
    sout   = bufout;
    ret = iconv(c_pt, &sin, (size_t *)&lenin, &sout, (size_t *)&lenout);
    if (ret == -1) {
        return NULL;
    }
    iconv_close(c_pt);
    return bufout;
}

void test(const char* tok, const char* from_encoding)
{
    char* out = ConvertEnc(from_encoding, "UTF-8", tok);
    printf("%s\n", out);
}

int main()
{
    test("hello world", "UTF-8");
    test("\xa4\x6a\xa4\xa4\xa6\xdc\xa5\xbf", "BIG5");
    test("\xc9\xcc\xd2\xb5\xd2\xf8\xd0\xd0", "GBK");

    return 0;
}
