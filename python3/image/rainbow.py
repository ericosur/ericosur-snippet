#!/usr/bin/env python3
# coding: utf-8

'''
create a PNG image of rainbow gradient
'''

from PIL import Image

def main():
    ''' main '''
    print('hello world')
    fn = 'test.png'
    width = 500
    height = 500
    size = width * height
    pixels = [255 * i / size for i in range(size)]

    img = Image.new('HSV', (width, height))
    img.putdata([(int(a), 255, 255) for a in pixels])
    img.convert(mode='RGB').save(fn)
    print('save to {}'.format(fn))
    img.show()

if __name__ == '__main__':
    main()
