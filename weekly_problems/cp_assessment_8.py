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
    z = x + j*y
    return z***4 - 1

def dfunc(z):
    return 4*z**3

# create a seed point
def random_generator(): # Generate a random number to use each time called
    return numpy.random.uniform(low=-10.0,high=10.0,size=(1,1))

def linear_generator():
    x = random_generator()
    return numpy.linspace(-x, x, 100)

def newton_raphson(x):
    x = x
    nr_history = numpy.zeros((MAX_ITER, 2), dtype=numpy.float32)

    for i in range(MAX_ITER):
        x = x - func(x) / dfunc(x)
        nr_history[i][0] = x
        nr_history[i][1] = func(x)
        if x < 1e-15:
            break
    return nr_history

def f(x,y):
    z0 = 0
    c = x + 1j*y
    z = z0
    MAX_ITER = 200

    for i in range(MAX_ITER):
        z = z**2 + c
        if abs(s) > 1:
            break
    return i == MAX_ITER-1

pyplot.figure()

# Generate random numbers to store into test array to find the roots
root_history = numpy.zeros((1, 2), dtype=numpy.float32)
steps = 1000
x_values = numpy.linspace(-50, 50, steps)
for i in range(steps):
    x_point = x_values[i]
    test_data = newton_raphson(x_point)
    pyplot.plot(test_data[:,0],test_data[:,1])

#print root_history
pyplot.imshow(test_data, extent=(-5, 5, -5, 5), cmap='cool', norm=matplotlib.colors.LogNorm(vmin=0.2, vmax=200))

xs = numpy.linspace(-5, 5, 100)


pyplot.show()
