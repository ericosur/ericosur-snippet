#!/bin/bash

# need one argument for input file
# SRC=$1
# if [ -z "$SRC" ]; then
#     echo "Usage: $0 <file>"
#     exit 1
# fi

# need key_iv.txt
if [ ! -e key_iv.txt ]; then
    echo "key_iv.txt not found"
    exit 1
fi

#openssl enc -aes-256-cbc -e -in input.txt -out output.enc -pass pass:yourpassword -padding  # PKCS#7 (explicit, but default)
#openssl enc -aes-256-cbc -d -in output.enc -out decrypted.txt -pass pass:yourpassword -padding # PKCS#7 (explicit, but default)

# Extract the key and IV from key_iv.txt
# first line of key_iv.txt is KEY
KEY=$(sed -n 1,1p key_iv.txt | base64 -d | xxd -p | tr -d '\n')
echo "KEY: $KEY"
# 2nd line of key_iv.txt is IV
IV=$(sed -n 2,2p key_iv.txt | base64 -d | xxd -p | tr -d '\n')
echo " IV: $IV"

function encrypt_file() {
    local IF=$1
    local OF=$2
    local B64=$3

    echo -ne "===== encrypt_file =====\n$IF\t$OF\n"
    if [ "$B64" == "b64" ]; then
        echo "** apply base64 **"
    fi

    # check file exist
    if [ ! -f "$IF" ]; then
        echo "Input file $IF not found"
        return 1
    fi
    # check OF exist
    if [ -e "$OF" ]; then
        rm $OF
    fi

    if [ "$B64" == "b64" ]; then
        openssl enc -aes-256-cbc -e -in $IF -out $OF \
            -K $KEY -iv $IV -base64
    else
        openssl enc -aes-256-cbc -e -in $IF -out $OF \
            -K $KEY -iv $IV
    fi
    md5sum $OF
}

function decrypt_file() {
    local IF=$1
    local OF=$2
    local B64=$3

    echo -ne "===== decrypt_file =====\n$IF\t$OF\t"
    if [ "$B64" == "b64" ]; then
        echo -ne "** apply base64 **\n"
    else
        echo -ne "\n"
    fi

    # check file exist
    if [ ! -f "$IF" ]; then
        echo "Input file $IF not found"
        return 1
    fi
    # check file exist
    if [  -f "$OF" ]; then
        rm $OF
    fi

    if [ "$B64" == "b64" ]; then
        openssl enc -aes-256-cbc -d -in $IF -out $OF \
            -K $KEY -iv $IV -base64
    else
        openssl enc -aes-256-cbc -d -in $IF -out $OF \
            -K $KEY -iv $IV
    fi

    md5sum $OF
}

# encrypt
IF=a.zip
md5sum $IF
OF=a.zip.ssl.enc.b64
encrypt_file $IF $OF "b64"
OF=a.zip.ssl.enc
encrypt_file $IF $OF

# decrypt
OF=out.dec

IF=a.zip.ssl.enc.b64
decrypt_file $IF $OF "b64"

IF=a.zip.ssl.enc
decrypt_file $IF $OF

IF=a.zip.enc
decrypt_file $IF $OF

IF=a.zip.enc.b64
decrypt_file $IF $OF "b64"
