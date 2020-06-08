#include "test_func.h"

#include <stdio.h>
#include <iostream>
#include <time.h>

class HelloWorker
{
public:
    HelloWorker()  {
        std::cout << "hello world from " << __func__ << std::endl;
    }
};

// the ctor will be run before main()
HelloWorker hw;

// MUST NOT replace NULL here !!
void test_fopen()
{
    FILE* fp = fopen("nosuchfile.txt", "rt");
    if (fp == nullptr) {
        printf("no such file... nullptr\n");
    }
    if (fp == NULL) {
        printf("no such file... NULL\n");
    }
    if (NULL == nullptr) {
        printf("they are the same!\n");
    }
}

int main()
{
    srand(time(nullptr));

    //std::cout << "hello world from " << __func__ << std::endl;

    test_jsonhpp_related();

#if 0
    test_re();
    test_string_connect();

    test_noise();
    test_utfstring();

    test_foo_string();

    test_lamb();

    test_fopen();
#endif

    return 0;
}
