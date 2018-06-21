#include <iostream>
#include <fstream>
#include <iomanip> // for std::setw
#include <nlohmann/json.hpp>

#define MY_JSON_PATH    "../out.json"

using namespace std;

void test_stl()
{
    cout << "test function: " << __func__ << endl;
    vector<string> name;
    vector<int> age;

    name.push_back("apple");
    name.push_back("ball");
    name.push_back("cat");

    age.push_back(100);
    age.push_back(200);
    age.push_back(300);

    map<string, int> m;
    for (size_t i = 0; i < name.size(); ++i) {
        m[name[i]] = age[i];
    }

    nlohmann::json j_map = m;
    cout << j_map.dump(4) << endl;
}

void load_json()
{
    cout << "test function: " << __func__ << endl;

    ifstream infile(MY_JSON_PATH);
    using namespace nlohmann;
    json myjson;

    try {
        infile >> myjson;
        cout << setw(4) << myjson << endl;

        vector<string> vec = myjson["array"];
        for (auto i : vec) {
            cout << i << ' ';
        }
        cout << endl;
    } catch (json::parse_error& e) {
        cout << "[load_json] parse error:" << e.what() << endl;
    }
}

int main()
{
    test_stl();
    load_json();

    return 0;
}
