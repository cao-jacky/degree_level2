from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
m = 1
MAX_ITER = 500

def func(z):
    #z = x + j*y
    return z**4 - 1

def dfunc(z):
    return 4*z**3

# create a seed point
def random_generator(): # Generate a random number to use each time called
    return numpy.random.uniform(low=-10.0,high=10.0,size=(1,1))

def newton_raphson(x,y):
    y_im = 1j
    z = x + y_im*y
    for i in range(MAX_ITER):
        z = z - func(z) / dfunc(z)
    return z

pyplot.figure()

# Generate random numbers to store into test array to find the roots
steps = 500
root_history = numpy.zeros((steps, 3), dtype=numpy.float32)
for i in range(steps):
    x_values = numpy.asscalar(numpy.random.uniform(low=-10.0,high=10.0,size=(1,1)))
    y_values = numpy.asscalar(numpy.random.uniform(low=-10.0,high=10.0,size=(1,1)))
    x_point, y_point = x_values, y_values
    test_data = newton_raphson(x_point,y_point)
    root_history[i][0] = x_values
    root_history[i][1] = y_values
    root_history[i][2] = numpy.angle(test_data)


    # do it like previous weeks, enumerate - banana function thing!

print root_history

pyplot.imshow(root_history, extent=(-5, 5, -5, 5), cmap='cool', norm=matplotlib.colors.LogNorm(vmin=0.2, vmax=200))

xs = numpy.linspace(-5, 5, 100)


pyplot.show()
