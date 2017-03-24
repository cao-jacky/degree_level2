# Standard libraries being imported
from __future__ import division
from PIL import Image # Importing Python Image Library
from operator import add
from scipy.special import j1
from scipy.integrate import quad
from scipy.special import jv

import numpy

""" This module returns the intensity for each function/Fourier Transform """

# Intensity Functions
def five_slit(x):
    """ Function which outputs the Fourier transform squared for the five slit
    diffraction grating scenario """

    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    k = (numpy.pi) / (lmda)
    d = 0.016 * 10 ** (-2)

    t1 = 2 * (numpy.cos((2*k*d*(x+30))/5))
    t2 = 2 * (numpy.cos((k*d*(x+30))/5))

    return 50 * (t1 + t2 + 1)**2 + 10

def five_slit_2(x):
    """ Second attempt by myself """

    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    a = 0.016 * 10 ** (-2)
    d = 0.016 * 10 ** (-2)
    z = 49 * 10 ** (-2)

    t1 = numpy.sin((numpy.pi*x*a)/(lmda))/(numpy.pi*x*a)/(lmda)
    t2 = numpy.sin((5*numpy.pi*x*d)/(lmda))/numpy.sin((numpy.pi*x*a)/(lmda))

    return (a * t1 * t2) ** 2

def five_slit_3(x):
    """ Function which outputs the Fourier transform squared for the five slit
    diffraction grating scenario """

    lmda = 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    k = numpy.pi / lmda
    d = 0.016 * 10 ** (-2)
    f = 48 * 10 ** (-2)

    t1 = 2 * (numpy.cos((numpy.pi*x*d)/(lmda*f)))
    t2 = 2 * (numpy.cos((3*numpy.pi*x*d)/(lmda*f)))

    return (t1 + t2 + 1)**2

def jinc(x):
    """ Deprecated function, new attempt in jinc.m file within this directory """
    return (j1(x) / x) ** 2

#jinc = numpy.vectorize(jinc)

def sinc(x):
    """ For singular slit, sinc pattern in Fourier plane """
    lmda = 19.8 * 700 * 10 ** (-9) # Wavelength of laser light, 700nm
    d = 0.068 * 10 ** (-2)
    f = 19.8 * 0.48
    #return 80*(numpy.sin((x*numpy.pi*d)/(lmda*f))/(numpy.pi*x*d)) ** 2
    return 35000*(numpy.sin((1/47)*(x-690))/((1/47)*(x-690)))**2
