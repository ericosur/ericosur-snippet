#include <stdio.h>

/*
   See if it is ok to delete a null pointer?
*/

void testfunc(char* ptr)
{
	delete ptr;
}


int main()
{
	const int REPEAT = 100000;

	for (int i=0; i<REPEAT; i++)
	{
		testfunc(nullptr);
	}
}
