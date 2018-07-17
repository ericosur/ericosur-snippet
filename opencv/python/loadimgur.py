#!/usr/bin/env python
#
# using skimage (scikit-image)

import myutil
from skimage import io

def main():
    app_name = 'loadimgur.py'
    data = myutil.read_setting('setting.json')
    url = data[app_name]['lego']
    print('url:{}'.format(url))

    # use skimage.io.imread to read an image from URL, may wait a moment
    img = io.imread(url)
    io.imshow(img)
    io.show()


if __name__ == '__main__':
    main()
