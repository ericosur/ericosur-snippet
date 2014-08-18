/// file: kbxdecrypt.h

#ifndef __KBXDECRYPT_H___
#define __KBXDECRYPT_H___

// a file contain one encrypted keybox
// one line with 288 chars:
// [0-9a-f]{288}\n

#define KEYBOX_FILENAME         "keybox.txt"
#define KEYBOX_BINARY           "keybox.bin"
#define CIPHER_LENGTH       (128+16)
#define PLAIN_LENGTH        (128)

#ifdef __cplusplus
extern "C" {
#endif

// input 288 + 1 C string in hex
// output 128 byte binary data
int decryptKeyboxBuffer(const char cipher[CIPHER_LENGTH*2+1], unsigned char plain[PLAIN_LENGTH]);

int decryptKeyboxFile(const char* fnin, const char* fnout);


#ifdef __cplusplus
}
#endif

#endif  // __KBXDECRYPT_H___
