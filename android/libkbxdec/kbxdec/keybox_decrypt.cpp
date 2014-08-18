/// file: keybox_decrypt.cpp

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <memory.h>

#include <openssl/aes.h>
#include <openssl/md5.h>

#include "kbxdecrypt.h"

//#define DEBUG_PRINT

#define KEYBOX_LENGTH            128
#define KEYBOX_FILE_LENGTH       (KEYBOX_LENGTH + MD5_DIGEST_LENGTH) * 2
//#define maxCmdLength             150

enum
{
    SUCCESSFUL,
    DEC_SBK_ERROR,
    DEC_KEYBOX_ERROR,
    EKS_ENCRYPT_KEYS_ERROR
};


// encrypt user key, using AES-256
static const unsigned char encKey32[] = {
    0x71, 0xeb, 0x82, 0x5e, 0x72, 0x2e, 0x2d, 0x7f, 
    0xc0, 0x79, 0x0d, 0xa0, 0xcf, 0xaa, 0xf0, 0xd3, 
    0xb7, 0xbc, 0x94, 0x56, 0x40, 0x0c, 0x55, 0xc7, 
    0x98, 0x70, 0xe7, 0xbc, 0x9f, 0x0c, 0xeb, 0x30
};

void transHexToBin(unsigned char *toBuffer, const char* fromString)
{
    char hexchar[] = "0123456789abcdef";
    int  num[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    unsigned int  i, j, k = 0;
    const char *data = fromString;
    size_t fromStringLen = strlen(fromString);

    for (i=0; i<fromStringLen; i++)
    {
        for (j=0; j<strlen(hexchar); j++)
        {
            if (data[i] == hexchar[j])
            {
                if (i%2 == 0)
                {
                    toBuffer[k] = num[j]*16;
                }
                else
                {
                    toBuffer[k] = toBuffer[k] + num[j];
                    k++;
                }
            }
        }
    }
}

bool decrypt(unsigned char *plain, unsigned char *cipher, size_t length)
{
    // notice iv would be changed
	unsigned char iv[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	AES_KEY aeskey;

	if(AES_set_decrypt_key(encKey32, 256, &aeskey))
	{
#ifdef DEBUG_PRINT
        printf("%d, Fail to set decrypt key\n", __LINE__);
#endif
        return false;
    }
	AES_cbc_encrypt(cipher, plain, length, &aeskey, iv, AES_DECRYPT);

    return true;
}

bool mydigest(unsigned char *data, size_t len, unsigned char *md)
{
    MD5_CTX ctx;

    if (MD5_Init(&ctx) != 1)
    {
#ifdef DEBUG_PRINT
        printf("%d, Fail to initial md5\n", __LINE__);
#endif
        return false;
    }
    if (MD5_Update(&ctx, data, len) != 1)
    {
#ifdef DEBUG_PRINT
        printf("%d, Fail to update md5\n", __LINE__);
#endif
        return false;
    }
    if (MD5_Final(md, &ctx) != 1)
    {
#ifdef DEBUG_PRINT
        printf("%d, Fail to finalize md5\n", __LINE__);
#endif
        return false;
    }

    return true;
}

#ifdef __cplusplus
extern "C" {
#endif

int decryptKeyboxBuffer(const char cipher[CIPHER_LENGTH*2+1], unsigned char plain[PLAIN_LENGTH])
{
    unsigned char checksum[MD5_DIGEST_LENGTH];
    unsigned char enckeybox[KEYBOX_LENGTH];
    //unsigned char plain[KEYBOX_LENGTH];
    unsigned char md[MD5_DIGEST_LENGTH];

    char md5enckeybox[KEYBOX_FILE_LENGTH+1];
    
    memset(md5enckeybox, 0, KEYBOX_FILE_LENGTH+1);
    memcpy(md5enckeybox, cipher, KEYBOX_FILE_LENGTH);

#ifdef DEBUG_PRINT
    printf("[%s]\nlen: %d\n", md5enckeybox, strlen(md5enckeybox));
#endif
    if (strlen(md5enckeybox) != KEYBOX_FILE_LENGTH)
    {
#ifdef DEBUG_PRINT
        printf("%d, invalid keybox length\n", __LINE__);
#endif
        return false;
    }

    char strKeybox[KEYBOX_LENGTH*2 + 1];
    memset(strKeybox, 0, KEYBOX_LENGTH*2 + 1);
    memcpy(strKeybox, md5enckeybox, KEYBOX_LENGTH*2);
    transHexToBin(enckeybox, strKeybox);

    char strMd5[MD5_DIGEST_LENGTH*2 + 1];
    memset(strMd5, 0, MD5_DIGEST_LENGTH*2 + 1);
    memcpy(strMd5, md5enckeybox + KEYBOX_LENGTH*2, MD5_DIGEST_LENGTH*2);
    transHexToBin(checksum, strMd5);

    memset(md, 0, MD5_DIGEST_LENGTH);
    if (!mydigest(enckeybox, KEYBOX_LENGTH, md))
    {
        return false;
    }
    if (memcmp(md, checksum, MD5_DIGEST_LENGTH) != 0)
    {
#ifdef DEBUG_PRINT
        printf("%d, Keybox digest mismatch", __LINE__);
#endif
        return false;
    }

    memset(plain, 0, KEYBOX_LENGTH);
    if (!decrypt(plain, enckeybox, KEYBOX_LENGTH))
    {
        return false;
    }

    return true;
}


int decryptKeyboxFile(const char* fnin, const char* fnout)
{
    unsigned char checksum[MD5_DIGEST_LENGTH];
    unsigned char enckeybox[KEYBOX_LENGTH];
    unsigned char plain[KEYBOX_LENGTH];
    unsigned char md[MD5_DIGEST_LENGTH];

    char md5enckeybox[KEYBOX_FILE_LENGTH+1];
    FILE *fptr = NULL;

    if ( (fptr = fopen(fnin, "rt")) == NULL )
    {
#ifdef DEBUG_PRINT
        printf("%d, Fail to open %s\n", __LINE__, fnin);
#endif
        return false;
    }
    else
    {
        memset(md5enckeybox, 0, KEYBOX_FILE_LENGTH+1);
        fgets(md5enckeybox, KEYBOX_FILE_LENGTH+1, fptr);
#ifdef DEBUG_PRINT
        printf("[%s]\nlen: %d\n", md5enckeybox, strlen(md5enckeybox));
#endif
        if (strlen(md5enckeybox) != KEYBOX_FILE_LENGTH)
        {
#ifdef DEBUG_PRINT
            printf("%d, invalid keybox length\n", __LINE__);
#endif
            return false;
        }

        char strKeybox[KEYBOX_LENGTH*2 + 1];
        memset(strKeybox, 0, KEYBOX_LENGTH*2 + 1);
        memcpy(strKeybox, md5enckeybox, KEYBOX_LENGTH*2);
        transHexToBin(enckeybox, strKeybox);

        char strMd5[MD5_DIGEST_LENGTH*2 + 1];
        memset(strMd5, 0, MD5_DIGEST_LENGTH*2 + 1);
        memcpy(strMd5, md5enckeybox + KEYBOX_LENGTH*2, MD5_DIGEST_LENGTH*2);
        transHexToBin(checksum, strMd5);

        memset(md, 0, MD5_DIGEST_LENGTH);
        if (!mydigest(enckeybox, KEYBOX_LENGTH, md))
        {
            return false;
        }
        if (memcmp(md, checksum, MD5_DIGEST_LENGTH) != 0)
        {
#ifdef DEBUG_PRINT
            printf("%d, Keybox digest mismatch", __LINE__);
#endif
            return false;
        }

        memset(plain, 0, KEYBOX_LENGTH);
        if (!decrypt(plain, enckeybox, KEYBOX_LENGTH))
        {
            return false;
        }

        FILE *outptr = NULL;
        if ( (outptr = fopen(fnout, "wb")) == NULL )
        {
#ifdef DEBUG_PRINT
            printf("%d, write output file %s fail\n", __LINE__, fnout);
#endif
        }
        else
        {
            fwrite(plain, KEYBOX_LENGTH, 1, outptr);
        }
        fclose(outptr);
    }
    fclose(fptr);

    return true;
}

#ifdef __cplusplus
}
#endif
