#include <stdio.h>
#include "mymat.h"

void test0()
{
    MyMat m;
    m.dump();
}

void test1()
{
    MyMat m(2,3);
    MyMat n(3,2);

    try {
        m.set(0,0,1);
        m.set(0,1,2);
        m.set(0,2,3);
        m.set(1,0,4);
        m.set(1,1,5);
        m.set(1,2,6);
    } catch (char const* s) {
        printf("invalid m: %s\n", s);
    }
    m.dump();

    try {
        n.set(0,0,7);
        n.set(0,1,8);
        n.set(1,0,9);
        n.set(1,1,10);
        n.set(2,0,11);
        n.set(2,1,12);
    } catch(char const* s) {
        printf("invalid n: %s\n", s);
    }
    n.dump();

    try {
        MyMat ans = m.cross(n);
        //printf("ans: row: %d, col: %d\n", m.row, m.col);
        ans.dump();
    } catch(char const* s) {
        printf("s:%s\n", s);
    }
}

void test2()
{
    MyMat m(1024,2048);
    MyMat n(2048,1024);
    MyMat ans = m.cross(n);
}

int main()
{
    test2();
    return 0;
}
