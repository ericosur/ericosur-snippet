'''
    dft test
    https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html

    perform fft on wave, and draw spectrum
'''

import os
import sys
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from skimage import util
#from scipy import fftpack

# pylint: disable=unused-variable
def main(fn):
    ''' main '''
    if not os.path.exists(fn):
        print('file not found:', fn)
        sys.exit(1)

    plt.style.use('dark_background')
    rate, audio = wavfile.read(fn)
    audio = np.mean(audio, axis=1)

    N = audio.shape[0]
    L = N / rate

    print('Audio length: {:.2f} seconds'.format(L))
    # need python 3.6+ to use such format string
    #print(f'Audio length: {L:.2f} seconds')
    #print('np.max(audio): {}'.format(np.max(audio)))

    f, ax = plt.subplots(figsize=(8, 4))
    ax.plot(np.arange(N) / rate, audio)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Amplitude [unknown]')
    ax.grid()


    #print('audio shape:', audio.shape)
    M = 1024
    slices = util.view_as_windows(audio, window_shape=(M,), step=100)
    print('Audio shape: {}, Sliced audio shape: {}'.format(audio.shape, slices.shape))

    win = np.hanning(M + 1)[:-1]
    #print('win:', win)
    slices = slices * win
    slices = slices.T
    print('Shape of `slices`', slices.shape)
    #print('np.max(slices): {}'.format(np.max(slices)))


    spectrum = np.fft.fft(slices, axis=0)[:M // 2 + 1:-1]
    spectrum = np.abs(spectrum)

    f, ax = plt.subplots(figsize=(8, 4))
    S = np.abs(spectrum)
    print('np.max: {}'.format(np.max(S)))
    with np.errstate(divide='ignore', invalid='ignore'):
        S = 20 * np.log10(S / np.max(S))
    ax.imshow(S, origin='lower', cmap='viridis',
              extent=(0, L, 0, rate / 2 / 1000))
    ax.axis('tight')
    ax.set_ylabel('Frequency [kHz]')
    ax.set_xlabel('Time [s]')

    plt.show()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('nightingale.wav')
