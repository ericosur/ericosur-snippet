/**
 * original code comes from:
 * http://www.zedwood.com/article/cpp-is-valid-utf8-string-function
 * license: CC BY-SA 3.0
 *
 * modified to show more log
 */
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool utf8_check_is_valid(const string& string);

void test(const string& s)
{
    bool r = utf8_check_is_valid(s);
    cout << "test...[" << s << "]\n";
    if (r) {
        cout << "\t\tis valid\n";
    } else {
        cout << "\t\tis not valid\n";
    }
}

int main(int argc, char *argv[])
{
    vector<string> list = {
        // "hello world",
        // "ol\xc3\xa1 mundo",
        // "\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c",
        // "\xa0\xa1", // invalid
        "\xe6\xb5\xaa" "\xe6\xb7\x98" "\xe6\xb2\x99",   // valid
        "\xe6\xb5\xaa" "\xe6\xb7\x98" "\xe6\xb2",   // invalid, lost last byte of 3rd char
        "\xe6\xb5\xaa" "\xe6\xb7\x98" "\xe6",   // invalid, lost 2 bytes of 3rd char
        "\xe6\xb5\xaa" "\xe6\xb7" "\xe6\xb2\x99",   // invalid, lost last bytes of 2nd char
        "\xe6\xb5\xaa" "\xe6" "\xe6\xb2\x99",   // invalid, lost 2 bytes of 2nd char
        // "\xed\x9f\xbf",
        // "\xee\x80\x80",
        // "\xef\xbf\xbd",
        // "\xf4\x8f\xbf\xbf",
        // "\xf4\x90\x80\x80",
    };

    vector<string>::iterator i;
    for (i = list.begin(); i != list.end(); ++i) {
        test(*i);
    }
    cout << endl;
    return 0;
}
//more invalid strings to test: http://stackoverflow.com/questions/1301402/example-invalid-utf8-string
// https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
bool utf8_check_is_valid(const string& string)
{
    bool result = true;
    int i;
    int ix = string.length();
    for (i=0; i < ix; i++) {
        int c = (unsigned char) string[i];
        int n = -1;
        //if (c==0x09 || c==0x0a || c==0x0d || (0x20 <= c && c <= 0x7e) ) n = 0; // is_printable_ascii
        if (0x00 <= c && c <= 0x7f) {
            n=0; // 0bbbbbbb
        } else if ((c & 0xE0) == 0xC0) {
            n=1; // 110bbbbb
        } else if ( c==0xed && i<(ix-1) && ((unsigned char)string[i+1] & 0xa0)==0xa0) {
            //U+d800 to U+dfff
            cout << "[FAIL] invalid code point";
            result = false;
            break;
        } else if ((c & 0xF0) == 0xE0) {
            n=2; // 1110bbbb
        } else if ((c & 0xF8) == 0xF0) {
            n=3; // 11110bbb
        }
        //else if (($c & 0xFC) == 0xF8) n=4; // 111110bb //byte 5, unnecessary in 4 byte UTF-8
        //else if (($c & 0xFE) == 0xFC) n=5; // 1111110b //byte 6, unnecessary in 4 byte UTF-8
        else {
            cout << "[FAIL] \\x" << hex << c << " is not a valid char" << dec << endl;
            result = false;
            break;
        }

        for (int j=0; j<n && i<ix; j++) { // n bytes matching 10bbbbbb follow ?
            if (++i == ix) {
                printf("[FAIL] not enough byte, at i(%d) j(%d) n(%d) ix(%d)\n", i, j, n, ix);
                return false;
            }
            if (((unsigned char)string[i] & 0xC0) != 0x80) {
                printf("[FAIL] not legal byte, at i(%d) j(%d) n(%d) ix(%d)\n", i, j, n, ix);
                return false;
            }
        }
    }
    if (!result) {
        cout << "break at:" << i << endl;
    }
    return result;
}
