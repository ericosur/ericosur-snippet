/** \file toolbox.cpp
 * implementation of my own openssl functions
*/
#include "toolbox.hpp"

#include <string.h>
#include <openssl/md5.h>
#include <openssl/sha.h>
#include <openssl/rc4.h>
#include <stdlib.h>

int CalculateFileMD5(FILE *fptr, byte *md5_hash, size_t& total_read)
{
	const int BUFFERSIZE = 4096;
	byte buffer[BUFFERSIZE];
	size_t size_read = 0;
	MD5_CTX ctx;

	if (md5_hash == NULL)
	{
		printf("error: hash buffer is null\n");
		return -1;
	}

	memset(&ctx, 0, sizeof(ctx));
	memset(md5_hash, 0, MD5_DIGEST_LENGTH);
	total_read = 0;
	// init ctx
	MD5_Init(&ctx);

	while (!feof(fptr))
	{
		size_read = fread(buffer, 1, BUFFERSIZE, fptr);
//		printf("%d ", size_read);
		MD5_Update(&ctx, buffer, size_read);
		total_read += size_read;
	}

	MD5_Final(md5_hash, &ctx);

//	printf("%s(%d) CalculateFileMD5(): %d", __FILE__, __LINE__, total_read);
	return 0;
}

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

void PrintHashValue(const byte *hash, const int len)
{
	int i;
	if (hash == NULL && len > 0)
		return;
//	printf("dump size = %d\n", len);
	for (i = 0; i < len; i ++)
	{
		printf("%02x", hash[i]);
		if (i != 0 && (i % 16) == 15 )
			printf("\n");
	}
	if (i!=0 && i%16 != 15)
		printf("\n");
}

void PerformRC4(const byte* in, byte* out, size_t len)
{
	RC4_KEY my_key;
	const char PASSWD[] = "A quick brown fox jumps over the lazy dog";

	memset(&my_key, 0, sizeof(my_key));

	RC4_set_key(&my_key, sizeof(PASSWD), (const unsigned char*)PASSWD);
	RC4(&my_key, len, in, out);
}

int GetActualHeaderSize(int record_header_size)
{
	return ( record_header_size + (16 - record_header_size % 16) );
}

void EncryptFileByRC4(FILE *in, FILE *out)
{
	const int BUFFERSIZE = 1024 * 10;
	byte buffer[BUFFERSIZE], out_buffer[BUFFERSIZE];
	size_t size_read = 0, total_read = 0;
	size_t size_write = 0, total_write = 0;

//	fseek(in , 0, SEEK_SET);
	while (!feof(in))
	{
		size_read = fread(buffer, 1, sizeof(buffer), in);
		PerformRC4(buffer, out_buffer, size_read);
		size_write = fwrite(out_buffer, 1, size_read, out);
		total_read += size_read;
		total_write += size_write;
	}
//	printf("%s(%d): %d, %d\n", __FILE__, __LINE__, total_read, total_write);
}

void VerifyHeaderMD5(const Header& header, byte* recorded_md5)
{
	byte *_fake = (byte*)malloc(512);
	size_t buf_len = header.HeaderSize;
	size_t len_copy_hdr = sizeof(Header) - 4;

	memset(_fake, 0, buf_len);
	memcpy(_fake, &header, len_copy_hdr);
	memcpy(_fake+len_copy_hdr, (byte*)header.FileName, header.FileNameLength);

	PrintHashValue(_fake, buf_len);

	CalculateBufferMD5(_fake, buf_len, recorded_md5);
//	PrintHashValue(recorded_md5, MY_MD5_DIGEST_LENGTH);

	free(_fake);
}

bool verify_magic(const Header_struct& header)
{
	if ( memcmp(&header, MY_MAGIC_NUMBER, 16) != 0 )
	{
		printf("This file is not rasmus own encrypted file\n");
		return false;
	}

	printf("magic header matched\n");
	return true;
}

