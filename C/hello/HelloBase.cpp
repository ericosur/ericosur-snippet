/// file: HelloBase.cpp

#include <iostream>
#include "HelloBase.h"

using namespace std;

HelloBase::HelloBase()
{
	cout << "ctor of HelloBase ==> " << endl;
	// init();
	// cout << "ctor of HelloBase <== " << endl;
}

HelloBase::~HelloBase()
{
	cout << "dtor of HelloBase <==" << endl;
}

void HelloBase::init()
{
	// register this object
	cout << "init(): registerObject(): " << getName() << endl;
}
