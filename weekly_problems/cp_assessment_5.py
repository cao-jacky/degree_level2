from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

circle_radius = 1.0

def estimate_pi(n):
    # Hit counter
    hits = 0

    # Array to store the randomly generated points
    history = numpy.zeros((n,2), dtype=numpy.float32)

    # Seed
    seeded = numpy.random.seed(seed=1)

    # Generate the random numbers
    history = numpy.random.uniform(size=(n,2))
    for i in range(n):
        # Defining (x,y) of the randomly generated point
        x_coord = history[i][0]
        y_coord = history[i][1]

        # Calculating the radius of the random point
        random_radius = numpy.sqrt(x_coord**2 + y_coord**2)
        if random_radius <= circle_radius:
            hits = hits + 1

    # Calculating pi after finding all hits and misses
    pi_value = (hits / (n - hits))

    return pi_value

def measure_error(n):
    pi_values = estimate_pi(n)
    pi_values = numpy.mean((pi_values - numpy.pi)**2)**.5
    return pi_values

# Plotting code
pyplot.figure()
point_counts=[25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]
error = []

for j in range(0, len(point_counts)):
    points = point_counts[j]
    calculate = measure_error(points)
    error.append(calculate)

pyplot.plot(point_counts, error)
pyplot.xlabel("Number of points cast")
pyplot.ylabel("Scaling of the error")
pyplot.show()


ANSWER1 = """ """
