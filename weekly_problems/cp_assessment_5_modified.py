from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

circle_radius = 1.0 # Unit circle radius

def random_numbers(n): # Function to generate random points
    random_points = numpy.random.uniform(size=(n,2))
    return random_points

def estimate_pi(n):
    hits = 0 # Hit counter
    # Generate random points and store in numpy array
    generated_points = random_numbers(n)
    for i in range(n):
        x_coord = generated_points[i][0] # x-component of the random point
        y_coord = generated_points[i][1] # y-component of the random pointhbury
        random_radius = numpy.sqrt(x_coord**2 + y_coord**2) # Radius of point
        if random_radius <= circle_radius:
            hits = hits + 1
    pi_fraction = (hits / n)
    return 4 * pi_fraction # Calculate a value of pi

def hits_returner(n):
    hits = 0 # Hit counter
    generated_points = random_numbers(n)
    extra_zeroes = numpy.zeros((n, 1), dtype=generated_points.dtype)
    storing_array = numpy.concatenate((generated_points,extra_zeroes), axis=1)
    for i in range(n):
        x_coord = generated_points[i][0] # x-component of the random point
        y_coord = generated_points[i][1] # y-component of the random point
        random_radius = numpy.sqrt(x_coord**2 + y_coord**2) # Radius of point
        if random_radius <= circle_radius:
            hits = hits + 1
            storing_array[i][2] = 1
    return storing_array

def measure_error(n):
    pi_values = numpy.zeros((80), dtype=numpy.float32)
    for j in range(80):
        pi_values[j] = estimate_pi(n)
    square_error = numpy.mean((pi_values - numpy.pi)**2)**.5
    return square_error

# Graphing the error and counts
pyplot.figure()
point_counts=[25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]
error = [] # List to store error of each point count respectively

# Plotting each item in the set of point counts
for k in range(0, len(point_counts)):
    points = point_counts[k]
    error_point_counts = measure_error(points)
    error.append(error_point_counts)

pyplot.subplot(211)
pyplot.semilogx(point_counts, error, "-o", linestyle='none')
pyplot.xlabel("Number of points cast"); pyplot.ylabel("Scaling of the error")
pyplot.title("Estimating the value of $\pi$")

point_count = [6400]

pyplot.subplot(212)
pyplot.xlabel("x-axis"); pyplot.ylabel("y-axis")
for l in range(0, len(point_count)):
    point = point_count[l]
    point_counted = hits_returner(point)
    for i in point_counted:
        pointed = i
        if pointed[2] == 1:
            pyplot.scatter(pointed[0], pointed[1], color='green')
        if pointed[2] == 0:
            pyplot.scatter(pointed[0], pointed[1], color='red')

pyplot.subplots_adjust(hspace=.5)
pyplot.scatter(0, 0, color='green', label='Inside')
pyplot.scatter(0, 0, color='red', label='Outside')
pyplot.legend(loc='lower left')
pyplot.show()
