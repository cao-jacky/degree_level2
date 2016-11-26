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
total_time = 100    # Total time of function running, in seconds
max_steps = 1000    # Max steps, 100 seconds
time_step = 0.1     # Time step, in seconds

r0 = numpy.array((x0,y0))

def f(x,y):
    return 2000 - (x**2 + y**2)

def df(x,y):
    return "123"

def random_generator(p):
    """ Generates either a random direction, or point for bacteria to
    head in

    For p = 1:
        random_position is generated
        p = 0:
        random_coord is generated"""

    random_position = numpy.random.uniform(size=(1,1)) # Initial direction of the bacteria
    random_coord = numpy.random.uniform(size=(1,2)) # Generates coordinate for the bacteria

    return random_position if p == 1 else random_coord

def bacteria((x,y)):
    bacteria_history = numpy.zeros((max_steps, 2), dtype=numpy.float32) # Initial array to store bacteria information
    r = r0
    t_half = 0          # Half-life
    mean_lifetime = 0   # Mean lifetime
    prob = 0.5          # Probability of not tumbling, implement full function later
    time_step_count = 0

    if time_step_count < max_steps: # going over steps until reach limit
        time_step_count = time_step_count + 1

        for i in range(max_steps):
            bacteria_history[i,:2] = r

            if random_generator(1) < prob: # tumble then move
                angle = 2 * numpy.pi * random_generator(1)
                x_coord = 2 * numpy.cos(angle) # Random direction x_coord
                y_coord = 2 * numpy.sin(angle) # Random direction y_coord

                r_new = numpy.hstack((x_coord, y_coord))

                r = r + r_new

                #bacteria_history[i][0] =  bacteria_history[i-1][0] + x_coord
                #bacteria_history[i][1] =  bacteria_history[i-1][1] + y_coord

            else:
                r = r


    print bacteria_history

    # half_life = 1 + k * df

    return bacteria_history

bacteria_data = bacteria(r0)
numpy.savetxt('bacteria_history.txt', bacteria_data, delimiter=',')   # X is an array


pyplot.figure()
pyplot.plot(bacteria_data[:,0], bacteria_data[:,1], '-o')
pyplot.xlabel("x-axis (microns)"); pyplot.ylabel("y-axis (microns)")
pyplot.show()
