#include <stdio.h>
#include <string.h>
#include <memory.h>

#include <openssl/aes.h>

void show(unsigned char* md, size_t len);
void enc();
void dec();

const int MYBUFFERSIZE = 1024;
unsigned char result[MYBUFFERSIZE];

void testAES()
{
	enc();
	dec();
}

void enc()
{
	//unsigned char key16[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	//unsigned char key24[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23};
	unsigned char key32[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
	unsigned char iv[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

	unsigned char inbuf[MYBUFFERSIZE]="The quick brown fox jumps over the lazy dog";
	unsigned char outbuf[MYBUFFERSIZE];

	AES_KEY aeskey;

	memset(outbuf, 0, sizeof(outbuf));

	AES_set_encrypt_key(key32, 32*8, &aeskey);

	AES_cbc_encrypt(inbuf, outbuf, MYBUFFERSIZE, &aeskey, iv, AES_ENCRYPT);

	memcpy(result, outbuf, MYBUFFERSIZE);
	show(outbuf, sizeof(outbuf));
}

void dec()
{
	//unsigned char key16[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
	//unsigned char key24[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23};
	unsigned char key32[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
	unsigned char iv[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

	unsigned char inbuf[MYBUFFERSIZE];
	unsigned char outbuf[MYBUFFERSIZE];

	AES_KEY aeskey;

	memcpy(inbuf, result, MYBUFFERSIZE);
	memset(outbuf, 0, sizeof(outbuf));

	AES_set_decrypt_key(key32, 32*8, &aeskey);
	AES_cbc_encrypt(inbuf, outbuf, MYBUFFERSIZE, &aeskey, iv, AES_DECRYPT);

	show(outbuf, sizeof(outbuf));
	printf("show as string: [%s]\n", (char*)outbuf);
}
