#ifndef __FONT_UTIL_H__
#define __FONT_UTIL_H__

#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include "uint24_t.h"

#define MAX_CHARCOUNT       (13094)
#define FONT_FILEPATH       "../stdfont.24f"
#define BYTE_PER_CHAR       72
#define FONT_WIDTH          24
#define FONT_HEIGHT         24

void dump(const uint8_t* buffer, size_t size);
void load_one_character_24x24(uint16_t id, uint8_t* char_buffer);

// dst_size = src_size * 8
// caller should allocate enough space to store data
void convert_bit_to_8uc1(uint8_t* src, size_t src_size, uint8_t* dst, size_t dst_size);
void convert_bit_to_8uc3(const uint8_t* src, const size_t src_size, uint24_t* dst, size_t dst_size);
bool big5_to_index(const uint16_t big5, uint16_t& index);

class Fontutil
{
public:
    static Fontutil* getInstance();

    bool isLoaded() const {
        return bFontLoaded;
    }

    bool load_one_character_by_id(const uint16_t id, uint8_t* char_buffer);
    bool big5_to_index(const uint16_t big5, uint16_t& index);

protected:
    Fontutil();
    static Fontutil* _instance;

    void load();
    bool load_fontfile();

private:
    uint8_t stdfont[BYTE_PER_CHAR * MAX_CHARCOUNT]; // byte size of stdfont.24
    bool bFontLoaded = false;
};



#endif  // __FONT_UTIL_H__
