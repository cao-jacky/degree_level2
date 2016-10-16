from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    '''Function as outlined in assessment 1'''
    return numpy.cos(x)

def g(x):
    '''Analytical derivative of f(x) with respect to x'''
    return -(numpy.sin(x))

def g_bdm(x, dx):
    '''Function as outlined in assessment 3'''
    return (f(x) - f(x - dx)) / dx

# Creating 100 evenly spaced points between -2*pi and 2*pi
xs = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 100)

# Evaluating the derivatives
df_dx_small = g_bdm(xs, dx=1e-10)
df_dx_good = g_bdm(xs, dx=1e-5)
df_dx_large = g_bdm(xs, dx=1e-4)
# Analytical
df_dx_analytic = g(xs)

# Plotting the three graphs, labelling the axes, adding a legend, and a title
pyplot.figure(figsize=(8,4))
pyplot.plot(xs, df_dx_small - df_dx_analytic , label='dx small')
pyplot.plot(xs, df_dx_good - df_dx_analytic, label='dx good')
pyplot.plot(xs, df_dx_large - df_dx_analytic, label='dx large')
pyplot.xlabel("x"); pyplot.ylabel("Error in the derivative of f(x)"); pyplot.legend(loc='upper right')
pyplot.title("Error between backwards difference derivative and analytic derivative of the function cos(x)", fontsize=11)
pyplot.show()

ANSWER1 = """As dx becomes smaller, plot becomes more jagged, the difference between error values varies considerably leading to a less accurate approximation of the derivative. With dx increasing, the error increases considerably so a greater variation between the bdm value and the analytic value for the derivative, so less accurate."""
