// g++ -O2 -Wall -std=gnu++11

#include <iostream>
#include <string>

using namespace std;

#if __cplusplus >= 201103L
void test()
{
    string s = "There are " + to_string(100) + " apples.";
    cout << s << endl;
}
#else
#error need C++11 support
#endif

int main()
{
    test();
    return 0;
}
