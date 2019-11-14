#include "test_func.h"

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <regex>

void print_title(const std::string& s)
{
    using namespace std;
    cout << "==========>> test: " << s << endl;
}

/**
 * dump() is a simple stupid dump function to see buffer in HEX
 * @param buf  [in] buffer to see
 * @param size_t [in] buffer size
 */
void dump(const char* buf, size_t size)
{
    for (size_t i=0; i<size; i++) {
        printf("%02X ", (unsigned char)buf[i]);
        if (i%16==15) {
            printf("\n");
        }
    }
    printf("\n");
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
    auto words_begin = std::sregex_iterator(s.begin(), s.end(), word_regex);
    auto words_end = std::sregex_iterator();

    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        std::string match_str = match.str();
        if (match_str.size()) {
            cout << match_str << '\n';
        }
    }

    // trying c++11 for-loop
    for (auto i: s) {
        cout << i << " ";
    }
    cout << endl;
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

void test_utfstring()
{
    print_title(__func__);
    const char s[] = "\U0001F60D \x35\u20e3  \U0001F631";
    std::cout << s << "\n";
    //const char t[] = "\uD83D\uDE1C";
    //std::cout << t << "\n";
}

void test_foo_string()
{
    print_title(__func__);
    const char foo[] = "The quick brown fox jumps over the lazy dog\0\0\0\0\0\x01\x02\x03\x04\x05";
    dump(foo, strlen(foo)+10);
    const char bar[] = "12345";
    dump(bar, strlen(bar)+1);
}

void test_lamb()
{
    using namespace std;
    print_title(__func__);
    int n = [](int x, int y) { return x+y; }(5, 4);
    cout << n << endl;

    auto lam = [](string s) { cout << s << endl; };
    lam(__func__);
}
