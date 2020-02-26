#include <stdint.h>
#include <iostream>

using namespace std;

#define MINUS_100   (-100)

int main()
{
    int16_t m = MINUS_100;
    uint16_t n = MINUS_100;
    int32_t p = MINUS_100;

    cout << "m:" << dec << m << "  hex: " << hex << m << endl;
    cout << "n:" << dec << n << "  hex: " << hex << n << endl;
    cout << "p:" << dec << p << "  hex: " << hex << p << endl;

    return 0;
}