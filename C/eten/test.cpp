#include "test.h"


void test()
{
    uint8_t buf[BYTE_PER_CHAR];
    const uint16_t test_id = 1000;

    bzero(buf, BYTE_PER_CHAR);
    load_one_character_24x24(test_id, buf);
    //dump(buf, BYTE_PER_CHAR);

    size_t dst_size = BYTE_PER_CHAR * 8;
    uint8_t dst[dst_size];
    convert_bit_to_8uc1(buf, BYTE_PER_CHAR, dst, dst_size);
    printf("\n");
    //dump(dst, dst_size);

    cv::Mat src(FONT_HEIGHT, FONT_WIDTH, CV_8UC1, dst);
    cv::Mat img(FONT_HEIGHT, FONT_WIDTH, CV_8UC3);

    cv::cvtColor(src, img, CV_GRAY2RGB);
    cv::Mat big;
    cv::resize(img, big, cv::Size(), 8.0, 8.0);
    cv::imshow("result", big);
    cv::waitKey(0);
    //cv::imshow( "result", img );
}

void test0(uint8_t val)
{
    const uint8_t src_size = 1;
    uint8_t src[src_size];
    const size_t dst_size = src_size * 8;
    uint24_t dst[dst_size];

    bzero(dst, dst_size*3);
    src[0] = val;
    convert_bit_to_8uc3(src, src_size, dst, dst_size);
    dump((uint8_t*)dst, dst_size*3);
}

void show_char_bitmap(const uint16_t test_id)
{
    uint8_t buf[BYTE_PER_CHAR];

    bzero(buf, BYTE_PER_CHAR);
    load_one_character_24x24(test_id, buf);
    //dump(buf, BYTE_PER_CHAR);
    draw_char_bitmap(buf);
}

void show_big5(const uint16_t big5)
{
    uint16_t index = 0;
    bool res = big5_to_index(big5, index);
    if (res) {
        printf("big5: %04X index:%d\n", big5, index);
        show_char_bitmap(index);
    } else {
        printf("not a big5 code, or it is spcfont, japfont: big5: %04X\n", big5);
    }
}



