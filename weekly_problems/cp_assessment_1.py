from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    '''Function which returns a value, or an array of values '''
    return numpy.cos(x)

def g(x):
    '''adasd'''
    return -(numpy.sin(x))

def g_bdm(x, dx):
    '''docstring'''
    return (f(x) - f(x - dx)) / dx

#Creating 100 evenly spaced points between -2*pi and 2*pi
xs = numpy.linspace(-numpy.pi, numpy.pi, 100)

pyplot.figure(figsize=(8,4))
df_dx_small = pyplot.plot(xs, g_bdm(xs, dx=1e-7) - g(xs), label='dx small')
df_dx_good = pyplot.plot(xs, g_bdm(xs, dx=1e-10) - g(xs), label='dx good')
df_dx_large = pyplot.plot(xs, g_bdm(xs, dx=1e-20) - g(xs), label='dx large')
pyplot.title("askjdns"); pyplot.legend(loc='upper left')
pyplot.show()

ANSWER1 =

#Testing the code
if __name__ == '__main__':

    import numpy
    import cp_assessment_1

    #cp_assessment_1.f(numpy.array([1,2,3,4,5]))
    cp_assessment_1.g_bdm(numpy.array([1,2,3,4,5]), numpy.array([0.1,0.1,0.1,0.1,0.1]))
