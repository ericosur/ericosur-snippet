# coding: utf-8

''' dft test

qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though
it was found. This application failed to start because no Qt platform plugin
could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen,
vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx,
webgl, xcb.


for matplotlib.use(), valid strings are ['pdf', 'GTK3Cairo', 'nbAgg',
'WXCairo', 'Qt4Cairo', 'WX', 'pgf', 'WXAgg', 'GTK3Agg', 'cairo', 'template',
'Qt5Cairo', 'WebAgg', 'agg', 'Qt5Agg', 'TkAgg', 'Qt4Agg', 'MacOSX', 'svg',
'ps', 'TkCairo']

'''


import matplotlib.pyplot as plt

import numpy as np


# pylint: disable=unused-variable
def main():
    ''' main '''
    plt.style.use('dark_background')

    f = 10  # Frequency, in cycles per second, or Hertz
    f_s = 100  # Sampling rate, or number of measurements per second

    t = np.linspace(0, 2, 2 * f_s, endpoint=False)
    x = np.sin(f * 2 * np.pi * t)

    # if not require_python_version(3, 6):
    #     # explicitly assign TkAgg, default maybe Qt
    #     matplotlib.use('TkAgg')

    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Signal amplitude')
    plt.show()

if __name__ == '__main__':
    #print(plt.style.available)
    main()
