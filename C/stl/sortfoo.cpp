#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <random>

using namespace std;

class Foo {
public:
    Foo(const string& s, int v) {
        str = s;
        val = v;
    }

    string str;
    int val;

    bool operator<(const Foo& g) {
        return this->val < g.val;
    }
    bool operator==(const Foo& g) {
        return this->val == g.val;
    }
    bool operator!=(const Foo& g) {
        return this->val != g.val;
    }
    bool operator>(const Foo& g) {
        return this->val > g.val;
    }
    bool operator>=(const Foo& g) {
        return this->val >= g.val;
    }
    bool operator<=(const Foo& g) {
        return this->val <= g.val;
    }
};


std::ostream& operator<<(std::ostream& ds, const Foo& obj)
{
    ds << obj.str << "," << obj.val;
    return ds;
}

void printsep()
{
    std::cout << "----------\n";
}


template<typename T>
void dump(std::vector<T> v)
{
    for (auto a: v) {
        std::cout << a << std::endl;
    }
    printsep();
}

int main()
{
    std::vector<Foo> s;

    s.push_back(Foo("alpha", 41));
    s.push_back(Foo("beta", 79));
    s.push_back(Foo("gamma", 13));
    s.push_back(Foo("victor", 73));
    s.push_back(Foo("roger", 67));
    // initial values
    dump(s);

    struct {
        bool operator()(Foo m, Foo n) {
            return m > n;
        }
    } customGreater;

    // sort with customized class
    std::sort(s.begin(), s.end(), customGreater);
    dump(s);

    random_device rd;
    mt19937 g(rd());

    // shuffle it
    std::shuffle(s.begin(), s.end(), g);
    dump(s);

    return 0;
}
