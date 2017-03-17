#include <iostream>

using namespace std;

class Foo {
public:
    Foo() {
        cout << "ctor" << __func__ << endl;
    }

    void output() {
        cout << __func__ << endl;
    }
};

int main()
{
    cout << __func__ << endl;
//    cout << __STDC_VERSION__ << endl;
    cout << __cplusplus << endl;
    Foo foo;
    foo.output();
    return 0;
}
