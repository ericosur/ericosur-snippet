/** \file toolbox.cpp
 * implementation of my own openssl functions
*/
#include "toolbox.h"


namespace toolbox
{

void dump(const uint8_t* buffer, size_t size)
{
    const size_t BYTE_PER_LINE = 16;
    for (size_t i = 0; i < size; i++) {
        if (i && i % BYTE_PER_LINE == 0) {
            printf("\n");
        }
        printf("%02X ", (uint8_t)buffer[i]);
    }
    printf("\n");
}

int Md5(const uint8_t* buffer, const size_t size, uint8_t *hash)
{
    MD5_CTX ctx;

    if (hash == NULL)
    {
        printf("error: hash buffer is null\n");
        return -1;
    }

    memset(&ctx, 0, sizeof(ctx));
    memset(hash, 0, MD5_DIGEST_LENGTH);
    // init ctx
    MD5_Init(&ctx);
    MD5_Update(&ctx, buffer, size);
    MD5_Final(hash, &ctx);

    return 0;
}

int Sha(const uint8_t* buffer, const size_t size, uint8_t *hash)
{
    SHA_CTX ctx;

    if (hash == NULL)
    {
        printf("error: hash buffer is null\n");
        return -1;
    }

    memset(&ctx, 0, sizeof(ctx));
    memset(hash, 0, SHA_DIGEST_LENGTH);
    // init ctx
    SHA_Init(&ctx);
    SHA_Update(&ctx, buffer, size);
    SHA_Final(hash, &ctx);

    return 0;
}

int Sha1(const uint8_t* buffer, const size_t size, uint8_t *hash)
{
    SHA_CTX ctx;

    if (hash == NULL)
    {
        printf("error: hash buffer is null\n");
        return -1;
    }

    memset(&ctx, 0, sizeof(ctx));
    memset(hash, 0, SHA_DIGEST_LENGTH);
    // init ctx
    SHA1_Init(&ctx);
    SHA1_Update(&ctx, buffer, size);
    SHA1_Final(hash, &ctx);

    return 0;
}



int Sha256(const uint8_t* buffer, const size_t size, uint8_t *hash)
{
    SHA256_CTX ctx;

    if (hash == NULL)
    {
        printf("error: hash buffer is null\n");
        return -1;
    }

    memset(&ctx, 0, sizeof(ctx));
    memset(hash, 0, SHA256_DIGEST_LENGTH);
    // init ctx
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, buffer, size);
    SHA256_Final(hash, &ctx);

    return 0;
}

#if 0
int CalculateFileSHA1(FILE *fptr, byte *sha1_hash, size_t& total_read)
{
    const int BUFFERSIZE = 4096;
    byte buffer[BUFFERSIZE];
    size_t size_read = 0;
    SHA_CTX ctx;

    if (sha1_hash == NULL)
    {
        printf("error: hash buffer is null\n");
        return (-3);
    }

    total_read = 0;
    memset(&ctx, 0, sizeof(ctx));
    memset(sha1_hash, 0, SHA_DIGEST_LENGTH);
    // init ctx
    SHA1_Init(&ctx);

    while (!feof(fptr))
    {
        size_read = fread(buffer, 1, sizeof(buffer), fptr);
        SHA1_Update(&ctx, buffer, size_read);
        total_read += size_read;
    }

    SHA1_Final(sha1_hash, &ctx);

    return 0;
}
#endif

}   // namespace toolbox
