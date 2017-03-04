# Standard libraries being imported
from __future__ import division
from PIL import Image # Importing Python Image Library
from operator import add
from scipy.special import j1
from scipy.integrate import quad

import numpy

# Intensity Functions
def five_slit(x):
    """ Function which outputs the Fourier transform squared for the five slit
    diffraction grating scenario """

    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    k = (2 * numpy.pi) / lmda
    d = 0.016 * 10 ** (-2)

    t1 = 2 * numpy.cos((2*k*d*x)/5)
    t2 = 2 * numpy.cos((k*d*x)/5)

    return (t1 + t2 + 1)
