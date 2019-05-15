#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    std::vector<int> v{3,1,4,1,5,9,2,6,5,3,5,8,9};
    std::cout << "distance(first, last) = "
              << std::distance(v.begin(), v.end()) << '\n'
              << "distance(last, first) = "
              << std::distance(v.end(), v.begin()) << '\n';
               //the behavior is undefined (until C++11)
}
