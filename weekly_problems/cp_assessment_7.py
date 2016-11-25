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
bacterias = 1       # Number of bacteria being launched

def f(x,y):
    return 2000 - (x**2 + y**2)

def bacteria(x,y):
    bacteria_history = numpy.zeros((bacterias, ))



    return bacteria_history

pyplot.figure()
pyplot.plot()
pyplot.show()
