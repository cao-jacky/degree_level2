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

def df(x,y):
    return "123"

def random_generator(p):
    """Generates random number to use"""

    random_position = numpy.random.uniform(size=(1,1)) # Initial direction of the bacteria
    random_coord = numpy.random.uniform(size=(1,2)) # Generates coordinate for the bacteria

    return random_position if p == 1 else random_coord

def bacteria((x,y)):
    bacteria_history = numpy.zeros((max_steps, 2), dtype=numpy.float32) # Initial array to store bacteria information
    r = r0
    dt = 1 # Time step of 1s

    time_step_count = 0 # Tracking total time
    eOriginal = f(r0)
    shift = [0, 0, 0, 0, 0, 0, 0]

    for i in range(max_steps):
        bacteria_history[i,:2] = r
        if time_step_count < total_time: # going over steps until reach limit
            time_step_count = time_step_count + time_step
        #print time_step_count

        r_flat = r.flatten()
        eNew = f(r_flat) # New energy level
        shift.append(eNew) # add to the python list
        shift = shift[-10:] # keep only the 10 most recent entries
        de = shift[-1] - shift[0] # [-1] is the newest entry, [0] is the oldest
        #print de

        t_half = 1 + k * (de/dt) #Half-life, de is the rate of change of energy fielf for 1s
        #print t_half

        if t_half < 0.1:
            prob = 1
        else:
            mean_life = t_half / numpy.log(2)
            #print mean_life
            prob = numpy.exp(- dt / mean_life)  # Probability of not tumbling
            print prob

        if random_generator(1) > prob: # tumble then move
            # Tumbling
            angle = 2 * numpy.pi * random_generator(1)
            x_coord = 2 * numpy.cos(angle) # Random direction x_coord
            y_coord = 2 * numpy.sin(angle) # Random direction y_coord
            r_new = numpy.hstack((x_coord, y_coord))

            # Moving
            r = r + r_new
        else:
            if bacteria_history[i][0] == bacteria_history[i-1][0]:
                r_new = 0 # If initially no tumble, allow bacteria to try again
            else:
                r_new = r

            r = r + r_new

    # half_life = 1 + k * df
    #print shift
    print bacteria_history
    return bacteria_history

bacterias = 1      # Number of bacteria being launched

pyplot.figure()
for i in range(bacterias):
    bacteria_data = bacteria(r0)
    pyplot.plot(bacteria_data[:,0], bacteria_data[:,1])


im = pyplot.imshow(points, extent=(xl, xu, yl, yu), origin='lower',
cmap=matplotlib.cm.gray)
pyplot.xlabel("x-axis (microns)"); pyplot.ylabel("y-axis (microns)")
pyplot.show()

numpy.savetxt('bacteria_history.txt', bacteria_data, delimiter=',')   # X is an array
