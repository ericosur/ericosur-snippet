''' getting started '''

from skimage import data, io, filters

def main():
    ''' main '''
    image = data.coins()
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()

if __name__ == '__main__':
    main()
