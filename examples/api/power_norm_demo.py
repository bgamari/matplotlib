#!/usr/bin/python

from scipy.stats import norm
from matplotlib import pyplot as pl
import matplotlib.colors as mcolors
import numpy as np
from numpy.random import multivariate_normal

samples = np.vstack([ multivariate_normal([10,10], [[3,5],[4,2]], size=100000),
                      multivariate_normal([30,20], [[2,3],[1,3]], size=1000)
                    ])

gammas = [0.8, 0.5, 0.3]
xgrid = np.floor((len(gammas)+1.)/2)
ygrid = np.ceil((len(gammas)+1.)/2)

pl.subplot(xgrid, ygrid, 1)
pl.title('Linear normalization')
pl.hist2d(samples[:,0], samples[:,1], bins=100)

for i,gamma in enumerate(gammas):
    pl.subplot(xgrid, ygrid, i+2)
    pl.title('Power law normalization\n$(\gamma=%1.1f)$' % gamma)
    pl.hist2d(samples[:,0], samples[:,1], bins=100, norm=mcolors.PowerNorm(gamma))

pl.subplots_adjust(hspace=0.39)
pl.show()
