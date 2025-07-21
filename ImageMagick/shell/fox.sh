#!/bin/bash
#
# demo for annotate two lines
# **gravity** not used
#

VERSION=2025.07.21

# image size
WIDTH=1920
HEIGHT=1080
# background color
BACKGROUND_COLOR="black"
# text color
TEXT_COLOR="white"
# font size
FONT_SIZE=100
FONT_NAME="DejaVu-Serif"

#
# $1: output filename
# $2: line 1
# $3: line 2
#
annote() {
	local output_file=$1
    local text1=$2
    local text2=$3

    magick -size "${WIDTH}x${HEIGHT}" xc:"${BACKGROUND_COLOR}" \
            -fill "${TEXT_COLOR}" \
            -font "${FONT_NAME}" \
            -pointsize "${FONT_SIZE}" \
            -annotate +80+250 "${text1}" \
            -annotate +80+400 "${text2}" \
            "${output_file}"
    echo "Generated: '${output_file}'"
}

annote "fox.png" "A quick fox jumps over" "the lazy dog"
