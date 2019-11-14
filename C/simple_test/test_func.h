#ifndef __LIB_TEST_FUNC_H__
#define __LIB_TEST_FUNC_H__

#include <iostream>

void print_title(const std::string& s);
void dump(const char* buf, size_t size);

void test_jsonhpp_related();
void test_read_json();
void show_jsonhpp_version();
void test_cbor();

void test_string_connect();
void test_re();

double generateGaussianNoise(double mu, double sigma);
void test_noise();

void test_utfstring();
void test_foo_string();

void test_lamb();

#endif  // __LIB_TEST_FUNC_H__
