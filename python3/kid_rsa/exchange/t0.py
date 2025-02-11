#!/usr/bin/env python3
# coding: utf-8

'''
test key and iv
'''

import os
import re
import sys
from binascii import hexlify
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from loguru import logger
from keyiv import from_file, from_env, save_bin

sys.path.insert(0, '../../')
from myutil import md5sum, prt

logd = logger.debug

def show_val(msg: str, val: bytes) -> None:
    ''' show bytes in hex string '''
    show_val = hexlify(val).decode('utf-8')
    logd(f'{msg}: {show_val}')

def get_keyiv_frombin() -> tuple:
    ''' get key and iv in bytes
        will return None, None if any file is missing
    '''
    KFILE = 'key.bin'
    IVFILE = 'iv.bin'
    try:
        key = from_file(KFILE)
        iv = from_file(IVFILE)
    except FileNotFoundError as err:
        logd(f'no key file: {err}')
        return None, None
    return key, iv

def encrypt_file(in_file: str, key: bytes, iv: bytes) -> bytes:
    '''
    given in_file, out_file, key, iv
    encrypt the file with AES/CBC/PKCS7Padding
    '''
    with open(in_file, 'rb') as in_fobj:
        plain_text = in_fobj.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # padding for AES block size, not for base64
    padded_data = pad(plain_text, AES.block_size, style='pkcs7')
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def decrypt_data(data: bytes, key: bytes, iv: bytes) -> bytes:
    '''
    given data, key, iv
    decrypt the data with AES/CBC/PKCS7Padding
    '''
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(data), AES.block_size, style='pkcs7')
    return decrypted_data

def decrypt_file(in_file: str, key: bytes, iv: bytes) -> bytes:
    '''
    given in_file, key, iv
    decrypt the file with AES/CBC/PKCS7Padding
    input file could be base64 either binary
    '''
    data = b''
    with open(in_file, 'rb') as in_fobj:
        data = in_fobj.read()

    while True:
        if len(data) % 4 != 0:
            break

        pattern = re.compile(b'^[A-Za-z0-9+/]+={0,2}$')
        if pattern.match(data):
            data = base64.b64decode(data)
            logd('base64 decoded')
        break

    return decrypt_data(data, key, iv)

class Solution():
    ''' solution '''
    INPUT_FILE = 'a.zip'
    ENC_FILE = 'a.zip.enc'
    ENCB64_FILE = 'a.zip.enc.b64'   # base64 encoded, multiple lines
    ENCB641_FILE = 'a.zip.enc1.b64' # base64 encoded, single line
    DEC_FILE = 'a.zip.dec'
    DECB64_FILE = 'a.zip.b64.dec'    # from multiple lines
    DECB641_FILE = 'a.zip.b641.dec' # from single line
    KEYIV_FILE = 'key_iv.txt'

    def __init__(self):
        self.key = None
        self.iv = None
        self.__get_keyiv()
        self.need_save = False

    def __get_keyiv(self) -> None:
        ''' get key and iv '''
        logd('hello world')
        key, iv = get_keyiv_frombin()
        if key and iv:
            show_val('key from bin:', key)
            show_val(' iv from bin:', iv)
        else:
            logd('no key file, then get from env...')
            self.need_save = True
        if key is None or iv is None:
            key = from_env('KEY', 32)
            iv = from_env('IV', 16)
            show_val('key2', key)
            show_val('iv2', iv)
        self.key = key
        self.iv = iv

    def save_keyiv(self) -> None:
        ''' save key and iv into a base64 two lines file '''
        # Save the key and IV to a file,
        # first line is key, 2nd line is iv, in base64
        with open(self.KEYIV_FILE, 'wb') as fobj:
            k64 = base64.b64encode(self.key)
            i64 = base64.b64encode(self.iv)
            fobj.write(k64 + b'\n' + i64 +b'\n')
        logd(f'save keyiv: {self.KEYIV_FILE}')

    def encode_file(self, ofile: str, data: bytes) -> None:
        ''' base64 encode data to file w/ multiple lines '''
        LINE_LENGTH = 64
        encoded_data = base64.b64encode(data)
        with open(ofile, 'wb') as f:
            for i in range(0, len(encoded_data), LINE_LENGTH):
                f.write(encoded_data[i:i+LINE_LENGTH] + b'\n')

    def encrypt_file(self):
        ''' encrypt file '''
        encrypted_data = encrypt_file(self.INPUT_FILE, self.key, self.iv)
        save_bin(self.ENC_FILE, encrypted_data)
        prt(f'output file: {self.ENC_FILE}')

        b64_encrypted_data = base64.b64encode(encrypted_data)
        save_bin(self.ENCB641_FILE, b64_encrypted_data)
        prt(f'output file: {self.ENCB641_FILE}')

        self.encode_file(self.ENCB64_FILE, encrypted_data)
        prt(f'output file: {self.ENCB64_FILE}')

    def decrypt_file(self):
        ''' decrypt file '''
        decrypted_data = decrypt_file(self.ENC_FILE, self.key, self.iv)
        save_bin(self.DEC_FILE, decrypted_data)
        #logd(f'decrypt to file: {self.DEC_FILE}')

    def decrypt_b64_file_multipleline(self):
        ''' decrypt a base64 file
            the base64 is multiple lines (64 char per line)
        '''
        data = b''
        prt(f'decrypt: {self.ENCB64_FILE}')
        with open(self.ENCB64_FILE, "rt") as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                data += ln.encode('utf-8')
        the_bytes = base64.b64decode(data)
        dec = decrypt_data(the_bytes, self.key, self.iv)
        save_bin(self.DECB64_FILE, dec)

    def decrypt_b64_file_singleline(self):
        ''' decrypt base64 file with single line '''
        data = b''
        with open(self.ENCB641_FILE, "rb") as fobj:
            data = fobj.read()
        the_bytes = base64.b64decode(data)
        dec = decrypt_data(the_bytes, self.key, self.iv)
        save_bin(self.DECB641_FILE, dec)

    def action(self):
        ''' action '''
        if not os.path.isfile(self.KEYIV_FILE):
            self.save_keyiv()
        if not os.path.isfile('key.bin'):
            save_bin('key.bin', self.key)
        if not os.path.isfile('iv.bin'):
            save_bin('iv.bin', self.iv)
        md5plain = md5sum(self.INPUT_FILE)
        prt(f'plain: {md5plain}')
        prt("===== test encrypt =====")
        self.encrypt_file()
        md = md5sum(self.ENC_FILE)
        prt(f'{self.ENC_FILE}       enc: {md}')
        md = md5sum(self.ENCB64_FILE)
        prt(f'{self.ENCB64_FILE}   enc: {md}')
        md = md5sum(self.ENCB641_FILE)
        prt(f'{self.ENCB641_FILE}  enc: {md}')
        prt("===== test decrypt =====")
        self.decrypt_file()
        md5 = md5sum(self.DEC_FILE)
        prt(f'{self.DEC_FILE}      dec: {md5}')
        self.decrypt_b64_file_multipleline()
        md5 = md5sum(self.DECB64_FILE)
        prt(f'{self.DECB64_FILE}  dec: {md5}')
        self.decrypt_b64_file_singleline()
        md5 = md5sum(self.DECB641_FILE)
        prt(f'{self.DECB641_FILE} dec: {md5}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == "__main__":
    main()
