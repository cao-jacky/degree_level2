# Standard libraries being imported
from __future__ import division
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image # Importing Python Image Library
from operator import add

import numpy
import scipy.ndimage
import matplotlib.pyplot as pyplot
import matplotlib.colors

import grapher_data         # Module output the raw data for graphing
import fourier_transforms   # Module which has the Fourier transform/intensity functions
import maxima_locator       # Module to locate maximas

def sinc(x):
    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    d = 0.068 * 10 ** (-2)
    f = 0.48
    return (numpy.sin((x*numpy.pi*d)/(lmda*f))/(numpy.pi*x*d)) ** 2

def sinc_2(x):
    return (numpy.sin((1/100)*x)/((1/100)*x))**2

pyplot.figure()
x = numpy.linspace(-1280,1280,500)
sinc = sinc_2(x)
pyplot.plot(x, sinc, '-g', label='Theoretical Model')
pyplot.show()
