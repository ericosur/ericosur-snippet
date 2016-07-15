#ifndef __FOO_H__
#define __FOO_H__

class foo;
typedef void (foo::*SetterFp)();

class foo
{
public:
    foo();

    enum FOOENUM {
        FOO_PUBLIC,
        FOO_HIGH,
        FOO_PROTECTED,
        FOO_MIDDLE,
        FOO_PRIVATE,
        FOO_LOW,
    };

public:
    void pub_setval();
    int getValue();
    void setPolicy(FOOENUM f);

protected:
    void init();
    void pro_setval();

private:
    void pri_setval();

private:
    int m_value;
    SetterFp m_fp;
};

#endif  // __FOO_H__
