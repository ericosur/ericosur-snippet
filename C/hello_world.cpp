#include <iostream>

using namespace std;

class HelloWorld
{
public:
	HelloWorld()  {
		cout << "hello world from class HelloWorld\n";
	}
};

// the ctor will be run before main()
HelloWorld hw;

int main()
{
    cout << "hello world from main\n";
	return 0;
}
