#!/usr/bin/env python

'''
my first script for skimage (scikit-image)
'''

import os
from skimage import io, data_dir

def main():
    ''' main '''
    fn = os.path.join(data_dir, 'moon.png')
    print('skimage.data_dir: {}'.format(fn))
    if not os.path.isfile(fn):
        print('file not found, exit')
        return
    moon = io.imread(fn)
    io.imshow(moon)
    io.show()


if __name__ == '__main__':
    main()
