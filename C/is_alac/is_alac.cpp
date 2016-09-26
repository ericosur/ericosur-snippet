#include <stdio.h>
#include <string.h>

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

/**
 * is_alac() to tell if specified file name is ALAC
 * (Apple Loseless Audio Codec) or not. Not just check by extensition.
 * This function will open file and search magic words in the header
 * of media file.
 * @param  fn [in] file name to test
 * @return    true if ALAC, false if error or not ALAC
 */
bool is_alac(const char* fn)
{
    FILE* fptr = fopen(fn, "rb");
    if (fptr == NULL) {
        perror("fopen");
        return false;
    }

    const int START_POS = 0x190;
    const int CHECK_SIZE = 0x40;
    char buffer[CHECK_SIZE*2];

    fseek(fptr, START_POS, SEEK_SET);
    size_t readsize = fread(buffer, sizeof(char), CHECK_SIZE, fptr);
    //printf("readsize: %lu\n", readsize);
    //dump(buffer, CHECK_SIZE);
    char* p = (char*)memchr(buffer, 'a', readsize);
    if (p != NULL && strncmp(p, "alac", 4) == 0) {
        return true;
    }
    return false;
}

int main(int argc, char* argv[])
{
#define MYTEST(fn) \
    printf("is %s alac? %s\n", fn, is_alac(fn)?"YES":"NO");

    if (argc == 1) {
        printf("please specify at least one filename...\n");
        return 0;
    }
    for (int i=1; i<argc; i++) {
        MYTEST(argv[i]);
    }
    return 0;
}
