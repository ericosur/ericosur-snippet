#include "HelloChild.h"
#include <iostream>
#include <string>

using namespace std;

HelloChild::HelloChild() :
	HelloBase()
{
	cout << "ctor of HelloChild!" << endl;
	init();
}

string HelloChild::getName()
{
	return "class Child";
}
