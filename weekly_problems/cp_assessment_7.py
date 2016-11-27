from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Define initial variables
xl, xu = -10, 50             # x-bounds
yl, yu = -10, 50             # y-bounds
x0, y0 = 30, 20     # Initial position of bacteria
v = 2               # Constant speed in microns per second
k = 0.2               # Sensitivity
tumble_time = 0.1   # Tumble event duration in seconds
total_time = 100    # Total time of function running, in seconds
max_steps = 1000    # Max steps, 100 seconds
time_step = 0.1     # Time step, in seconds

r0 = numpy.array((x0,y0))

# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS

y_axis = numpy.arange(yl, yu, dy) # Generating points between lower and upper y
x_axis = numpy.arange(xl, xu, dx) # Generating points between lower and upper x
points = numpy.zeros((len(y_axis), len(x_axis)))        # Generating points

def f((x,y)):
    return 2000 - (x**2 + y**2)

for iy, y in enumerate(y_axis):     # Explore all points and populate array
    for ix, x in enumerate(x_axis):
        points[iy, ix] = f((x, y))

def random_generator(p):
    """Generates random number to use"""

    random_position = numpy.random.uniform(size=(1,1)) # Initial direction of the bacteria
    random_coord = numpy.random.uniform(size=(1,2)) # Generates coordinate for the bacteria

    return random_position if p == 1 else random_coord

def bacteria((x,y)):
    bacteria_history = numpy.zeros((max_steps, 2), dtype=numpy.float32) # Initial array to store bacteria information
    r = r0
    dt = 1 # Time step in seconds
    angle = 3.73

    a = 0

    shift = [a, a, a, a, a, a, a, a, a, a]
    increasing, decreasing = 0, 0
    print "begins"

    for i in range(max_steps):
        bacteria_history[i,:2] = r
        #print r

        #p_nt = 0.5
        eNew = f(r.flatten()) # New energy level
        shift.append(eNew) # add to the python list
        shift = shift[-10:] # keep only the 10 most recent entries
        de = shift[-1] - shift[0] # [-1] is the newest entry, [0] is the oldest
        #print 'de is:', de
        #print shift
        t_half = 1 + k * (de/dt)

        if t_half < 0:
            t_half = - t_half

        print 'half-life is:', t_half

        mean_life = t_half / numpy.log(2)

        if t_half < 0.1:
            #p_nt = 0
            b = 0
        else:
            p_nt = numpy.exp(-dt / mean_life) # Probability of not tumbling, i.e. not changing coordinate, it's happy
            #print 'probability of not tumbling is:', p_nt

        # p_nt is a varibale, it changes, we need to change it to account for the energy field - make it related to the energy field

        if random_generator(1) < p_nt: # if the randomly generated probability is less than probability of not tumbling, then tumble
            # Tumbling
            angle = 2 * numpy.pi * random_generator(1)
        else:
            dist = v * dt
            x_coord = dist * numpy.cos(angle) # Random direction x_coord
            y_coord = dist * numpy.sin(angle) # Random direction y_coord
            r_new = numpy.hstack((x_coord, y_coord))
            r = r + r_new

    return bacteria_history

bacterias = 2     # Number of bacteria being launched

pyplot.figure()
for i in range(bacterias):
    bacteria_data = bacteria(r0)
    pyplot.plot(bacteria_data[:,0], bacteria_data[:,1])


im = pyplot.imshow(points, extent=(xl, xu, yl, yu), origin='lower',
cmap=matplotlib.cm.gray)
pyplot.xlabel("x-axis (microns)"); pyplot.ylabel("y-axis (microns)")
pyplot.show()

numpy.savetxt('bacteria_history.txt', bacteria_data, delimiter=',')   # X is an array