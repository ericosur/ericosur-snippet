#!/usr/bin/python3
# coding: utf-8

''' euclidean distance '''

import numpy as np

def main():
    ''' main '''
    m = np.array([3, 4])

    d = np.linalg.norm(m)
    print(d)

if __name__ == '__main__':
    main()
