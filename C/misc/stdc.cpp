#include <iostream>
#include <chrono>
#include <ratio>
#include <thread>

using namespace std;

#define PRINT_HEADER()  \
    std::cout << __func__ << " =====>>>" << std::endl;

class Foo {
public:
    Foo() {
        cout << "ctor" << __func__ << endl;
    }

    void output() {
        PRINT_HEADER();
    }

    static void f() {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
};


// reference: https://en.cppreference.com/w/cpp/chrono/duration/duration_cast
int test1()
{
    PRINT_HEADER();
    auto t1 = std::chrono::high_resolution_clock::now();
    Foo::f();
    auto t2 = std::chrono::high_resolution_clock::now();

    // floating-point duration: no duration_cast needed
    std::chrono::duration<double, std::milli> fp_ms = t2 - t1;

    // integral duration: requires duration_cast
    auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);

    // converting integral duration to integral duration of shorter divisible time unit:
    // no duration_cast needed
    std::chrono::duration<long, std::micro> int_usec = int_ms;

    std::cout << "f() took " << fp_ms.count() << " ms, "
              << "or " << int_ms.count() << " whole milliseconds "
              << "(which is " << int_usec.count() << " whole microseconds)" << std::endl;

    return 0;
}

int test0()
{
    PRINT_HEADER();
//    cout << __STDC_VERSION__ << endl;
    cout << __cplusplus << endl;
    Foo foo;
    foo.output();
    return 0;
}

int main()
{
    test0();
    test1();
    return 0;
}
