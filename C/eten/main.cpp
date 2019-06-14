#include "fontutil.h"
#ifdef USE_ICONV
#include "try_iconv.h"
#endif
#include <mytool.h>

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;


bool draw_char_bitmap(const uint8_t* char_buf)
{
    const double scale = 2.0;
    size_t dst_size = BYTE_PER_CHAR * 8;
    uint24_t dst[dst_size];
    convert_bit_to_8uc3(char_buf, BYTE_PER_CHAR, dst, dst_size);

    cv::Mat img(FONT_HEIGHT, FONT_WIDTH, CV_8UC3, (uint8_t*)dst);
    if (scale != 1.0) {
        cv::resize(img, img, cv::Size(), scale, scale);
    }

    cv::imshow("result", img);
    if ( cv::waitKey(0) == 0x1B ) {
        return false;
    } else {
        return true;
    }
}


void show_big5_char_from_vector(std::vector<uint16_t>& big5s)
{
    //printf("try_class\n");
    Fontutil* fu = Fontutil::getInstance();
    if (!fu->isLoaded()) {
        printf("cannot init font loading...\n");
        return;
    }

    //printf("here...\n");
    uint8_t buf[BYTE_PER_CHAR];
    for (vector<uint16_t>::iterator it = big5s.begin() ; it != big5s.end() ; it++) {
        //cout << *it << endl;
        if ( fu->load_one_character_by_big5(*it, buf) ) {
            if (!draw_char_bitmap(buf))
                break;
        }
    }
}

int main(int argc, char** argv)
{
    if (argc == 1) {
        vector<uint16_t> big5s = {
            0xA4D1, 0xB0AE, 0xAAAB, 0xC0EA, 0xA141, 0xA470, 0xA4DF, 0xA4F5, 0xC0EB
        };
        printf("Usage: eten [setting.json]\n");
        printf("use default demo...\n");
        show_big5_char_from_vector(big5s);
    } else if ( mytool::is_file_exist(argv[1]) ) {
#ifdef USE_ICONV
        printf("use load utf-8 string from setting.json and iconv to big5 code\n");

        // load string from jsonfile, it is utf-8 encoding
        string str = mytool::get_string_from_jsonfile(argv[1], "string", "");
        //cout << str << endl;

        // use iconv convert to big5
        char* big5buf = ConvertEnc("UTF-8", "BIG5", str.c_str());
        //cout << big5buf << endl;
        //dump((const uint8_t*)big5buf, strlen(big5buf));

        // put big5buf into big5s
        std::vector<uint16_t> v;
        for (size_t i=0; i<strlen(big5buf); i+=2) {
            uint16_t val = (uint8_t)big5buf[i] << 8 | (uint8_t)big5buf[i+1];
            //cout << hex << val << endl;
            v.push_back(val);
        }
        show_big5_char_from_vector(v);
#else
        printf("use load big5 list from setting.json\n");
        // load big5 code vector
        vector<string> keys = {"big5s"};
        vector<string> hexstrs = mytool::get_vector_from_jsonfile(argv[1], keys);
        std::vector<uint16_t> v;
        for (vector<string>::iterator it=hexstrs.begin(); it!=hexstrs.end(); it++) {
            //cout << *it << endl;
            uint16_t val = (uint16_t)strtoul(it->c_str(), nullptr, 16);
            v.push_back(val);
        }
        show_big5_char_from_vector(v);
#endif
    }

    return 0;
}
