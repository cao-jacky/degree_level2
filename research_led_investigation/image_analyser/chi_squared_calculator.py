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

def sinc(x,data,uncert):
    sinc = (1/20) * fourier_transforms.sinc(x)
    sinc_cs = ((data-sinc)/uncert) ** 2 # Calculating the bit before summation
    sinc_cs = numpy.delete(sinc_cs,numpy.s_[539:849]) # Removes the central saturated peak
    numpy.savetxt('saved_data/sinc_cs.txt', sinc_cs, delimiter='-')
    print numpy.size(x)
    return "reduced chi-squared value for sinc: ", numpy.sum(sinc_cs) / (numpy.size(x)-(849-539))

def five_slit(x,data,uncert):
    five = fourier_transforms.five_slit(x)
    five_cs = ((data-five)/uncert) ** 2 # Calculating the bit before summation
    #five_cs = numpy.delete(five_cs,numpy.s_[539:849]) # Removes the central saturated peak
    numpy.savetxt('saved_data/five_cs.txt', five_cs, delimiter='-')
    print numpy.size(x)
    return "reduced chi-squared value for five slits: ", numpy.sum(five_cs) / (numpy.size(x))

def jinc(x,data,uncert):
    jinc = numpy.loadtxt('saved_data/jinc.txt')
    jinc = numpy.delete(jinc,numpy.s_[157:200])
    jinc_cs = ((data-jinc)/uncert) ** 2 # Calculating the bit before summation
    #jinc_cs = numpy.delete(five_cs,numpy.s_[539:849]) # Removes the central saturated peak
    numpy.savetxt('saved_data/jinc_cs.txt', jinc_cs, delimiter='-')
    print numpy.size(x)
    return "reduced chi-squared value for jinc: ", numpy.sum(jinc_cs) / (numpy.size(x))
