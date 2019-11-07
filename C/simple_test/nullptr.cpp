#include <iostream>
using namespace std;

void foo(int i)
{
    cout << "foo#1: i: " << i << endl;
}

void foo(char* c)
{
    if (c == nullptr) {
        cout << "nullptr!!\n";
    }
    cout << "foo#2: c: " << c << endl;
}

// struct BAR {
//     int m = 41;
//     int n = 97;
// };

// void foo(BAR* b)
// {
//     if (b == nullptr) {
//         cout << "nullptr!\n";
//         return;
//     }
//     cout << b->m << endl;
//     cout << b->n << endl;
// }

int main()
{
    //foo(NULL);
    //foo(101);

    char s[] = "money talks";
    foo(s);

    cout << "here...\n";
    foo(nullptr);

    return 0;
}