''' dft test
    https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html
'''

from scipy import fftpack
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#from myutil import get_python_version

# pylint: disable=unused-variable

def main():
    ''' main '''
    plt.style.use('dark_background')

    f = 10  # Frequency, in cycles per second, or Hertz
    f_s = 50  # Sampling rate, or number of measurements per second

    t = np.linspace(0, 2, 2 * f_s, endpoint=False)
    x = np.sin(f * 2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Signal amplitude')
    #plt.show()

    print("do FFT")
    X = fftpack.fft(x)
    freqs = fftpack.fftfreq(len(x)) * f_s

    # if float(get_python_version()) < 3.6:
    #     # explicitly assign TkAgg, default maybe Qt
    #     matplotlib.use('TkAgg')

    fig, ax = plt.subplots()
    ax.stem(freqs, np.abs(X), use_line_collection=True)
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    ax.set_xlim(-f_s / 2, f_s / 2)
    ax.set_ylim(-5, 110)
    plt.show()

if __name__ == '__main__':
    main()
