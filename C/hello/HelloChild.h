#ifndef __HELLOCHILD_H__
#define __HELLOCHILD_H__

#include "HelloBase.h"

class HelloChild : public HelloBase
{
public:
	HelloChild();

	virtual string getName();
};

#endif	// __HELLOCHILD_H__
