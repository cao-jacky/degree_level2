from __future__ import division
import numpy
import matplotlib
import matplotlib.pyplot as pyplot

# Optionally set font to Computer Modern to avoid common missing font errors
matplotlib.rc('font', family='serif', serif='cm10')

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']

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
blue_error = numpy.array((0.005560451, 0.005572149, 0.005575628, 0.005584188, 0.005591421, 0.005635416, 0.005650468, 0.005660813, 0.005661994, 0.00570595, 0.005778588, 0.005882465, 0.005999608))
#blue_n_resid = numpy.array((1.01877615, 3.046240999, 0.090678174, -1.266799348, -3.415611863, 2.364021224, 0.819666274, -1.698484312, -5.784179379, -3.36815283, 1.515492796, 3.822722148, 5.666108442))
blue_n_resid = numpy.array((1.806245733, 3.671820494, 0.555730547, -0.962351229, -3.271242107, 2.348826005, 0.646495703, -2.02906551, -6.272385757, -4.009077638, 0.728112141, 2.745677902, 4.312452971))

## Red Tube
red_heights = numpy.array((2, 4, 6, 8, 10, 12, 14, 16))
red_v_prime = numpy.array((0.021111111, 0.045, 0.045555556, 0.091111111, 0.1, 0.121111111, 0.156111111, 0.2))
red_error = numpy.array((0.0055567, 0.005561116, 0.005561254, 0.005578314, 0.00558296, 0.005595706, 0.005622107, 0.005664377))
red_n_resid = numpy.array((1.260929807, 1.300062916, -2.855550597, 1.077263889, -1.57042023, -2.023387231, 0.00212071, 3.572328553))

## Black Tube
black_heights = numpy.array((2, 4, 6, 8, 10, 12, 14, 16))
black_v_prime = numpy.array((0.018888889, 0.028888889, 0.06, 0.075555556, 0.087777778, 0.098888889, 0.111666667, 0.148888889))
black_error = numpy.array((0.000565272, 0.000578028, 0.000646938, 0.000694905, 0.000737447, 0.00077919, 0.000830217, 0.000992621))
black_n_resid = numpy.array((-0.245697937, 1.069541768, -1.411781623, -1.095480207, -0.182151226, 0.928401832, 1.737921554, -1.815873529))

# Grapher
fig = pyplot.figure(1)

# Calling line of best fit functions
blue_line = f_blue(xs)
red_line = f_red(xs)
black_line = f_black(xs)

# Plot blue data and errors
frame1=fig.add_axes((.1,.3,.8,.6))
pyplot.xlim(2, 16)
pyplot.errorbar(blue_heights, blue_v_prime, yerr=blue_error, linestyle='None', marker='o', markeredgecolor='blue', markersize='5', color='blue')
pyplot.plot(xs, blue_line, color='blue')

# Plot red data and errors
pyplot.errorbar(red_heights, red_v_prime, yerr=red_error, linestyle='None', marker='s', markeredgecolor='red', markersize='5', color='red')
pyplot.plot(xs, red_line, color='red')

# Plot black data and errors
pyplot.errorbar(black_heights, black_v_prime, yerr=black_error, linestyle='None', marker='^', markeredgecolor='black', markersize='5', color='black')
pyplot.plot(xs, black_line, color='black')

frame1.axes.get_xaxis().set_visible(False)
pyplot.ylabel('${dV}/{dt}$ ($cm^3 s^{-1} $)')

# Legend stuff
pyplot.plot(0, 0, marker='o', markeredgecolor='blue', markersize='5', color='blue', label='Blue Tube')
pyplot.plot(0, 0, marker='s', markeredgecolor='red', markersize='5', color='red', label='Red Tube')
pyplot.plot(0, 0, marker='^', markeredgecolor='black', markersize='5', color='black', label='Black Tube')
pyplot.legend(loc=0, numpoints=1)

# Plotting residuals
frame2 = fig.add_axes((.1,.1,.8,.2))
pyplot.xlim(2, 16)

pyplot.scatter(blue_heights, blue_n_resid, color='blue', alpha=0.7, marker='o')        # Blue normalised residuals
pyplot.scatter(red_heights, red_n_resid, color='red', alpha=0.7, marker='s')           # Red normalised residuals
pyplot.scatter(black_heights, black_n_resid, color='black', alpha=0.7, marker='^')     # Black normalised residuals

pyplot.axhline(y=0, color='black', alpha=0.5)
pyplot.axhline(y=2, color='black', alpha=0.5, linestyle='--', linewidth='0.5')
pyplot.axhline(y=-2, color='black', alpha=0.5, linestyle='--', linewidth='0.5')

y_ticks = numpy.array((6, 4, 2, 0, -2, -4, -6, -8))
custom_y_ticks = ['','$4$','$2$','$0$','$-2$','$-4$','$-6$','$-8$']
pyplot.yticks(y_ticks, custom_y_ticks)
#pyplot.tick_params(axis='y', pad=1)

pyplot.xlabel(r'\textbf{Heights} $(cm)$')
pyplot.ylabel(r'\textbf{Residuals}')

pyplot.savefig('fig1-2.pdf')
pyplot.show()
