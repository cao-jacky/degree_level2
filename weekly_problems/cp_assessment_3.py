from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

T_HALF = 20.8 # Half-life of isotope in hours
TAU = T_HALF / numpy.log(2) # Average lifetime of the isotope in hours

def f(n):
	return - n / TAU # Decay rate of n atoms with half life TAU

def analytic(n0, timebase):
	n_analytic = n0 * (numpy.e ** (- timebase / TAU))
	return n_analytic

def solve_euler(n0, t1, n_panels):
	dt = t1 / n_panels # Width of a panel
	# Initialise simulation parameters
	n, t = n0, 0
	# Make an array to hold the counts at each time point in
	n_history = numpy.zeros((n_panels,), dtype=numpy.float32)
	# Integrate each panel
	for i in range(n_panels):
		n_history[i] = n # Record current values
		t = i * dt # more accurate than t = t + dt as less rounding errors
		# Mind you, this DEQ doesn't depend on time anyway
		# Calculate next time step
		n = n + f(n) * dt # Euler time step involving f(n)

	return n_history

def solve_heun(n0, t1, n_panels):
	# A lot like Euler but with more maths
	#return n_history
	return "poop"

N0 = 1000 # Initial conditions - number of nuclei
T1 = 60 # Integrate over time range 0 <= t <= t1
N_PANELS = 10 # Number of panels to divide the time range into

# Time at the start of each panel - used for plotting and analytical solution
timebase = numpy.arange(0, T1, T1/N_PANELS)
# Evaluate various methods
n_analytic = analytic(N0, timebase)
n_euler = solve_euler(N0, T1, N_PANELS)
n_heun = solve_heun(N0, T1, N_PANELS)
# Graphing time
pyplot.figure()
pyplot.subplot(211) # Top plot - count vs time for methods
#??? # Plot n_analytic vs timebase etc.

pyplot.subplot(212) # Bottom plot - error vs time for numerics
pyplot.semilogy() # Make y-axis log
err_euler = abs(n_euler-n_analytic)/n_analytic
#err_heun = ???

pyplot.show()
ANSWER1 = " "
