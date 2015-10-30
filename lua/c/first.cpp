#include <iostream>
#include <lua.hpp>

using namespace std;

void test()
{
	lua_State *L = lua_open();
	lua_close(L);
}

int main()
{
	cout << "hello lua!" << endl;
	test();
	return 0;
}

