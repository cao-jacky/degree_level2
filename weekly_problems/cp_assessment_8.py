from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
valmin = -2.0               # The minimum value for x and y axis
valmax = 2.0                # The maximum value for x and y axis
steps = 302                 # Number of steps to take for Newton-Raphson
max_iteration = 1000        # Maximum number of iterations for root finder
convergence_steps = 15      # Maximum number of steps for convergence time fn

def newton_raphson(z):
    for i in range(max_iteration):
        z = z - (z**4 - 1) / (4*z**3)
    return z

def nr_convergence(z):
    for i in range(convergence_steps):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            break   # Breaks loops and returns i if convergence criteria is met
    return i

# Newton-Raphson root plotting
xvals = numpy.linspace(valmin,valmax,steps) # Generates values from min to max
xx, yy = numpy.meshgrid(xvals, xvals)       # Creates an array of coordinates
xx2, yy2 = numpy.meshgrid(xvals/2, xvals/2) # For second root plot
xx3, yy3 = numpy.meshgrid(xvals/10, xvals/10)   # For third root plot
# Newton-Raphson convergence time plotting
tmp = numpy.zeros(steps, dtype=int)             # Array to store vals
zs = numpy.outer(tmp, tmp)                      # A square array

# First fractals roots plot, from valmin to valmax on x and y-axis
image = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])
# Roots plot zoomed in at half of valmin and valmax
image2 = numpy.reshape(newton_raphson(numpy.ravel(xx2+yy2*1j)),[steps,steps])
# Roots plot zoomed in at tenth of valmin and valmax
image3 = numpy.reshape(newton_raphson(numpy.ravel(xx3+yy3*1j)),[steps,steps])

# Plotting the convergence time graph, from valmin to valmax
for i in range(steps):
    for j in range(steps):
        z = xvals[i]+ xvals[j]*1j
        zs[i,j] = nr_convergence(z)

pyplot.figure()
pyplot.suptitle('The chaotic nature of the Newton-Raphson method')
ax1 = pyplot.subplot(221)
ax1.set_title('Root x1 Zoom', fontsize=10); pyplot.tick_params(labelsize=9)
pyplot.imshow(numpy.angle(image), origin='lower', extent=[-2,2,-2,2])

ax2 = pyplot.subplot(222)
ax2.set_title('Convergence Time', fontsize=10); pyplot.tick_params(labelsize=9)
pyplot.imshow(zs, origin='lower', extent=[-2,2,-2,2])

ax3 = pyplot.subplot(223)
ax3.set_title('Root x2 Zoom', fontsize=10); pyplot.tick_params(labelsize=9)
pyplot.imshow(numpy.angle(image2), origin='lower', extent=[-2,2,-2,2])

ax4 = pyplot.subplot(224)
ax4.set_title('Root x10 Zoom', fontsize=10); pyplot.tick_params(labelsize=9)
pyplot.imshow(numpy.angle(image3), origin='lower', extent=[-2,2,-2,2])
pyplot.show()

ANSWER1 = """  """
