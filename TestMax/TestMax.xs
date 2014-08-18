#include "EXTERN.h"
#include "perl.h"
#include "XSUB.h"

#include "ppport.h"


MODULE = TestMax		PACKAGE = TestMax

int Max(int a, int b)
CODE:
        RETVAL = (a > b) ? a : b;
OUTPUT:
        RETVAL
