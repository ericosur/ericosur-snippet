#include "fontutil.h"

void dump(const uint8_t* buffer, size_t size)
{
    const size_t BYTE_PER_LINE = 16;
    for (size_t i = 0; i < size; i++) {
        if (i && i % BYTE_PER_LINE == 0) {
            printf("\n");
        }
        printf("%02X ", (uint8_t)buffer[i]);
    }
    printf("\n");
}


// size of char_buffer is uint8_t buffer[BYTE_PER_CHAR]
void load_one_character_24x24(uint16_t id, uint8_t* char_buffer)
{
    if (id >= MAX_CHARCOUNT) {
        printf("error: id is out-of-range: %d\n", id);
        return;
    }

    FILE* fptr = fopen(FONT_FILEPATH, "rb");
    if (fptr == NULL) {
        printf("error: fptr is null\n");
        return;
    }

    if ( fseek(fptr, id*BYTE_PER_CHAR, SEEK_SET) != 0 ) {
        printf("error: errno: %d\n", errno);
        fclose(fptr);
        return;
    }

    size_t rd = fread(char_buffer, sizeof(uint8_t), BYTE_PER_CHAR, fptr);
    if (rd != BYTE_PER_CHAR) {
        printf("error: read byte not matched, rd: %d\n", (int)rd);
    }

    fclose(fptr);
}

// dst_size = src_size * 8
// caller should allocate enough space to store data
void convert_bit_to_8uc1(uint8_t* src, size_t src_size, uint8_t* dst, size_t dst_size)
{
    //Mat fontimg( FONT_HEIGHT, FONT_WIDTH, CV_8UC1 );

    size_t p = 0;
    for (size_t i = 0; i < src_size; ++i) {
        uint8_t c = src[i];

        // 8 bits to 8 bytes
        dst[p++] = (c >> 7) & 1;
        dst[p++] = (c >> 6) & 1;
        dst[p++] = (c >> 5) & 1;
        dst[p++] = (c >> 4) & 1;
        dst[p++] = (c >> 3) & 1;
        dst[p++] = (c >> 2) & 1;
        dst[p++] = (c >> 1) & 1;
        dst[p++] = c & 1;
        //printf("p:%u\n", p);
    }

    if (p != dst_size) {
        printf("error: size not match: p: %d\n", (int)p);
    }
}

// dst_size = src_size * 8
// caller should allocate enough space to store data
void convert_bit_to_8uc3(const uint8_t* src, const size_t src_size, uint24_t* dst, size_t dst_size)
{
    //Mat fontimg( FONT_HEIGHT, FONT_WIDTH, CV_8UC1 );

    #define SET_PIXEL(b) \
        if (b) { \
            UINT24_SET(dst[p], 0x00FFFFFF); \
        } else { \
            UINT24_SET(dst[p], 0); \
        } \
        p++

    size_t p = 0;
    for (size_t i = 0; i < src_size; ++i) {
        uint8_t c = src[i];

        SET_PIXEL(((c >> 7) & 1));
        SET_PIXEL(((c >> 6) & 1));
        SET_PIXEL(((c >> 5) & 1));
        SET_PIXEL(((c >> 4) & 1));
        SET_PIXEL(((c >> 3) & 1));
        SET_PIXEL(((c >> 2) & 1));
        SET_PIXEL(((c >> 1) & 1));
        SET_PIXEL((c & 1));

        //printf("p:%d\n", (int)p);
    }

    if (p != dst_size) {
        printf("error: size not match: p: %d\n", (int)p);
    }
}

