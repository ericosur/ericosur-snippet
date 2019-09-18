#include "test_func.h"

#include <iostream>
#include <time.h>

// fmt:print()
#include <fmt/core.h>

class HelloWorld
{
public:
    HelloWorld()  {
        std::cout << "hello world from " << __func__ << std::endl;
    }
};

// how to use & sample:
// https://fmt.dev/latest/index.html
// how to link and build:
// https://fmt.dev/latest/usage.html
// python format usage:
// https://github.com/gto76/python-cheatsheet#format
//
void test_fmt()
{
    // use fmt::print() like python fmt
    fmt::print("fmt says: The answer is {}.\n", 42);
    for (int i = 0; i < 3; i++) {
        fmt::print("[{:>4d}] result: {:.3f}\n", i, i*1.05);
    }
}



// the ctor will be run before main()
HelloWorld hw;


int main()
{
    srand(time(nullptr));

    std::cout << "hello world from " << __func__ << std::endl;
    show_jsonhpp_version();

    test_read_json();
    test_re();
    test_string_connect();

    test_noise();
    test_utfstring();

    test_foo_string();

    test_lamb();

    test_fmt();

    return 0;
}
