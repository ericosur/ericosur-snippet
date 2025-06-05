#!/bin/bash

# This script generates images with text using ImageMagick.
# Here uses hans characters. Need proper font to display them.

# image size
WIDTH=600
HEIGHT=800
# background color
BACKGROUND_COLOR="black"
# text color
TEXT_COLOR="white"
# font size
FONT_SIZE=80
# Here use Center
# North, South, West, East, NorthWest, NorthEast, SouthWest, SouthEast
GRAVITY="Center"


function generate() {
        local font=$1
        local text=$2
        local output_file=$3

        magick -size "${WIDTH}x${HEIGHT}" xc:"${BACKGROUND_COLOR}" \
                -gravity "${GRAVITY}" \
                -fill "${TEXT_COLOR}" \
                -font "${font}" \
                -pointsize "${FONT_SIZE}" \
                -annotate 0x0 "${text}" \
                "${output_file}"

        echo "Generated: '${output_file}'"
}


generate "Noto-Sans-CJK-TC" "萬事具備" "sans.png"
generate "Noto-Serif-CJK-TC" "只欠東風" "serif.png"