/*
  stdfont.24? │標準字型│ 常用字 │A440-C67E │5401│
  (hanstd.24) │        │次常用字│C940-F9D5 │7652│
  from: http://140.134.32.129/fcu/lego/word_r.c
*/
bool big5_to_index(const uint16_t big5, uint16_t& index)
{
    uint8_t hb = big5 >> 8;
    uint8_t lb = big5 & 0x00FF;

    index = 0;

    if (hb >= 0xC6 && hb <= 0xC9 && lb <= 0xF2) {
        if (hb == 0xC6) {
            index = (hb - 0xC6) * 157;
            index += lb - 0xA1;
        } else {
            index = (hb - 0xC7) * 157 + 94;
            index += (lb >= 0xA1) ? (lb - 0xA1 + 63) : (lb - 0x40);
        }
        // it is japfont24
        return false;
    }
    if ((hb>=0xa4 && hb<=0xc6) || (hb>=0xc9 && hb<=0xf9)) {
        if ((lb>=0x40 && lb<=0x7e) || (lb>=0xa1 && lb<=0xfe)) {
            index = (hb>=0xc9) ? ((hb-0xc9)*157+5401) : ((hb-0xa4)*157);
            index += (lb>=0xa1) ? (lb-0xa1+63) : (lb-0x40);
            // it is in stdfont
            return true;
        }
    }
    if (hb>=0xa1 && hb<=0xa3) {
        if ((lb>=0x40 && lb<=0x7e) || (lb>=0xa1 && lb<=0xfe)) {
            index = (hb - 0xa1) * 157;
            index += (lb>=0xa1) ? (lb-0xa1+63) : (lb-0x40);
            // it is in spcfont
            return false;
        }
    }
    return false;
}

Fontutil* Fontutil::_instance = NULL;
Fontutil* Fontutil::getInstance()
{
    if (_instance == NULL) {
        _instance = new Fontutil();
    }
    printf("and returns instance\n");
    return _instance;
}

Fontutil::Fontutil()
{
    bzero(stdfont, BYTE_PER_CHAR*MAX_CHARCOUNT);
    load();
}

void Fontutil::load()
{
    if ( load_fontfile() ) {
        bFontLoaded = true;
    } else {
        bFontLoaded = false;
    }
}

bool Fontutil::load_fontfile()
{
    FILE* fptr = fopen(FONT_FILEPATH, "rb");
    if (fptr == NULL) {
        printf("error: fptr is null\n");
        return false;
    }

    size_t rd = fread(stdfont, sizeof(uint8_t), BYTE_PER_CHAR * MAX_CHARCOUNT, fptr);
    if (rd != BYTE_PER_CHAR * MAX_CHARCOUNT) {
        printf("warning: read byte not matched, rd: %d\n", (int)rd);
    }

    fclose(fptr);
    return true;
}

bool Fontutil::load_one_character_by_id(const uint16_t id, uint8_t* char_buffer)
{
    if (id >= MAX_CHARCOUNT) {
        printf("error: id is out-of-range: %d\n", id);
        return false;
    }

    if (!bFontLoaded) {
        printf("error: font is not loaded\n");
        return false;
    }

    bzero(char_buffer, BYTE_PER_CHAR);
    memcpy(char_buffer, &stdfont[id*BYTE_PER_CHAR], BYTE_PER_CHAR);
    return true;
}

bool Fontutil::big5_to_index(const uint16_t big5, uint16_t& index)
{
    uint8_t hb = big5 >> 8;
    uint8_t lb = big5 & 0x00FF;

    index = 0;

    if (hb >= 0xC6 && hb <= 0xC9 && lb <= 0xF2) {
        if (hb == 0xC6) {
            index = (hb - 0xC6) * 157;
            index += lb - 0xA1;
        } else {
            index = (hb - 0xC7) * 157 + 94;
            index += (lb >= 0xA1) ? (lb - 0xA1 + 63) : (lb - 0x40);
        }
        // it is japfont24
        return false;
    }
    if ((hb>=0xa4 && hb<=0xc6) || (hb>=0xc9 && hb<=0xf9)) {
        if ((lb>=0x40 && lb<=0x7e) || (lb>=0xa1 && lb<=0xfe)) {
            index = (hb>=0xc9) ? ((hb-0xc9)*157+5401) : ((hb-0xa4)*157);
            index += (lb>=0xa1) ? (lb-0xa1+63) : (lb-0x40);
            // it is in stdfont
            return true;
        }
    }
    if (hb>=0xa1 && hb<=0xa3) {
        if ((lb>=0x40 && lb<=0x7e) || (lb>=0xa1 && lb<=0xfe)) {
            index = (hb - 0xa1) * 157;
            index += (lb>=0xa1) ? (lb-0xa1+63) : (lb-0x40);
            // it is in spcfont
            return false;
        }
    }
    return false;
}
