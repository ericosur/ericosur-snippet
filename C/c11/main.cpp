/// file: main.cpp

#include <iostream>
#include "foo.h"

using namespace std;

int main()
{
    cout << "hello world\n";

    Foo foo;

    foo.a = 3;
    cout << "a" << foo.a << endl;
    // foo.b = 8;
    // cout << "b" << foo.b << endl;
    // foo.c = 11;
    // cout << "c" << foo.c << endl;

    return 0;
}
