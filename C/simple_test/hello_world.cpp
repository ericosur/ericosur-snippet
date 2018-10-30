#include <iostream>
#include "json.hpp"

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

void test()
{
	nlohmann::json json = {"apple", 10};
	std::cout << json << std::endl;
}

int main()
{
    cout << "hello world from main\n";
	test();

	return 0;
}
