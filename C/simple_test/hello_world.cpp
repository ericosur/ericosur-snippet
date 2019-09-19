#include "test_func.h"

#include <iostream>
#include <time.h>

class HelloWorld
{
public:
    HelloWorld()  {
        std::cout << "hello world from " << __func__ << std::endl;
    }
};

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

    return 0;
}
