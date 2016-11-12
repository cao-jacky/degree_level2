from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

circle_radius = 1.0 # Unit circle radius

def estimate_pi(n):
    hits = 0 # Hit counter
    # Generate random points and store in numpy array
    random_numbers = numpy.random.uniform(size=(n,2))
    for i in range(n):
        x_coord = random_numbers[i][0] # x-component of the random point
        y_coord = random_numbers[i][1] # y-component of the random point
        random_radius = numpy.sqrt(x_coord**2 + y_coord**2) # Radius of point
        if random_radius <= circle_radius:
            hits = hits + 1
    pi_fraction = (hits / n)
    return 4 * pi_fraction # Calculate a value of pi

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

pyplot.semilogx(point_counts, error, "-+")
pyplot.xlabel("Number of points cast"); pyplot.ylabel("Scaling of the error")
pyplot.title("Estimating the value of $\pi$")
pyplot.show()

ANSWER1 = """ As the number of points increases we see that the accuracy
increases - the error between the calculated and analytical value of pi
decreases."""
