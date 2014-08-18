void ucs2_to_utf8(unsigned short /*unicode*/ c, char* utf) /* uses max 4 chars from utf (including the trailing 0) */
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
