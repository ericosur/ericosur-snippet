#include <iostream>
#include <iomanip>
#include <fstream>
#include <assert.h>
#include <nlohmann/json.hpp>
#include "dow.h"

using namespace std;

const bool DEBUG = false;

void show_v(std::vector<int>& v)
{
    for (auto x: v) {
        std::cout << x << ", ";
    }
    std::cout << std::endl;
}

void run_test(std::vector<int>& v)
{
    int y = v[0];
    int m = v[1];
    int d = v[2];
    int r = v[3];

    if (DEBUG) {
        cout << y << ", " << m << ", " << d << ": " << r;
    }

    int res = dow(y, m, d);
    if (DEBUG) {
        cout << "  got: " << res << endl;
    }
    assert(r == res);
    assert(r == dow2(y, m, d));
}

void read_json_and_run_tests()
{
    using json = nlohmann::json;
    using namespace std;

    const std::string JSONPATH = "../dow-test.json";
    try {
        ifstream infile(JSONPATH);
        json j;
        infile >> j;

        if (DEBUG) {
            cout << j << endl;
        }

        // iterate the array
        vector<int> v;
        for (json::iterator it = j.begin(); it != j.end(); ++it) {
            v = it->get<vector<int>>();
            run_test(v);
        }
    } catch (nlohmann::json::parse_error& e) {
        // output exception information
        std::cout << "message: " << e.what() << '\n'
                  << "exception id: " << e.id << '\n'
                  << "byte position of error: " << e.byte << std::endl;
    }

}

void show(int y, int m, int d)
{
    printf("dow of %d/%d/%d is %d\n", y, m, d, dow(y,m,d));
    printf("dow2 of %d/%d/%d is %d\n", y, m, d, dow2(y,m,d));
}

int main()
{
    cout << "running tests... ";
    read_json_and_run_tests();
    cout << "ok\n";

    show(2020, 12, 25);

    return 0;
}
