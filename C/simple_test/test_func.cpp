#include "test_func.h"

#include <iostream>
#include <fstream>
#include <iomanip>
#include <regex>
#include <nlohmann/json.hpp>

void print_title(const std::string& s)
{
    using namespace std;
    cout << "==========>> test: " << s << endl;
}


void test_read_json()
{
    print_title(__func__);

    using namespace std;
    try {
        std::ifstream infile(JSONPATH);
        nlohmann::json j;
        infile >> j;

        string smiles = j["smiles"].get<std::string>().c_str();
        cout << smiles << endl;

    } catch (nlohmann::json::parse_error& e) {
        // output exception information
        std::cout << "message: " << e.what() << '\n'
                  << "exception id: " << e.id << '\n'
                  << "byte position of error: " << e.byte << std::endl;
    }

}

void show_jsonhpp_version()
{
    print_title(__func__);
    using namespace std;
    nlohmann::json json = {{"apple", 31}, {"ball", 43}, {"egg", 71}};
    cout << setw(4) << json << endl;

    auto query = json.meta();
    cout << "json.hpp version: " << query["version"]["string"] << endl;
}

void test_string_connect()
{
    print_title(__func__);
    using namespace std;
    string s;
    s = string("color") + string("12345") + ".png";
    cout << s << endl;
}

void test_re()
{
    print_title(__func__);
    using namespace std;
    string s = "color1544508130.png";

    std::regex word_regex("(\\d+)");
    auto words_begin =
        std::sregex_iterator(s.begin(), s.end(), word_regex);
    auto words_end = std::sregex_iterator();

    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        std::string match_str = match.str();
        if (match_str.size()) {
            std::cout << match_str << '\n';
        }
    }
}

void test_noise()
{
    print_title(__func__);
    using namespace std;

    const int max_count = 10;
    for (int i=0; i<max_count; ++i) {
        double n = generateGaussianNoise(100.0, 15);
        cout << n << endl;
    }
}
