/// file: friend.cpp
/// g++ -std=c++0x -o friend -c friend.cpp
#include <iostream>
using namespace std;

class bar;

class foo
{
//friend class bar;
private:
	static int m_val;
};

int foo::m_val = 99;

class bar
{
public:
	int getValue() {
		return foo::m_val;
	}
};


int main()
{
	bar bar;
	cout << bar.getValue() << endl;
	return 0;
}
