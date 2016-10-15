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

xs = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 100) #100 evenly spaced points between -2*pi and 2*pi

df_dx_small = g_bdm(xs, dx=1e-7)
df_dx_good = g_bdm(xs, dx=1e-5)
df_dx_large = g_bdm(xs, dx=1e-4)

df_dx_analytic = g(xs)

pyplot.figure(figsize=(8,4))
pyplot.plot(xs, df_dx_small - df_dx_analytic , label='dx small')
pyplot.plot(xs, df_dx_good - df_dx_analytic, label='dx good')
pyplot.plot(xs, df_dx_large - df_dx_analytic, label='dx large')
pyplot.xlabel("x increment"); pyplot.ylabel("Error")
pyplot.title("Graph showing"); pyplot.legend(loc='upper right')
pyplot.show()

ANSWER1 = """ """
