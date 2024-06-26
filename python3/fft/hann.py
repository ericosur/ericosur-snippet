# coding: utf-8

'''
hanning window
https://numpy.org/doc/stable/reference/generated/numpy.hanning.html
'''

import matplotlib.pyplot as plt

import numpy as np
from numpy.fft import fft, fftshift


def main():
    ''' main '''
    window = np.hanning(51)
    plt.style.use('dark_background')
    plt.plot(window)
    plt.title('Hann Window')
    plt.ylabel('Amplitude')
    plt.xlabel('Sample')

    plt.figure()
    A = fft(window, 2048) / 25.5
    mag = np.abs(fftshift(A))
    freq = np.linspace(-0.5, 0.5, len(A))
    with np.errstate(divide='ignore', invalid='ignore'):
        response = 20 * np.log10(mag)

    response = np.clip(response, -100, 100)
    plt.plot(freq, response)
    plt.title('Frequency response of the Hann Window')
    plt.ylabel('Magnitude [dB]')
    plt.xlabel('Normalized frequency [cycles per sample')
    plt.axis('tight')
    plt.show()

if __name__ == '__main__':
    main()
