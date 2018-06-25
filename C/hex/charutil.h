#ifndef __FOO_CHAR_UTIL_H__
#define __FOO_CHAR_UTIL_H__

#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

void dump(const char* buf, int size);
uint8_t fetch_two_digits(const char* tok);
void str2hex(const char* str, char* bytearray, size_t& sz);
char* iso88591_to_utf8(const char *str, size_t& ret_sz);
uint8_t get_value_from_digits(uint8_t cc);

int test0();

#endif  // __FOO_CHAR_UTIL_H__
