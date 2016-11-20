from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
xl, xu = -0.2, 1.2  # x-bounds
yl, yu = -0.2, 1.2  # y-bounds
x0, y0 = 0.2, 1.0   # Initial position
n_panels = 1000

## zkjdnasnd
# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS

# Generate x and y values
x_axis = numpy.arange(xl, xu, dy)
y_axis = numpy.arange(yl, yu, dx)

def f((x, y)):
    """ Function at vec(r) """
    return (1-x)**2 + 100*(y-x**2)**2

def grad((x, y)):
    """ Vector differential of f(vec(r)) """
    df_dx = 400*x**3 - 400*x*y + 2*x - 2
    df_dy = 200*(y - x**2)
    return numpy.array((df_dx, df_dy))

def gradient_descent((x,y)):
    r0 = numpy.array((x0,y0))
    gamma = 0.05                 # Gamma parameter, step size
    r = numpy.array((x,y))

    r_history = numpy.zeros((n_panels, 3), dtype=numpy.float32)

    for i in range(n_panels):
        r = r0
        r_history[i] = r # Record current values
		# Calculate next time step
        r = r - gamma * grad(r) # Euler time step involving f(n)
	#print r_history

#pyplot.figure()
#pyplot.show()

r_history = numpy.zeros((n_panels, 3), dtype=numpy.float32)
r_history[0][0] = 1
r_history[0][1] = 2
print r_history[0]

ANSWER1 = """ """
ANSWER2 = """ """
