#ifndef __LIB_TEST_FUNC_H__
#define __LIB_TEST_FUNC_H__

#include <iostream>

#define JSONPATH    "../test.json"

void print_title(const std::string& s);
void test_read_json();
void show_jsonhpp_version();
void test_string_connect();
void test_re();

double generateGaussianNoise(double mu, double sigma);
void test_noise();

void test_utfstring();

#endif  // __LIB_TEST_FUNC_H__
