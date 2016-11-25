from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining data to use
xl, xu = -0.2, 1.2              # x-bounds
yl, yu = -0.2, 1.2              # y-bounds
x0, y0 = 0.2, 1.0               # Initial position
r0 = numpy.array((x0,y0))       # Vector form of the initial position
max_iter = 100000               # Maximum number of iterations
convergence_criteria = 1e-11    # Convergence critera

# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS

y_axis = numpy.arange(yl, yu, dy) # Generating points between lower and upper y
x_axis = numpy.arange(xl, xu, dx) # Generating points between lower and upper x

points = numpy.zeros((len(y_axis), len(x_axis)))        # Generating points
gammas = [0.001, 0.0008, 0.000003, 0.00000007, 0.002]   # Various gammas

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
    r_history = numpy.zeros((max_iter, 2), dtype=numpy.float32)

    for i in range(max_iter):
        r_history[i,:2] = r         # Record current values
        fLast = f(r)                # Last value calculated of f(r)
        r = r - gamma * grad(r)     # Gradient Descent method applied
        fNew = f(r)                 # New value of f(vec(r)) after GD
        if abs(fNew - fLast) < convergence_criteria:
            break                   # Terminate if convergence criteria met
    r_history = r_history[0:i+1]    # Trim the r_history array
    print 'Found minimum in %i iterations' % i
    return r_history

for iy, y in enumerate(y_axis):     # Explore all points and populate array
    for ix, x in enumerate(x_axis):
        points[iy, ix] = f((x, y))

pyplot.figure()
for gamma in gammas: # Call function and plot for different gamma values
    data = gradient_descent(r0, gamma)
    pyplot.plot(data[:,0], data[:,1], label=gamma)
    if gamma == gammas[-1]:
        final_gamma = gradient_descent(r0, gammas[-1])
        xmin, ymin = final_gamma[-1][0], final_gamma[-1][1]

# Show a greyscale colourmap of the data
im = pyplot.imshow(points, extent=(xl, xu, yl, yu), origin='lower',
cmap=matplotlib.cm.gray, norm=matplotlib.colors.LogNorm(vmin=0.2, vmax=200))
pyplot.xlabel("x-axis"); pyplot.ylabel("y-axis")
pyplot.legend(loc='lower left')
pyplot.title("Finding the minima of Rosenbrock's Banana Function")
pyplot.colorbar(im, orientation='vertical')
pyplot.show()

ANSWER1 = """ As larger values of the step size parameter (gamma) is chosen
we see that the Gradient Descent method struggles to find the value of the
minimum. If a value of gamma is chosen which provides the best GD trajectory,
it finds the minimum with the least number of iterations. As gamma varies from
this best value, we see that the number of iterations required increases - at
times the number of iterations reaches the maximum limit."""
ANSWER2 = 'Minima occurs at %.2f, %.2f' % (xmin, ymin)
