from __future__ import division
import numpy
import matplotlib
import matplotlib.pyplot as pyplot

# Normalised residuals
blue_n_resid = numpy.array((1.806245733, 3.671820494, 0.555730547, -0.962351229, -3.271242107, 2.348826005, 0.646495703, -2.02906551, -6.272385757, -4.009077638, 0.728112141, 2.745677902, 4.312452971))
red_n_resid = numpy.array((1.260929807, 1.300062916, -2.855550597, 1.077263889, -1.57042023, -2.023387231, 0.00212071, 3.572328553))
black_n_resid = numpy.array((-0.245697937, 1.069541768, -1.411781623, -1.095480207, -0.182151226, 0.928401832, 1.737921554, -1.815873529))

# Lagged residuals
blue_l_resid = blue_n_resid - 1
red_l_resid = red_n_resid - 1
black_l_resid = black_n_resid - 1

# Durbin-Watson statistic
## Blue tube
d_blue_hist = numpy.zeros((13, 1))
for i in range(13):
    d_blue_hist[i] = (blue_n_resid[i] - blue_l_resid[i-1])**2
d_blue = numpy.sum(d_blue_hist)/numpy.sum(blue_n_resid**2)
## Red tube
d_red_hist = numpy.zeros((8, 1))
for i in range(8):
    d_red_hist[i] = (red_n_resid[i] - red_l_resid[i-1])**2
d_red = numpy.sum(d_red_hist)/numpy.sum(red_n_resid**2)
## Black tube
d_black_hist = numpy.zeros((8, 1))
for i in range(8):
    d_black_hist[i] = (black_n_resid[i] - black_l_resid[i-1])**2
d_black = numpy.sum(d_black_hist)/numpy.sum(black_n_resid**2)

pyplot.figure()
pyplot.scatter(blue_l_resid, blue_n_resid, color='blue', alpha=0.7, marker='o', label=d_blue)
pyplot.scatter(red_l_resid, red_n_resid, color='red', alpha=0.7, marker='s', label=d_red)
pyplot.scatter(black_l_resid, black_n_resid, color='black', alpha=0.7, marker='^', label=d_black)

pyplot.plot((-2,2),(2,2))
pyplot.plot((-2,2),(-2,-2))
pyplot.plot((2,2),(-2,2))
pyplot.plot((-2,-2),(-2,2))

pyplot.xlabel('Normalised Residuals-1')
pyplot.ylabel('Normalised Residuals')
pyplot.legend(loc='lower right', title='Durbin-Watson Statistic')
pyplot.savefig('durbin-watson.pdf', bbox_inches='tight')
pyplot.show()
