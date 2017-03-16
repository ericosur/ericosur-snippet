#include <algorithm>
#include <functional>
//#include <array>
#include <vector>
#include <iostream>

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

int main()
{
    std::vector<Foo> s;

    s.push_back(Foo("alpha", 41));
    s.push_back(Foo("beta", 79));
    s.push_back(Foo("gamma", 13));
    s.push_back(Foo("victor", 73));
    s.push_back(Foo("roger", 67));

    for (auto ii : s) {
        std::cout << ii << endl;
    }
    cout << "-----" << endl;

    struct {
        bool operator()(Foo m, Foo n) {
            return m > n;
        }
    } customGreater;

    std::sort(s.begin(), s.end(), customGreater);
    for (auto a : s) {
        std::cout << a << endl;
    }


    return 0;
}
