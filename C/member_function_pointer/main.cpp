#include <iostream>
#include "foo.h"

using namespace std;

int main()
{
    foo bar;

    //bar.pub_setval();

    cout << "default" << endl;
    cout << bar.getValue() << endl;

    cout << "high" << endl;
    bar.setPolicy(foo::FOO_HIGH);
    cout << bar.getValue() << endl;

    cout << "middle" << endl;
    bar.setPolicy(foo::FOO_MIDDLE);
    cout << bar.getValue() << endl;

    cout << "low" << endl;
    bar.setPolicy(foo::FOO_LOW);
    cout << bar.getValue() << endl;

    return 0;
}
