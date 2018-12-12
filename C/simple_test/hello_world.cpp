#include <iostream>
#include <iomanip>
#include <regex>
#include <nlohmann/json.hpp>

using namespace std;

class HelloWorld
{
public:
	HelloWorld()  {
		cout << "hello world from " << __func__ << endl;
	}
};

// the ctor will be run before main()
HelloWorld hw;

void test()
{
	nlohmann::json json = {{"apple", 31}, {"ball", 43}, {"egg", 71}};
	cout << setw(4) << json << endl;

    auto query = json.meta();
    cout << "json.hpp version: " << query["version"]["string"] << endl;
}

void testre()
{
    cout << __func__ << endl;
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

void what()
{
    string s;
    s = string("color") + string("12345") + ".png";
    cout << s << endl;
}

int main()
{
    cout << "hello world from " << __func__ << endl;
	//test();
    //testre();
    what();

	return 0;
}
