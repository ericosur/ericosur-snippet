# coding: utf-8

'''
hanning window
https://numpy.org/doc/stable/reference/generated/numpy.hanning.html
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftshift
from myutil import get_python_version

if float(get_python_version()) < 3.6:
    # explicitly assign TkAgg, default maybe Qt
    matplotlib.use('TkAgg')

window = np.hanning(51)
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
