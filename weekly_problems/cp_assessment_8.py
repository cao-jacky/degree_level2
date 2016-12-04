from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
m = 1
MAX_ITER = 200

def func(x):
    return x**2

def func_deriv(x):
    return 2*x

# create a seed point
def random_generator(): # Generate a random number to use each time called
    return numpy.random.uniform(size=(1,1)) * 5

def newton_raphson(x):
    n = random_generator()
    nr_history = numpy.zeros((MAX_ITER, 2), dtype=numpy.float32)

    for i in range(MAX_ITER):
        n = n - func(x) / func_deriv(x)
        nr_history[i][0] = x
        nr_history[i][1] = n
    print nr_history
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
test_123 = 100
root_history = numpy.zeros((MAX_ITER*100, 2), dtype=numpy.float32)
for i in range(test_123):
    x_point = random_generator()
    test_data = newton_raphson(x_point)
    pyplot.imshow(test_data, extent=(-5, 5, -5, 5), cmap='Accent')

xs = numpy.linspace(-5, 5, 100)

pyplot.plot(xs,func(xs))
pyplot.show()
