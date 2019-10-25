# -*- coding: utf-8 -*-

"""
from http://matplotlib.sourceforge.net/examples/animation/animate_decay_tk_blit.html
"""

from __future__ import print_function
import time
import matplotlib.pyplot as plt
import numpy as np


def data_gen():
    ''' generate data points '''
    t = data_gen.t
    data_gen.t += 0.05
    return np.sin(2*np.pi*t) * np.exp(-t/10.)


def run():
    ''' run by args '''
    background = FIG.canvas.copy_from_bbox(AX.bbox)
    # for profiling
    tstart = time.time()

    while 1:
        # restore the clean slate background
        FIG.canvas.restore_region(background)
        # update the data
        t = data_gen.t
        y = data_gen()
        XDATA.append(t)
        YDATA.append(y)
        xmin, xmax = AX.get_xlim()
        if t >= xmax:
            AX.set_xlim(xmin, 2*xmax)
            FIG.canvas.draw()
            background = FIG.canvas.copy_from_bbox(AX.bbox)

        LINE.set_data(XDATA, YDATA)

        # just draw the animated artist
        AX.draw_artist(LINE)
        # just redraw the axes rectangle
        FIG.canvas.blit(AX.bbox)

        if run.cnt == 1000:
            # print the timing info and quit
            print('{:.2f} fps'.format(1000.0/(time.time()-tstart)))
            return

        run.cnt += 1

if __name__ == '__main__':
    data_gen.t = 0

    FIG = plt.figure()
    AX = FIG.add_subplot(111)
    LINE, = AX.plot([], [], animated=True, lw=2)
    AX.set_ylim(-1.1, 1.1)
    AX.set_xlim(0, 5)
    AX.grid()
    XDATA, YDATA = [], []

    run.cnt = 0

    MANAGER = plt.get_current_fig_manager()
    MANAGER.window.after(100, run)

    plt.show()
