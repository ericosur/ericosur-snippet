/** \file toolbox.cpp
 * implementation of my own openssl functions
*/
#include "toolbox.h"

#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

int CalculateBufferMD5(byte* buffer, size_t buffer_size, byte *md5_hash)
{
	//size_t size_read = 0;
	MD5_CTX ctx;

	if (md5_hash == NULL)
	{
		printf("error: hash buffer is null\n");
		return -1;
	}

	memset(&ctx, 0, sizeof(ctx));
	memset(md5_hash, 0, MD5_DIGEST_LENGTH);
	// init ctx
	MD5_Init(&ctx);
	MD5_Update(&ctx, buffer, buffer_size);
	MD5_Final(md5_hash, &ctx);

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
