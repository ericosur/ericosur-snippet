#!/usr/bin/env python3
# coding: utf-8

'''
input text from CLI and generate qrcode image
'''

import random
import sys

'''
Use Shift JIS COULD NOT avoid the zbralight decoding error.
There are many han characters that are common or litter difference between
Chinese and Japanese. I think it could not be solved by encoding simply.

Maybe I should use table to replace these character to another?

It does not the fault within encoding side.
'''
APPLY_EXTRA_ENCODING = True

try:
    import qrcode
except ImportError:
    print('need install module **qrcode**')
    sys.exit()

def get_random_filename():
    ''' random hex '''
    i = random.randint(0, 0xffffffff)
    return f'{i:08x}.png'

def apply_shiftjis(s: str):
    ''' apply shift-jis encoding '''
    data = s
    try:
        data = s.encode('SHIFT_JIS')
        return data
    except UnicodeEncodeError as e:
        print('UnicodeEncodeError at:', s, ' ', e)
        #data = s.encode('UTF-8')
        return None

def make_qrimg(s):
    ''' make qrcode image '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # here I pre-decode str as SHIFT JIS encoding, if failed, try UTF-8 next
    # for some qr decoder it default works at SHIFT-JIS
    if APPLY_EXTRA_ENCODING:
        data = apply_shiftjis(s)
    if not data:
        data = s

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    #img.show()
    fn = get_random_filename()
    print('saved:', fn)
    img.save(fn)


def main(argv):
    ''' main '''
    if argv == []:
        argv.append('https://www.google.com/')

    for a in argv:
        print(a)
        make_qrimg(a)

if __name__ == '__main__':
    main(sys.argv[1:])
