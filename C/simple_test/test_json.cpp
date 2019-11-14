#include "test_json.h"
#include "test_func.h"

#include <iostream>
#include <iomanip>
#include <fstream>
#include <cctype>
#include <nlohmann/json.hpp>

const std::string JSONPATH = "../test.json";
nlohmann::json jv = {{"apple", 3.1415926535897932384626433832}, {"ball", 399}, {"egg", 25}};

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

void test_cbor()
{
    print_title(__func__);

    // explicit conversion to string
    std::string s = jv.dump();    // {\"happy\":true,\"pi\":3.141}
    std::cout << "size of string(jv): " << s.size() << std::endl;

    // serialize to CBOR
    std::vector<std::uint8_t> v_cbor = nlohmann::json::to_cbor(jv);
    std::cout << "size of v_cbor: " << v_cbor.size() << std::endl;

    // roundtrip
    nlohmann::json j_from_cbor = nlohmann::json::from_cbor(v_cbor);

    // inspect a field
    // will lose some precesion
    std::cout << "apple: " << j_from_cbor.at("apple") << std::endl;
#if 0
    std::vector<std::uint8_t>::iterator i;
    for (i = v_cbor.begin(); i != v_cbor.end(); ++i) {
        int c = isprint(*i);
        if (c) {
            std::cout << *i << std::endl;
        } else {
            std::cout << std::hex << c << std::endl;
        }
    }
#endif

}

void show_jsonhpp_version()
{
    print_title(__func__);
    using namespace std;

    cout << setw(4) << jv << endl;

    auto query = jv.meta();
    cout << "json.hpp version: " << query["version"]["string"] << endl;
}


void test_jsonhpp_related()
{
    show_jsonhpp_version();
    test_read_json();
    test_cbor();
}
