/// file: myinc.h

#ifndef __MYINC_H__
#define __MYINC_H__

class MyInc
{
public:
    MyInc();

    int getValue() const;
    int getSecret() const;
private:
    int m_val;
    static const int SECRET = 1023;
};

#endif  // __MYINC_H__
