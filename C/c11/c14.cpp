#include <iostream>

using namespace std;

int main()
{
	auto func = [](auto x, auto y) { return x + y; };

	cout << func(5.0, 3.5) << endl;

	int b = 0b0001'1110'1001'1101;
	cout << hex << b << endl;
	
	return 0;
}
