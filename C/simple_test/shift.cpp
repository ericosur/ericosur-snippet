#include <stdint.h>
#include <iostream>

int16_t shift1(const int8_t val)
{
    return (val << 8) >> 8;
}

int16_t shift2(const int8_t val)
{
    return (((val << 8) & 0xFF00) >> 8);
}

void test()
{
    using namespace std;

    int8_t m = 0x7F;
    int8_t n = 0x89;

    cout << "shift1: " << hex << shift1(m) << endl
        << "shift2: " << hex << shift2(m) << endl;

    cout << "shift1: " << hex << shift1(n) << endl
        << "shift2: " << hex << shift2(n) << endl;

}

int main()
{
    test();
    return 0;
}