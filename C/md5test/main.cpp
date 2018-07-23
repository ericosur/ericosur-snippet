/// main.cpp

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#include "toolbox.h"

#define BUFFER_SIZE     (1024 * 500)
#define DEFAULT_REPEAT  (20000)

uint8_t buffer[BUFFER_SIZE];

void testmd5(uint8_t r)
{
    uint8_t md[MD5_DIGEST_LENGTH];

    memset(md, 0, MD5_DIGEST_LENGTH);
    memset(buffer, r, BUFFER_SIZE);
    toolbox::Md5(buffer, BUFFER_SIZE, md);
}

void benchmark()
{
    int repeat = DEFAULT_REPEAT;
    // if (argc > 1) {
    //     repeat = atoi(argv[1]);
    // }
    fprintf(stderr, "will repeat md5sum %d times\n", repeat);
    for (int i = 0; i<repeat; i++) {
        if (i%1000 == 0) {
            fprintf(stderr, ".");
        }
        uint8_t r = (uint8_t)(i % 255);
        testmd5(r);
    }
    fprintf(stderr, "\n");
}

void get_md5(const uint8_t* buffer, size_t size)
{
    const size_t mdsize = MD5_DIGEST_LENGTH;
    uint8_t md[mdsize];

    bzero(md, mdsize);
    toolbox::Md5(buffer, size, md);
    toolbox::dump(md, mdsize);
}

void get_sha(const uint8_t* buffer, size_t size)
{
    const size_t mdsize = SHA_DIGEST_LENGTH;
    uint8_t md[mdsize];

    bzero(md, mdsize);
    toolbox::Sha(buffer, size, md);
    toolbox::dump(md, mdsize);
}

void get_sha1(const uint8_t* buffer, size_t size)
{
    const size_t mdsize = SHA_DIGEST_LENGTH;
    uint8_t md[mdsize];

    bzero(md, mdsize);
    toolbox::Sha1(buffer, size, md);
    toolbox::dump(md, mdsize);
}

void get_sha256(const uint8_t* buffer, size_t size)
{
    const size_t mdsize = SHA256_DIGEST_LENGTH;
    uint8_t md[mdsize];

    bzero(md, mdsize);
    toolbox::Sha256(buffer, size, md);
    toolbox::dump(md, mdsize);
}

void run_cmd(const char* str, const char* cmd2)
{
    const size_t cmd_size = 768;
    char cmd[cmd_size];

    sprintf(cmd, "printf \"%s\" | %s", str, cmd2);
    printf("running: %s\n", cmd2);
    int r = system(cmd);
    (void)r;
}

void simple_call(const unsigned char* str, const size_t n)
{
    printf("perform %s:\n", __func__);

    printf("call MD5\n");
    unsigned char md0[MD5_DIGEST_LENGTH];
    MD5(str, n, md0);
    toolbox::dump(md0, MD5_DIGEST_LENGTH);

    printf("call SHA\n");
    unsigned char md[SHA_DIGEST_LENGTH];
    SHA(str, n, md);
    toolbox::dump(md, SHA_DIGEST_LENGTH);

}

/*
    note: it seems the result of 'shasum' and 'sha1sum' is the same
    it is better to use 'openssl sha' / 'openssl sha1' to check
 */
int main(/* int argc, char** argv */)
{
    const char str[] = "hello";

    get_md5((const uint8_t*)str, strlen(str));
    run_cmd(str, "openssl md5");
    get_sha((const uint8_t*)str, strlen(str));
    run_cmd(str, "openssl sha");
    get_sha1((const uint8_t*)str, strlen(str));
    run_cmd(str, "openssl sha1");
    get_sha256((const uint8_t*)str, strlen(str));
    run_cmd(str, "openssl sha256");

    simple_call((const unsigned char*)str, strlen(str));

    return 0;
}
