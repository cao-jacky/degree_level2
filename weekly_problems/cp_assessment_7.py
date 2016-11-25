from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Define initial variables
x0, y0 = 30, 20     # Initial position of bacteria
v = 2               # Constant speed in microns per second
k = 2               # Sensitivity
tumble_time = 0.1   # Tumble event duration in seconds
bacterias = 1       # Number of bacteria being launched


r0 = numpy.array((x0,y0))

def f(x,y):
    return 2000 - (x**2 + y**2)

def df(x,y):
    return "123"


def bacteria((x,y)):
    bacteria_history = numpy.zeros((bacterias, 3), dtype=numpy.float32) # Initial array to store bacteria information
    random_position = numpy.random.uniform(size=(1,1)) # Initial direction of the bacteria
    r = r0
                        # Half-life
                        # Mean lifetime
    prob = 0.5          # Probability of not tumbling, implement with function later

    for i in range(bacterias):
        bacteria_history[i,:2] = r

        if


    print bacteria_history
    print random_position

    # half_life = 1 + k * df

    return bacteria_history

bacteria_data = bacteria(r0)

pyplot.figure()
pyplot.plot(bacteria_data[:,0], bacteria_data[:,1], '-o')
pyplot.show()
