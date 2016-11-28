from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Define initial variables
xl, xu = -10, 40            # x-bounds
yl, yu = -10, 40            # y-bounds
x0, y0 = 30, 20             # Initial position of bacteria
r0 = numpy.array((x0,y0))   # Vector form of initial position
v = 2                       # Constant speed in microns per second
k = 0.2                     # Sensitivity
max_steps = 1000            # Max steps, 100 seconds, each step is 0.1s
dt = 0.1                    # Time step in seconds
bacterias = 20              # Number of bacteria being launched

# Exploring 1000 points in x and y
N_POINTS = 1000
dx = (xu-xl)/N_POINTS
dy = (yu-yl)/N_POINTS
y_axis = numpy.arange(yl, yu, dy) # Generating points between lower and upper y
x_axis = numpy.arange(xl, xu, dx) # Generating points between lower and upper x
points = numpy.zeros((len(y_axis), len(x_axis)))        # Generating points

def f((x,y)): # Energy density function
    return 2000 - (x**2 + y**2)

for iy, y in enumerate(y_axis):     # Explore all points and populate array
    for ix, x in enumerate(x_axis):
        points[iy, ix] = f((x, y))

def random_generator(): # Generate a random number to use each time called
    return numpy.random.uniform(size=(1,1))

def bacteria((x,y)):
    # Initial system for each bacterium
    bacteria_history = numpy.zeros((max_steps, 5), dtype=numpy.float32)
    r = r0; angle = 2 * numpy.pi * random_generator() # Position and angle
    shift = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(max_steps):
        bacteria_history[i][2] = i # Storing time of step
        bacteria_history[i,:2] = r # Storing position of molecule

        # Mean square displacement calculations
        posn_0 = bacteria_history[0,:2] # Particle position at time 0
        posn_max = numpy.array((0,0))   # Position of maximum energy
        posn_t = r                      # Particle at time 'i'
        msd_origin = numpy.average((posn_t-posn_0)**2)  # MSD from initial posn
        msd_max = numpy.average((posn_t-posn_max)**2)   # MSD from max E posn
        bacteria_history[i][3] = msd_origin # Index the value of msd_origin
        bacteria_history[i][4] = msd_max    # Index the value of msd_max

        # Energy minimisation calculations
        eNew = f(r.flatten())       # New energy level
        shift.append(eNew)          # Add to the 'shift' list
        shift = shift[-10:]         # Keep only the 10 most recent entries
        de = shift[-1] - shift[0]   # [-1] is newest entry, [0] is the oldest
        t_half = 1 + k * (de/dt)    # Half-life of a run event
        mean_life = t_half / numpy.log(2)

        if t_half < 0: # Calculating probabilites of tumbling
            p_nt = 1
        else:
            p_nt = 1 - numpy.exp(-dt / mean_life)

        if random_generator() < p_nt: # Generate new angle or continue on
            angle = 2 * numpy.pi * random_generator()
        else:
            x_coord = v * dt * numpy.cos(angle) # Random direction's x_coord
            y_coord = v * dt * numpy.sin(angle) # Random direction's y_coord
            r_new = numpy.hstack((x_coord, y_coord)) # Joining arrays together
            r = r + r_new
    return bacteria_history

pyplot.figure()


bac_av_origin = numpy.zeros((max_steps,(bacterias+1)), dtype=numpy.float32)
bac_av_energy = numpy.zeros((max_steps,(bacterias+1)), dtype=numpy.float32)

for i in range(bacterias):  # Plot all three plots
    b_d = bacteria(r0)      # Bacteria data

    pyplot.subplot(221)     # Energy field and bacteria tracks
    pyplot.plot(b_d[:,0], b_d[:,1])
    pyplot.imshow(points, extent=(xl, xu, yl, yu), origin='lower',
    cmap=matplotlib.cm.gray)
    pyplot.xlabel("x-axis $(\mu m )$"); pyplot.ylabel("y-axis $(\mu m)$")

    pyplot.subplot(222)     # Simplified trajectorys
    pyplot.plot((b_d[0][0], b_d[-1][0]), (b_d[0][1], b_d[-1][1]), '-o')
    pyplot.xlabel("x-axis $(\mu m )$"); pyplot.ylabel("y-axis $(\mu m)$")

    pyplot.subplot(212); pyplot.subplots_adjust(hspace=.25)
    pyplot.plot(b_d[:,2]*dt, b_d[:,3], '-r', alpha=0.05) # MSD for origin
    pyplot.plot(b_d[:,2]*dt, b_d[:,4], '-b', alpha=0.05) # MSD for max energy
    bac_av_origin[:,i] = b_d[:,3] # Storing MSD_origin in ith column
    bac_av_energy[:,i] = b_d[:,4] # Storing MSD_max in ith column
    pyplot.xlabel("Time $(s)$"); pyplot.ylabel("MSD $({\mu m}^2)$")

for i in range(max_steps):  # Storing MSD origin and energy in ith column
    bac_av_origin[i][20] = numpy.average(bac_av_origin[i,:19])
    bac_av_energy[i][20] = numpy.average(bac_av_energy[i,:19])

pyplot.plot(b_d[:,2]*dt,bac_av_origin[:,20], '-r',label='Initial, $(30,20)$')
pyplot.plot(b_d[:,2]*dt,bac_av_energy[:,20], '-b',label='Max E, $(0,0)$')
pyplot.legend(loc='lower right')
pyplot.suptitle("Bacteria as chemotaxis", fontsize='x-large')
pyplot.show()

ANSWER1 = """ If sensitivity becomes too small, the bacteria will not be able
to find the maximum energy. The half-life """
