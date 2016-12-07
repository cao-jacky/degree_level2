from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import time

time_start = time.clock()

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
valmin = -2.0
valmax = 2.0
steps = 300                 # Number of steps to take for the Newton Raphson m
max_iteration = 1000
convergence_steps = 15

def newton_raphson(z):
    for i in range(max_iteration):
        z = z - (z**4 - 1) / (4*z**3)
    return z

def nr_convergence(z):
    for i in range(convergence_steps):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            break
    return i

xvals = numpy.linspace(valmin,valmax,steps) # Generates values from min to max
xx, yy = numpy.meshgrid(xvals, xvals)
xx2, yy2 = numpy.meshgrid(xvals/2, xvals/2)
xx3, yy3 = numpy.meshgrid(xvals/10, xvals/10)
tmp = numpy.zeros(steps, dtype=int)
zs = numpy.outer(tmp, tmp)                      # A square array

# Plotting the first fractals graph, from valmin to valmax on x and y-axis
image = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])

# Plotting 'zoomed' in at half of valmin and valmax
image2 = numpy.reshape(newton_raphson(numpy.ravel(xx2+yy2*1j)),[steps,steps])

# Plotting 'zoomed' in at half of valmin and valmax
image3 = numpy.reshape(newton_raphson(numpy.ravel(xx3+yy3*1j)),[steps,steps])

# Plotting the convergence time graph, from valmin to valmax
for i in range(steps):
    for j in range(steps):
        z = xvals[i]+ xvals[j]*1j
        zs[i,j] = nr_convergence(z)

time_elapsed = (time.clock() - time_start)

print time_elapsed

# rename pic
pyplot.figure()
ax1 = pyplot.subplot(221)
ax1.set_title('x1 Zoom')
pyplot.imshow(numpy.angle(image), origin='lower')

ax2 = pyplot.subplot(222)
ax2.set_title('Convergence Time')
pyplot.imshow(zs, origin='lower')

ax3 = pyplot.subplot(223)
ax3.set_title('x2 Zoom')
pyplot.imshow(numpy.angle(image2), origin='lower')

ax4 = pyplot.subplot(224)
ax4.set_title('x10 Zoom')
pyplot.imshow(numpy.angle(image3), origin='lower')

pyplot.show()
