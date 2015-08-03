#define MYMAINFUNCTION		1

typedef unsigned char uchar;
typedef unsigned short ushort;

void ucs2_to_utf8(ushort /*unicode*/ c, uchar* utf) /* uses max 4 chars from utf (including the trailing 0) */
{
	if (c < 0x80)
	{
		utf[0] = c; /* 0******* */
		utf[1] = 0;
	}
	else if (c < 0x800)
	{
		utf[0] = 0xc0 | (c >> 6); /* 110***** 10****** */
		utf[1] = 0x80 | (c & 0x3f);
		utf[2] = 0;
	}
	else
	{
		utf[0] = 0xe0 | (c >> 12); /* 1110**** 10****** 10****** */
		utf[1] = 0x80 | ((c >> 6) & 0x3f);
		utf[2] = 0x80 | (c & 0x3f);
		utf[3] = 0;
	}
	/* UTF-8 is defined for words of up to 31 bits,
	but we need only 16 bits here */
}

#if MYMAINFUNCTION

#include <stdio.h>

void clear_utf8(uchar* utf)
{
	int i;
	for (i=0; i<4; i++) {
		utf[i] = 0;
	}
}

void dump_utf8(uchar* utf)
{
	int i;
	for (i=0; i<4; i++) {
		printf("%02X ", utf[i]);
	}
}

void test(ushort ucs)
{
	uchar utf[4];

	clear_utf8(utf);
	ucs2_to_utf8(ucs, utf);
	dump_utf8(utf);
	printf("\n");
}

int main()
{
	test(0x32);
	test(0x074c);
	test(0x3d5d);
	test(0x7ac8);
	return 0;
}
#endif
