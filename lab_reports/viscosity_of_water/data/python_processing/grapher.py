from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

# Generate points for the lines of best fit
def f_blue(x):
    return (0.0242 * x) - 0.0119

def f_red(x):
    return (0.0118 * x) - 0.0096

def f_black(x):
    return (0.0087 * x) + 0.0002


xs = numpy.linspace(2, 16, 100)

# Raw Data
## Blue Tube
blue_heights = numpy.array((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16))
blue_v_prime = numpy.array((0.042222222, 0.077777778, 0.085555556, 0.102222222, 0.114444444, 0.171111111, 0.186666667, 0.196666667, 0.197777778, 0.235555556, 0.287777778, 0.35, 0.41))
blue_error = numpy.array((0.005555605, 0.006477024, 0.006574496, 0.006786023, 0.00694329, 0.007692762, 0.00790352, 0.008039993, 0.008055202, 0.008577295, 0.00931279, 0.010205603, 0.011079665))

## Red Tube
red_heights = numpy.array((2, 4, 6, 8, 10, 12, 14, 16))
red_v_prime = numpy.array((0.021111111, 0.045, 0.045555556, 0.091111111, 0.1, 0.121111111, 0.156111111, 0.2))
red_error = numpy.array((0.005794821, 0.006075936, 0.006082593, 0.006644613, 0.006757619, 0.007029789, 0.007491427, 0.008085647))

## Black Tube
black_heights = numpy.array((2, 4, 6, 8, 10, 12, 14, 16))
black_v_prime = numpy.array((0.018888889, 0.028888889, 0.06, 0.075555556, 0.087777778, 0.098888889, 0.111666667, 0.148888889))
black_error = numpy.array((0.000793378, 0.000932859, 0.001390458, 0.001625793, 0.001812261, 0.001982614, 0.002179256, 0.002755027))

# Grapher
pyplot.figure()

# Calling line of best fit functions
blue_line = f_blue(xs)
red_line = f_red(xs)
black_line = f_black(xs)

# Plot blue data and errors
pyplot.errorbar(blue_heights, blue_v_prime, yerr=blue_error, linestyle='None', marker='o', markeredgecolor='blue', markersize='5', color='blue', label='Blue Tube')
pyplot.plot(xs, blue_line, color='blue')

# Plot red data and errors
pyplot.errorbar(red_heights, red_v_prime, yerr=red_error, linestyle='None', marker='o', markeredgecolor='red', markersize='5', color='red', label='Red Tube')
pyplot.plot(xs, red_line, color='red')

# Plot black data and errors
pyplot.errorbar(black_heights, black_v_prime, yerr=black_error, linestyle='None', markeredgecolor='black', markersize='5', marker='o', color='black', label='Black Tube')
pyplot.plot(xs, black_line, color='black')

pyplot.xlabel('$Heights (cm)$')
pyplot.ylabel('${dV}/{dt}$ ($cm^3 s^{-1} $)')
pyplot.legend(loc=0, numpoints=1)

# Plotting residuals
#pyplot.add_axes((.1,.1,.8,.2))

# Blue normalised residuals
#pyplot.plot(blue_heights, difference,'or')

pyplot.show()
