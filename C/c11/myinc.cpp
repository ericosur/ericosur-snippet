/// file: myinc.cpp

#include "myinc.h"

MyInc::MyInc()
{
    m_val = 999;
}

int MyInc::getValue() const
{
    return m_val;
}

int MyInc::getSecret() const
{
    return SECRET;
}
