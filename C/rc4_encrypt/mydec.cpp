/**
	\file mydec.cpp
	\date Jul 21 2004

	the program to decrypt files encrypted by \e 'myenc'
*/

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#include "ToolBox.hpp"
#include <unistd.h>

const int MY_MD5HASH_LEN = 16;

void my_truncate(const char* fname, size_t to_size);

int main(int argc, char** argv)
{
	char TMPFILE[] = "tmp1234";
	FILE *in = NULL;
	FILE *out = NULL;

	// we need one argument
	if (argc != 2)
	{
		printf("%s <file to decrypt>\n", argv[0]);
		return (-99);
	}

	// open input file
	if ( (in = fopen(argv[1], "rb")) == NULL )
	{
		printf("error: canot open file [%s] for reading\n", argv[1]);
		return (-1);
	}
	printf("open '%s' for reading\n", argv[1]);

	// open output file
	if ( (out = fopen(TMPFILE, "wb")) == NULL )
	{
		printf("error: open file [%s] for writing\n", TMPFILE);
		return (-3);
	}
	printf("open tmpfile for writing\n");

// get header from input file
	Header header;
	byte header_md5[MY_MD5_DIGEST_LENGTH];
	char *filename = NULL;
	size_t size_read;

	fseek(in, 0, SEEK_SET);
	size_read = fread(&header, sizeof(header)-sizeof(char*), 1, in);
	assert( size_read != 0 );

	filename = (char*)malloc(header.FileNameLength);
	size_read = fread(filename, header.FileNameLength, 1, in);
	assert( size_read != 0 );

	header.FileName = filename;

	memcpy(header_md5, header.header_md5, MY_MD5_DIGEST_LENGTH);
//	PrintHashValue((byte*)&header, header.HeaderSize);
	byte calc_md5[MY_MD5_DIGEST_LENGTH];
//	memset(header.reserved2, 0, MY_MD5_DIGEST_LENGTH);
	memset(header.header_md5, 0, MY_MD5_DIGEST_LENGTH);
	VerifyHeaderMD5(header, calc_md5);
	if (memcmp(calc_md5, header_md5, MY_MD5_DIGEST_LENGTH) == 0)
	{
		printf("ok\n");
	}
	else
	{
		printf("header is invalid\n");
		exit (-1);
	}

	fseek(in, header.HeaderSize, SEEK_SET);
	fseek(out, 0, SEEK_SET);
	size_t in_pos = ftell(in);
	//printf("start read content from: %d\n", in_pos);
	// decrypt & output
	EncryptFileByRC4(in, out);
	fflush(out);
// close files
	fclose(in);
	fclose(out);

	exit(-2);

#if 0
// truncate file
	my_truncate(TMPFILE, header.FileSize);
#endif

// final check the output file
	FILE* check = NULL;
	if ( (check = fopen(TMPFILE, "rb")) == NULL )
	{
		printf("open tmpfile for checking md5 error\n");
	}
	else
	{
		size_t total_read = 0, file_size = 0;
		byte md5_hash[MY_MD5HASH_LEN];

		fseek(check, 0, SEEK_SET);
		CalculateFileMD5(check, md5_hash, total_read);

		if ( memcmp(md5_hash, header.file_md5, MY_MD5HASH_LEN) != 0 )
		{
			printf("md5 checksum invalid\n");
			printf("calculated md5 = ");
			PrintHashValue(md5_hash, MY_MD5HASH_LEN);
			printf("recorded md5 = ");
			PrintHashValue(header.file_md5, MY_MD5HASH_LEN);
		}
		if ( total_read != header.FileSize )
		{
			printf("size not matched %lu vs %lu\n", total_read, file_size);
		}
	}

	// renmae tmp file to actual file
	rename(TMPFILE, header.FileName);

	free(filename);

	return 0;
}

void my_truncate(const char* fname, size_t to_size)
{
	printf("%s(%d) my_truncate(%s, %lu)...\n", __FILE__, __LINE__, fname, to_size);

	const char out_fname[] = "tmp9876";
	FILE *in = fopen(fname, "rb");
	FILE *out = fopen(out_fname, "wb");
	if (in == NULL || out == NULL)
	{
		printf("something wrong\n");
		return;
	}

	const int BUFFER_SIZE = 1024*10;
	size_t left_size = to_size;
	size_t read_size = 0;
	size_t write_size = 0;
	byte buffer[BUFFER_SIZE];
	size_t total_write = 0;

	while (left_size > 0 && !feof(in))
	{
		read_size = fread(buffer, 1, BUFFER_SIZE, in);
		printf("%lu ", read_size);
		write_size = fwrite(buffer, 1, (read_size > left_size ? left_size : read_size), out);
		left_size -= write_size;
		total_write += write_size;
	}

	printf("total_write = %lu\n", total_write);
	fclose(in);
	fclose(out);

//	unlink(fname);
//	rename(fname, out_fname);
}

