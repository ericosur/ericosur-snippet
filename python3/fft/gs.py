''' getting started '''

import sys
from myutil import need_python36

try:
    need_python36()
    from skimage import data, io, filters
except RuntimeError:
    print("[ERROR] you need python 3.6+ to run this sample")
    sys.exit(1)

def main():
    ''' main '''
    image = data.coins()
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()

if __name__ == '__main__':
    main()
