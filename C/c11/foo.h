#ifndef __FOO_H__
#define __FOO_H__

class Foo
{
public:
     int a = 1;       //C++11 only
     const int b = 9; //C++11 only
     //This works fine (both in C++03 and C++11)
     static const int c = 10;

     const int arr[5] = {1,2,3,4,5};
};

#endif  // __FOO_H__
