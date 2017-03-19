from __future__ import division
from PIL import Image # Importing Python Image Library
from operator import add
from scipy.special import j1
from scipy.integrate import quad
from scipy.special import jv

import numpy
import fourier_transforms

""" Calculates the chi-squared between the model and theory """

#x = numpy.linspace(0,size[0],200) # Is the 'data' variable in the functions

def five_slit(data,uncert):
    five_slit_data = fourier_transforms.five_slit(data)

def sinc(x,data,uncert):
    sinc = (1/20) * fourier_transforms.sinc(x)
    sinc_cs = ((data-sinc)/uncert) ** 2 # Calculating the bit before summation
    sinc_cs = numpy.delete(sinc_cs,numpy.s_[539:849]) # Removes the central saturated peak
    numpy.savetxt('saved_data/sinc_cs.txt', sinc_cs, delimiter='-')
    return "reduced chi-squard value: ", numpy.sum(sinc_cs) / (numpy.size(x)-(849-539))
