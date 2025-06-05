#!/bin/bash

#
# This script will generate six images with text.
# and combine them into a different layout.
#

function generate_image() {
    local text=$1
    local output_file=$2

    magick -size 480x480 xc:"#2e2e2e" \
        -gravity Center \
        -fill "#ffd54a" \
        -font Ubuntu-Mono \
        -pointsize 80 \
        -annotate 0x0 "$text" \
        "$output_file"

    echo "Generated: '$output_file'"
}

function combine_tile() {
    local files=$1
    local tile=$2
    local output_file=$3

    # do not use quotes for files, will take as one file with space
    #         -frame 5   # add frame around each image
    magick montage $files \
        -mode Concatenate -tile "$tile" \
        -background "#2e2e2e" \
        "$output_file"

    echo "Combined images into $tile: '$output_file'"
}

files=""

for i in {1..6} ; do
    text="Image $i"
    ofn="image$i.png"
    files="$files $ofn"
    generate_image "$text" "$ofn"
done

echo "files: $files"
# two columns, three rows
combine_tile "$files" "2x3" "tile-2x3.png"
# three columns, two rows
combine_tile "$files" "3x2" "tile-3x2.png"
combine_tile "$files" "4x" "tile-4x.png"
