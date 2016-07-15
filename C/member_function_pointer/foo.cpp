#include <iostream>
#include "foo.h"

using namespace std;

foo::foo()
{
    init();
}

void foo::setPolicy(FOOENUM f)
{
    switch (f) {
    case FOO_PUBLIC:
    case FOO_HIGH:
        m_fp = &foo::pub_setval;
        break;
    case FOO_PROTECTED:
    case FOO_MIDDLE:
        m_fp = &foo::pro_setval;
        break;
    case FOO_PRIVATE:
    case FOO_LOW:
        m_fp = &foo::pri_setval;
        break;
    }
}

void foo::init()
{
    m_value = 0;
    m_fp = NULL;
}

// it's public
void foo::pub_setval()
{
    m_value = 999;
}

// it's protected
void foo::pro_setval()
{
    m_value = 799;
}

// it's private
void foo::pri_setval()
{
    m_value = 199;
}

int foo::getValue()
{
    if (m_fp) {
        // both are ok
        // (*this.*m_fp)();
        (this->*m_fp)();
    }
    return m_value;
}
