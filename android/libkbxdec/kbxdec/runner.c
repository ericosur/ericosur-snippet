#include <stdio.h>

#include "kbxdecrypt.h"

int main()
{
    if ( decryptKeyboxFile(KEYBOX_FILENAME, KEYBOX_BINARY) ) {
        printf("ok\n");
    } else {
        printf("nok\n");
    }

    return 0;
}
