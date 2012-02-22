#include <stdio.h>
#include <string.h>
#include <memory.h>

#include <openssl/md5.h>

void show(unsigned char* buf, size_t len);

void testMD5()
{
	unsigned char my_string[] = "Hello world";
	unsigned char md[MD5_DIGEST_LENGTH];
	MD5_CTX c;

	memset(md, 0, MD5_DIGEST_LENGTH);
	MD5_Init(&c);
	MD5_Update(&c, my_string, sizeof(my_string));
	MD5_Final(md, &c);

	show(md, MD5_DIGEST_LENGTH);
}
