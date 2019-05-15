#include <iostream>
#include <random>
#include <algorithm>
#include <iterator>

void dump_vector(const std::vector<int>& v)
{
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
}


float get_median(std::vector<int>& v)
{
    float ans = 0;

    // cannot get median number for a unsorted vector
    if (!std::is_sorted(v.begin(), v.end())) {
        std::cout << "[FAIL] input vector is not sorted\n";
        return 0;
    }

    std::nth_element(v.begin(), v.begin() + v.size()/2, v.end());
    auto id1 = v.size() / 2;
    if ( v.size() % 2 ) {   // size is odd
        ans = v[id1];
    } else {    // size is even
        if (v.size() / 2 >= 1) {
            auto id0 = v.size() / 2 - 1;
            ans = (v[id0] + v[id1]) / 2.0;
        }
    }

    return ans;
}

void do_avg(const std::vector<int>& v)
{
    int sum = std::accumulate(v.cbegin(), v.cend(), 0);
    float avg = float(sum / v.size());

    std::vector<int> dst(v.size());
    std::copy(v.cbegin(), v.cend(), dst.begin());
    float median = get_median(dst);
    std::cout << "sum: " << sum << std::endl
              << "avg: " << avg << std::endl
              << "median: " << median << std::endl;
    std::cout << "dist: " << std::distance(v.cbegin(), v.cend()) << "\n";
}

void test()
{
    using namespace std;

    const size_t VECTOR_SIZE = 10;
    vector<int> v(VECTOR_SIZE);
    std::iota(v.begin(), v.end(), 1);   // 1, 2, .. 9, 10

    vector<int> m(v.size());
    vector<int> n(v.size());

    // copy v to m
    std::copy(v.begin(), v.end(), m.begin());

    random_device rd;
    mt19937 g(rd());

    cout << "shuffled =====>\n";
    shuffle(v.begin(), v.end(), g);
    // copy shuffled v to n
    std::copy(v.begin(), v.end(), n.begin());
    dump_vector(v);
    do_avg(v);

    cout << "sorted =====>\n";
    sort(v.begin(), v.end());
    dump_vector(v);
    do_avg(v);

    cout << "inner_product =====>\n";
    int ip = std::inner_product(m.begin(), m.end(), n.begin(), 0);
    cout << "ip = " << ip << endl;
}

int main()
{
    test();

    return 0;
}
