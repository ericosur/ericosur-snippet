// no library need to list
// need specify boost include file path while compiling
// $ g++ -I../../../boost_1_58_0/ -o first.app first.cpp

#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>

int main()
{
    using namespace boost::lambda;
    typedef std::istream_iterator<int> in;

    std::for_each(
        in(std::cin), in(), std::cout << (_1 * 3) << " " );

    return 0;
}
