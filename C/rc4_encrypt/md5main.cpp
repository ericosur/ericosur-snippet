/**
	\file md5main.cpp
	\date Jul 22 2004 add comments for doxygen
	\author rasmus lai

	a small test program for MD5 digest
*/
#include <stdio.h>
#include <stdlib.h>
#include "ToolBox.hpp"

const int MY_MD5_DIGEST_LENGTH = 16;
const int MY_SHA_DIGEST_LENGTH = 20;

int main(int argc, char **argv)
{
	if (argc != 2)
	{
		printf("Usage: %s <infile>\n", argv[0]);
		exit(-2);
	}

	FILE *in = NULL;
	byte md5_hash[MY_MD5_DIGEST_LENGTH];
	byte sha1_hash[MY_SHA_DIGEST_LENGTH];

	printf("mymd5 starting...\n");

	if ( (in = fopen(argv[1], "rb")) == NULL )
	{
		printf("error: cannot open file for writing\n");
		exit(-1);
	}

	size_t total_size = 0;
	// rewind the file pointer
	fseek(in, 0, SEEK_SET);
	CalculateFileMD5(in, md5_hash, total_size);
	printf("total size for md5 = %d\n", total_size);

	// rewind the file pointer
	total_size = 0;
	fseek(in, 0, SEEK_SET);
	CalculateFileSHA1(in, sha1_hash, total_size);
	printf("total size for sha1 = %d\n", total_size);
	fclose(in);

	PrintHashValue(md5_hash, MY_MD5_DIGEST_LENGTH);
	PrintHashValue(sha1_hash, MY_SHA_DIGEST_LENGTH);

	return 0;
}

