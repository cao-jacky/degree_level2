from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining data to use
xl, xu = -0.2, 1.2          # x-bounds
yl, yu = -0.2, 1.2          # y-bounds
x0, y0 = 0.5, 0.5           # Initial position
r0 = numpy.array((x0,y0))   # Vector form of the initial position
n_panels = 5000             # Number of panels used, also max iteration value
convergence_criteria = 1e-11

# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS

y_axis = numpy.arange(yl, yu, dy) # Generating points between lower and upper y
x_axis = numpy.arange(xl, xu, dx) # Generating points between lower and upper x

points = numpy.zeros((len(y_axis), len(x_axis)))
gammas = [0.001, 0.0008, 0.000003, 0.00000007, 0.002]

def f((x, y)):
    """ Function at vec(r) """
    return (1-x)**2 + 100*(y-x**2)**2

def grad((x, y)):
    """ Vector differential of f(vec(r)) """
    df_dx = 400*x**3 - 400*x*y + 2*x - 2
    df_dy = 200*(y - x**2)
    return numpy.array((df_dx, df_dy)) # Returning grad

def gradient_descent((x,y), gamma):
    r = r0
    r_history = numpy.zeros((n_panels, 2), dtype=numpy.float32)

    for i in range(n_panels):
        r_history[i,:2] = r # Record current values
        #r_history[i,:4] = grad(r)
        fLast = f(r)
        r = r - gamma * grad(r) # Euler time step involving f(n)
        fNew = f(r)
        if abs(fNew - fLast) < convergence_criteria:
            break
    #r_history = r_history[0:i+1]
    print 'Found minimum in %i iterations' % i
    return r_history

def trim_gradient(values):
	# Process a gradient to terminate when it goes below y=0
	for i in range(len(values)-1):
		x0, y0 = values[i]
		x1, y1 = values[i+1]
		if y0 == 0: return values[:i]
	return values

for iy, y in enumerate(y_axis):
    for ix, x in enumerate(x_axis):
        points[iy, ix] = f((x, y))

pyplot.figure()
for gamma in gammas:
    data = gradient_descent(r0, gamma)
    data = trim_gradient(data)
    pyplot.plot(data[:,0], data[:,1], label=gamma)

pyplot.legend(loc='lower left')
pyplot.xlabel("x-axis"); pyplot.ylabel("y-axis")
pyplot.title("Finding the minima of Rosenbrock's Banana Function")
im = pyplot.imshow(points, extent=(xl, xu, yl, yu), origin='lower', cmap=matplotlib.cm.gray, norm=matplotlib.colors.LogNorm(vmin=0.2, vmax=200))

pyplot.colorbar(im, orientation='vertical')
pyplot.show()

ANSWER1 = """ """
ANSWER2 = 'Minima occurs at %.2f, %.2f' % (xmin, ymin)
print ANSWER2
