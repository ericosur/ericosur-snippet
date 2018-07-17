// download from http://palatis.blogspot.com/2006/09/blog-post.html


/*
 * Meta-programming Infrastructure
 */

struct NullType { };

template <typename Head, typename Tail>
struct Typelist { };

/**
 * meta-(data structure) to store "X x Y = Z"
 */

template <unsigned int X, unsigned int Y>
struct ChartNode
{
    enum { first = X, second = Y, product = X * Y };
};

/**
 * Chart Maker...
 *
 * @param X, Y: current X and Y
 * @param XN, YN: max X and Y
 */

template <unsigned int X, unsigned int Y, unsigned int XN, unsigned int YN>
struct makeChart
{
    typedef Typelist< ChartNode<X, Y>, typename makeChart<X+1, Y, XN, YN>::Result > Result;
};

template <unsigned int Y, unsigned int XN, unsigned int YN>
struct makeChart<XN, Y, XN, YN>
{
    typedef Typelist< ChartNode<XN, Y>,
        Typelist< NullType, typename makeChart<1, Y+1, XN, YN>::Result > > Result;
};

template <unsigned int XN, unsigned int YN>
struct makeChart<XN, YN, XN, YN>
{
    typedef Typelist< ChartNode<XN, YN>, NullType > Result;
};

/**
 * Algorithm to write a ChartNodeList to an Ostream
 */
template <typename TList>
struct toOstream;

template <typename X, typename XS>
struct toOstream< Typelist<X, XS> > : toOstream< XS >
{
    template <typename OST, typename DELIM>
    OST & operator() (OST & dest, DELIM delim1, DELIM delim2)
    {
        dest << X::first << "x" << X::second << "=" << X::product << delim1;
        return toOstream<XS>::operator()(dest, delim1, delim2);
    }
};

template <typename XS>
struct toOstream< Typelist<NullType, XS> > : toOstream< XS >
{
    template <typename OST, typename DELIM>
    OST & operator() (OST & dest, DELIM delim1, DELIM delim2)
    {
        dest << delim2;
        return toOstream<XS>::operator()(dest, delim1, delim2);
    }
};

template <>
struct toOstream<NullType>
{
    template <typename OST, typename DELIM>
    OST & operator() (OST & dest, DELIM, DELIM delim2)
    {
        dest << delim2;
        return dest;
    }
};

/*
 * Main Program...
 */
#include <iostream>
#include <iterator>
using namespace std;

int main()
{
    enum { x = 9, y = 9 };
    cout << "make a Chart from [(1x1=1) .. (" << x << "x" << y << "=" << x*y << ")]:" << endl;

    typedef makeChart<1, 1, x, y>::Result ChartList;
    toOstream<ChartList> generator;
    generator(cout, ", ", "\n");

    return 0;
}
