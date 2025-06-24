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
                -annotate -45x-45 "${text}" \
                "${output_file}"

        echo "Generated: '${output_file}'"
}

# Noto-Serif-CJK-TC-Bold
# Noto-Sans-CJK-TC
# AR-PL-UKai-TW, AR-PL-UKai-TW-MBE
# AR-PL-UMing-TW
generate "Noto-Serif-CJK-TC-Bold" "豆腐TC襯線\n相煎太急" "notoserif.png"
generate "AR-PL-UKai-TW" "AR楷書\n舉一反三" "arkai.png"
generate "AR-PL-UMing-TW" "AR明體\n學富五車" "arming.png"
# Noto-Color-Emoji / Noto-Emoji (you cannot use color emoji in this way)
generate "Noto-Emoji" "🧃🧊🧇🧄🧅🧉🧆🧈\n🦮🐕‍🦺🦧🦦🦥🦩🦨🦪" "emoji.png"
