from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    '''docstring here'''

    print numpy.cos(x)
    return numpy.cos(x)

def g_bdm(x, dx):
    '''docstring'''

    f_deriv = (f(x) - f(x - dx)) / dx

    print f_deriv

#Creating 100 evenly spaced points between -2*pi and 2*pi
xs = numpy.linspace(-numpy.pi, numpy.pi, 100)

#Testing the code
if __name__ == '__main__':

    import numpy
    import cp_assessment_1

    #cp_assessment_1.f(numpy.array([1,2,3,4,5]))
    cp_assessment_1.g_bdm(numpy.array([1,2,3,4,5]), numpy.array([0.1,0.1,0.1,0.1,0.1]))
