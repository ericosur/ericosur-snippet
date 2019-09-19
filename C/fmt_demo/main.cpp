#include <iostream>
#include "tests.h"


int main()
{
    srand(time(nullptr));

    std::cout << "hello world from " << __func__ << std::endl;

    test_fmt();

    return 0;
}
