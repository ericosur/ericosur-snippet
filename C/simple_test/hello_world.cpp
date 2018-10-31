#include <iostream>
#include <iomanip>
#include "json.hpp"

using namespace std;

class HelloWorld
{
public:
	HelloWorld()  {
		cout << "hello world from " << __func__ << endl;
	}
};

// the ctor will be run before main()
HelloWorld hw;

void test()
{
	nlohmann::json json = {{"apple", 31}, {"ball", 43}, {"egg", 71}};
	cout << setw(4) << json << endl;

    auto query = json.meta();
    cout << "json.hpp version: " << query["version"]["string"] << endl;
}

int main()
{
    cout << "hello world from " << __func__ << endl;
	test();

	return 0;
}
