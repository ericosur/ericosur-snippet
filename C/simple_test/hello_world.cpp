#include <iostream>
#include <iomanip>
#include <regex>
#include <nlohmann/json.hpp>
#include <time.h>

using namespace std;

double generateGaussianNoise(double mu, double sigma);

class HelloWorld
{
public:
	HelloWorld()  {
		cout << "hello world from " << __func__ << endl;
	}
};

// the ctor will be run before main()
HelloWorld hw;

void show_jsonhpp_version()
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

void test_string_connect()
{
    string s;
    s = string("color") + string("12345") + ".png";
    cout << s << endl;
}

void test_noise()
{
    const int max_count = 10;
    for (int i=0; i<max_count; ++i) {
        double n = generateGaussianNoise(100.0, 15);
        cout << n << endl;
    }
}

int main()
{
    srand(time(NULL));

    cout << "hello world from " << __func__ << endl;
	show_jsonhpp_version();
    //testre();
    test_string_connect();

    test_noise();

	return 0;
}
