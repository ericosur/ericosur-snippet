/** \file myenc.cpp
* \date Jul 22 2004  add doxygen comments
*
* a test program for RC4 encrypting
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ToolBox.hpp"

#include <assert.h>


/** \param header [in/out] set the header size
	\brief set the header size field

	It will return the length without file name
*/
int SetHeaderSize(Header_struct& header);


int main(int argc, char **argv)
{
	FILE *in = NULL;
	FILE *out = NULL;

	// we need 3 arguments
	if (argc != 3)
	{
		printf("%s <infile> <outfile>\n", argv[0]);
		exit(-99);
	}

	printf("starting...\n");

	// open input file
	if ( (in = fopen(argv[1], "rb")) == NULL )
	{
		printf("error: open file [%s] for reading\n", argv[1]);
		exit(-1);
	}
	printf("open '%s' as reading\n", argv[1]);

	// get the input filename
	char* fname = NULL;
	size_t len = strlen(argv[1]) + 1;
	fname = new char[len];
	memset(fname, 0, len);
	strcpy(fname, argv[1]);

// open output file
	if ( (out = fopen(argv[2], "wb")) == NULL )
	{
		printf("error: open file [%s] for writing\n", argv[2]);
		exit(-2);
	}
	printf("open '%s' as writing\n", argv[2]);

	// take command line arguments
	assert(in != NULL);
	assert(out != NULL);

	Header_struct file_header;
	// init file_header
	memset(&file_header, 0, sizeof(file_header));
	memcpy(&file_header.MagicNumber, MY_MAGIC_NUMBER, 16);
	memset(file_header.reserved2, 0xcc, MY_MD5_DIGEST_LENGTH);
	byte header_hash[MY_MD5_DIGEST_LENGTH];
	memset(header_hash, 0, MY_MD5_DIGEST_LENGTH);

// calc MD5 for input file
	CalculateFileMD5(in, file_header.file_md5, file_header.FileSize);
	printf("%d: file md5 = ", __LINE__);
	PrintHashValue((byte*)file_header.file_md5, MY_MD5_DIGEST_LENGTH);
	printf("file size = %lu\n", file_header.FileSize);

// length of filename
	file_header.FileNameLength = strlen(fname) + 1;
//	printf("fname(%s), len(%d)\n", fname, file_header.FileNameLength);
	file_header.FileName = fname;


// write header to file
	int header_size = SetHeaderSize(file_header);
	fseek(out, 0, SEEK_SET);
	fwrite(&file_header, header_size, 1, out);
	fwrite(file_header.FileName, file_header.FileNameLength, 1, out);

// encrypt & output
	fseek(in, 0, SEEK_SET);
//	fseek(out, MY_PRESERVED_LENGTH, SEEK_SET);
//	fwrite(file_header.reserved2, MY_MD5_DIGEST_LENGTH, 1, out);
	EncryptFileByRC4(in, out);

// calculate header md5
	VerifyHeaderMD5(file_header, header_hash);
	printf("header hash: ");
	PrintHashValue(header_hash, MY_MD5_DIGEST_LENGTH);
// write header checksum
	fseek(out, 0x20, SEEK_SET);
	byte stamp_buf[MY_MD5_DIGEST_LENGTH];
	memset(stamp_buf, 0xcc, MY_MD5_DIGEST_LENGTH);
	fwrite(stamp_buf, MY_MD5_DIGEST_LENGTH, 1, out);
	fwrite(header_hash, MY_MD5_DIGEST_LENGTH, 1, out);

	fclose(in);
	fclose(out);
	delete[] fname;

	return 0;
}

int SetHeaderSize(Header& header)
{
	int size = sizeof(header);

	size -= 4;
	header.HeaderSize = size + header.FileNameLength;
//	printf("%d: header.HeaderSize = %d\n", __LINE__, header.HeaderSize);

	return size;
}


