#include <iostream>

using namespace std;

int main()
{
	auto func = [](int x, int y) { return x + y; };

	cout << func(5.0, 3.5) << endl;
	return 0;
}
