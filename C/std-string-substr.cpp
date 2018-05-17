#include <iostream>
#include <stdio.h>

using namespace std;

int main(void)
{
	string foo = "abcdef";
	char ch;

	for (int i = 0; i < foo.length(); i++)
	{
		string bar = foo.substr(i, 1);
		ch = bar.c_str()[0];
		printf("%c\t", ch);
	}
	return 0;
}
