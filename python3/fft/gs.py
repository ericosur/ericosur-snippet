''' getting started '''

# pylint: disable=import-error

from skimage import data, filters, io


def main():
    ''' main '''
    image = data.coins()
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()

if __name__ == '__main__':
    main()
