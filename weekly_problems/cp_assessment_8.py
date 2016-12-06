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

def newton_raphson(z):
    for i in range(MAX_ITER):
        z = z - func(z) / dfunc(z)
    return z

pyplot.figure()

# Generate random numbers to store into test array to find the roots
steps = 1000
root_history = numpy.zeros((steps, 3), dtype=numpy.float32)
x_values = numpy.linspace(-10,10,steps)
y_values = numpy.linspace(-10,10,steps)
xx, yy = numpy.meshgrid(x_values, y_values)

pic = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])

pyplot.imshow(numpy.angle(pic))

pyplot.show()
