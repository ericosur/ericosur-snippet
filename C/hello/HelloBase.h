/// file: HelloBase.h
#ifndef __HELLOBASE_H__
#define __HELLOBASE_H__

#include <string>

using namespace std;

class HelloBase
{
public:
	~HelloBase();

	void init();

protected:
	// you cannot create HelloBase() object
	HelloBase();
	virtual string getName() = 0;

private:
};

#endif	// __HELLOBASE_H__
