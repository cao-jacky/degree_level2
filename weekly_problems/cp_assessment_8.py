from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import time

time_start = time.clock()

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
valmin = 2.0
valmax = 2.0
steps = 300

def newton_raphson(z):
    for i in range(1000):
        z = z - (z**4 - 1) / (4*z**3)
    return z

def nr_plot(z):
    for i in range(500):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        #if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            #break
    return numpy.angle(z)

def nr_convergence(z):
    for i in range(15):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            break
    return i

x_values = numpy.linspace(-valmin,valmax,steps)
y_values = numpy.linspace(-valmin,valmax,steps)
xx, yy = numpy.meshgrid(x_values, y_values)

# Converts the values returned from Newton Raphson into an image of step x step
# resolution
pic = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])

xs = numpy.linspace(-valmin, valmax, steps)
tmp = numpy.zeros(steps, dtype=int)
zs = numpy.outer(tmp, tmp)  # A square array
zsplot = numpy.outer(tmp, tmp)  # A square array

for i in range(steps):
    for j in range(steps):
        z = xs[i]+ xs[j]*1j
        zs[i,j] = nr_convergence(z)
        zsplot[i,j] = nr_plot(z)

time_elapsed = (time.clock() - time_start)

print time_elapsed

# rename pic
pyplot.figure()
pyplot.subplot(221)
im = pyplot.imshow(numpy.angle(pic), origin='lower')
#pyplot.colorbar(im, orientation='vertical')

pyplot.subplot(222)
pyplot.imshow(zs, origin='lower')

pyplot.subplot(223)
pyplot.imshow(zsplot, origin='lower')

pyplot.show()
