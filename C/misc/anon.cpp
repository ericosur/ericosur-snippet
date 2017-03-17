// anon.cpp
// try anonymous function for c++
#include <iostream>

using namespace std;

int foo()
{
    auto f = [](int m, int n) -> int { return (m+n); };
    auto n = f(3, 7);

    return n;
}

int main()
{

    cout << foo() << endl;

    return 0;
}
