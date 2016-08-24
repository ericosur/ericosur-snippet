/**
	\file ReadHeader.cpp
	\date Jul 22 2004

	read the header of file encrypted by \e myenc
*/

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#include "toolbox.hpp"
/**
	\param header [in] data of header to print out
	\param fnmae [in] input file name
*/
void ShowHeader(const Header& header, const char* fname);


#define TEMP_BUFFER_SIZE	256
char FileName[TEMP_BUFFER_SIZE];

int main(int argc, char** argv)
{
	FILE* fptr = NULL;
	Header header;
	byte header_digest[MY_MD5_DIGEST_LENGTH];
	byte calculated_digest[MY_MD5_DIGEST_LENGTH];
	size_t size_read = 0;

	memset(&header, 0, sizeof(header));
	memset(FileName, 0, TEMP_BUFFER_SIZE);

	if (argc != 2)
	{
		printf("not enough arguments\n");
		return -2;
	}
	if ( (fptr = fopen(argv[1], "rb")) == NULL )
	{
		printf("error: cannot open [%s] to read\n", argv[1]);
		return -1;
	}
	printf("readhead: open [%s]\n", argv[1]);
// read ''Header'' from intpu file
	fseek(fptr, 0, SEEK_SET);
	size_read = fread(&header, sizeof(header)-sizeof(char*), 1, fptr);
	assert( size_read != 0 );

	size_read = fread(FileName, header.FileNameLength, 1, fptr);
	assert( size_read != 0 );

	header.FileName = FileName;
	memcpy(header_digest, header.header_md5, MY_MD5_DIGEST_LENGTH);

	fclose(fptr);


	if (verify_magic(header))
	{
		ShowHeader(header, FileName);
	}
	else
	{
		return -1;
	}

// verify header md5
//	memset(header.reserved2, 0, MY_MD5_DIGEST_LENGTH);
	memset(header.header_md5, 0, MY_MD5_DIGEST_LENGTH);
	VerifyHeaderMD5(header, calculated_digest);

	if (memcmp(header_digest, calculated_digest, MY_MD5_DIGEST_LENGTH) == 0)
	{
		printf("validated ok\n");
	}
	else
	{
		printf("calculated digest = ");
		PrintHashValue(calculated_digest, MY_MD5_DIGEST_LENGTH);
		printf("header MD5 hash = ");
		PrintHashValue(header_digest, MY_MD5_DIGEST_LENGTH);
	}
	return 0;
}

void ShowHeader(const Header& header, const char* fname)
{
//	printf("sizeof(header) = %d\n", sizeof(header));
	printf("MagicNumber = [%s]\n", header.MagicNumber);
	printf("HeaderSize = %d\n", header.HeaderSize);
	printf("FileNameLength = %d\n", header.FileNameLength);
	printf("FileSize = %lu\n", header.FileSize);
	printf("file MD5 hash = ");
	PrintHashValue(header.file_md5, MY_MD5_DIGEST_LENGTH);
	printf("FileName = [%s]\n", fname);

//	printf("actual header size = %d\n", GetActualHeaderSize(header.HeaderSize));
	fflush(stdout);
}



