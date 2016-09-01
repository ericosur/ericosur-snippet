#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zlib.h>

#define DEFAULT_BUFFER_SIZE   (1024)

typedef unsigned char byte;

void make_buffer(byte* buffer, int size)
{
    FILE *fin = fopen("/dev/urandom", "r");
    size_t rsz = fread(buffer, 1, size, fin);
    //fprintf(stderr, "rsz=%lu\n", rsz);
    (void)rsz;
    fclose(fin);
}

void dump(const byte* buffer, int size)
{
    for (int i = 0; i < size; i++) {
        if (i&&i%16==0) {
            printf("\n");
        }
        printf("%02X ", (byte)buffer[i]);
    }
    printf("\n");
}

void my_compress_buffer(Byte* outbuf, uLong* outsize, const Byte* inbuf, uLong insize)
{
    int ret = compress(outbuf, outsize, inbuf, insize);
    if (ret == Z_OK) {
        perror("Z_OK");
    } else if (ret == Z_MEM_ERROR) {
        perror("Z_MEM_ERROR");
    } else if (ret == Z_BUF_ERROR) {
        perror("Z_BUF_ERROR");
    }
    fprintf(stderr, "ret = %d, outsize=%lu\n", ret, *outsize);
}

void my_read_line(FILE* ptr)
{
    Byte* inbuf;
    Byte* outbuf;
    uLong inbuf_size = DEFAULT_BUFFER_SIZE;
    uLong outbuf_size = DEFAULT_BUFFER_SIZE*2;
    inbuf = malloc(inbuf_size);
    outbuf = malloc(outbuf_size);

    char line[DEFAULT_BUFFER_SIZE];
    int cnt = 0;
    while (!feof(ptr)) {
        char* p = fgets(line, DEFAULT_BUFFER_SIZE, ptr);
        fprintf(stderr, "%s, len:%lu\n", p, strlen(p));
        strncpy((char*)inbuf, line, DEFAULT_BUFFER_SIZE-2);
        dump(inbuf, DEFAULT_BUFFER_SIZE);
        inbuf_size = DEFAULT_BUFFER_SIZE;
        //fprintf(stderr, "inbuf_size:%lu\n", inbuf_size);
        if (inbuf_size > DEFAULT_BUFFER_SIZE) {
            inbuf_size = DEFAULT_BUFFER_SIZE;
        }
        memset(outbuf, 0, DEFAULT_BUFFER_SIZE*2);
        outbuf_size = DEFAULT_BUFFER_SIZE*2;
        my_compress_buffer(outbuf, &outbuf_size, inbuf, inbuf_size);
        dump(outbuf, outbuf_size);
        cnt ++;
        if (cnt > 1)
            break;
    }
}

void my_read_buffer(FILE* ptr)
{
    Byte* inbuf;
    Byte* outbuf;
    uLong inbuf_size = DEFAULT_BUFFER_SIZE;
    uLong outbuf_size = DEFAULT_BUFFER_SIZE*2;
    inbuf = malloc(inbuf_size);
    outbuf = malloc(outbuf_size);

    int cnt = 0;
    while (!feof(ptr)) {
        size_t sz = fread(inbuf, 1, DEFAULT_BUFFER_SIZE, ptr);
        fprintf(stderr, "%lu\n", sz);
        inbuf_size = sz;
        fprintf(stderr, "inbuf_size:%lu\n", inbuf_size);
        memset(outbuf, 0, DEFAULT_BUFFER_SIZE*2);
        outbuf_size = DEFAULT_BUFFER_SIZE*2;
        my_compress_buffer(outbuf, &outbuf_size, inbuf, inbuf_size);
        dump(outbuf, outbuf_size);
        cnt ++;
        if (cnt > 1)
            break;
    }
}

int main()
{
    const char file[] = "/tmp/list.txt";
    FILE* fptr = fopen(file, "r");
    if (fptr == NULL) {
        perror("fopen");
        return -1;
    }

    my_read_line(fptr);
    //my_read_buffer(fptr);
    fclose(fptr);

    return 0;
}
