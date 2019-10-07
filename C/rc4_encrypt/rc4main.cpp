/// \file: rc4main.cpp

#include <stdio.h>
#include <stdlib.h>
#include "toolbox.hpp"

int main(int argc, char **argv)
{
	if (argc != 3)
	{
		printf("%s <infile> <outfile>\n", argv[0]);
		exit(-2);
	}

	FILE *in = nullptr;
	FILE *out = nullptr;

	printf("myrc starting...\n");

	if ( (in = fopen(argv[1], "rb")) == nullptr )
	{
		printf("error while open 'in' for writing\n");
		exit(-1);
	}

	if ( (out = fopen(argv[2], "wb")) == nullptr )
	{
		printf("error while open 'ccc' for writing\n");
		exit(-1);
	}

	const int BUFFERSIZE = 4096;
	byte buffer[BUFFERSIZE], out_buffer[BUFFERSIZE];
	size_t size_read = 0, total_read = 0;

	fflush(stdout);

	while (!feof(in))
	{
		size_read = fread(buffer, 1, sizeof(buffer), in);
		//printf("%lu", size_read);
		printf(".");
		PerformRC4(buffer, out_buffer, size_read);
		fwrite(out_buffer, 1, size_read, out);
		total_read += size_read;
	}
	printf("\n");
	fclose(in);
	fclose(out);
	printf("total processed: %lu bytes\n", total_read);

	return 0;
}
