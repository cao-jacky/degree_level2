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

    t1 = 2 * (numpy.cos((2*k*d*x)/5))
    t2 = 2 * (numpy.cos((k*d*x)/5))

    return (t1 + t2 + 1)

def five_slit_2(x):
    """ Second attempt by myself """

    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    a = 0.016 * 10 ** (-2)
    d = 0.016 * 10 ** (-2)
    z = 49 * 10 ** (-2)

    t1 = numpy.sin((numpy.pi*x*a)/(lmda))/(numpy.pi*x*a)/(lmda)
    t2 = numpy.sin((5*numpy.pi*x*d)/(lmda))/numpy.sin((numpy.pi*x*a)/(lmda))

    return (a * t1 * t2) ** 2
