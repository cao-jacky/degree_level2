from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
xl, xu = -0.2, 1.2  # x-bounds
yl, yu = -0.2, 1.2  # y-bounds
x0, y0 = 0.2, 1.0   # Initial position
r0 = numpy.array((x0,y0))
n_panels = 10000

# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS

y_axis = numpy.arange(yl, yu, dx)
x_axis = numpy.arange(xl, xu, dy)

dat = numpy.zeros((len(y_axis), len(x_axis)))

def f((x, y)):
    """ Function at vec(r) """
    return (1-x)**2 + 100*(y-x**2)**2

for iy, y in enumerate(y_axis):
    for ix, x in enumerate(x_axis):
        dat[iy, ix] = f((x, y))

def grad((x, y)):
    """ Vector differential of f(vec(r)) """
    df_dx = 400*x**3 - 400*x*y + 2*x - 2
    df_dy = 200*(y - x**2)
    return numpy.array((df_dx, df_dy))

def gradient_descent((x,y)):
    gamma = 0.001              # Gamma parameter, step size
    r = r0

    r_history = numpy.zeros((n_panels, 3), dtype=numpy.float32)

    for i in range(n_panels):
        r_history[i,:2] = r # Record current values
		# Calculate next time step
        r = r - gamma * grad(r) # Euler time step involving f(n)

    print r_history
    return r_history

data = gradient_descent(r0)

pyplot.figure()
im = pyplot.imshow(dat, extent=(xl, xu, yl, yu), origin='lower', cmap=matplotlib.cm.gray, norm=matplotlib.colors.LogNorm(vmin=0.2, vmax=200))
pyplot.plot(data[:,0], data[:,1], '-o')
pyplot.colorbar(im, orientation='vertical')
pyplot.show()

ANSWER1 = """ """
ANSWER2 = """ """
