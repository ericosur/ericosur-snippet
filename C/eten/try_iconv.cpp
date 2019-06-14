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
        return nullptr;
    }
    iconv(c_pt, nullptr, nullptr, nullptr, nullptr);
    lenin  = strlen(in) + 1;
    lenout = 1024;
    sin    = (char *)in;
    sout   = bufout;
    ret = iconv(c_pt, &sin, (size_t *)&lenin, &sout, (size_t *)&lenout);
    if (ret == -1) {
        return nullptr;
    }
    iconv_close(c_pt);
    return bufout;
}
