#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
refer to: https://blog.csdn.net/dcrmg/article/details/79155233
'''

import cv2
import numpy as np

def main():
    ''' main '''
    fn = 'lena.png'
    img = cv2.imread(fn)
    if img is None:
        print('cannot load image: {}'.format(fn))
        return

    # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
    img_encode = cv2.imencode('.jpg', img)[1]
    # imgg = cv2.imencode('.png', img)

    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()

    # actually, str_encode is exactly the JPEG bytearray
    # so name it as "foo.jpg" works fine

    # 缓存数据保存到本地，以txt格式保存
    ofn = 'img_encode.bin'
    with open(ofn, 'wb') as f:
        f.write(str_encode)
        f.flush()

    # read it back and show
    with open(ofn, 'rb') as f:
        str_encode = f.read()

    nparr = np.fromstring(str_encode, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("img_decode", img_decode)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
