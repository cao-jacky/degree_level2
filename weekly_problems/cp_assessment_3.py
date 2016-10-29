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
		# Calculate next time step
		n = n + f(n) * dt # Euler time step involving f(n)
	return n_history

def solve_heun(n0, t1, n_panels):
	dt = t1 / n_panels # Width of a panel
	# Initialise simulation parameters
	n, t = n0, 0
	# Make an array to hold the counts at each time point in
	n_history = numpy.zeros((n_panels,), dtype=numpy.float32)
	for i in range(n_panels):
		n_history[i] = n # Record current values
		k_0 = f(n)
		k_1 = f(n + k_0 * dt)
		n = n + (dt / 2) * (k_0 + k_1)
	return n_history

t1 = 60 # Integrate over time range 0 <= t <= t1
N_PANELS = 15 # Number of panels to divide the time range into
N0 = 1200 # Initial conditions - number of nuclei


# Time at the start of each panel - used for plotting and analytical solution
timebase = numpy.arange(0, t1, t1/N_PANELS)
# Evaluate various methods
n_analytic 	= analytic(N0, timebase)
n_euler 	= solve_euler(N0, t1, N_PANELS)
n_heun 		= solve_heun(N0, t1, N_PANELS)
# Graphing time
pyplot.figure()
pyplot.subplot(211) # Top plot - count vs time for methods
pyplot.plot(timebase, n_analytic, color='grey', label='Analytic')
pyplot.plot(timebase, n_euler, color='red', label='Euler')
pyplot.plot(timebase, n_heun, color='blue', label='Heun', linestyle='--')
pyplot.xlabel("Time in hours")
pyplot.ylabel("Number of undecayed atoms")
pyplot.legend(loc='upper right')

pyplot.subplot(212) # Bottom plot - error vs time for numerics
pyplot.semilogy() # Make y-axis log
err_euler 	= abs(n_euler-n_analytic)/n_analytic
err_heun 	= abs(n_heun-n_analytic)/n_analytic
pyplot.plot(timebase, err_euler, color='red', label='Euler')
pyplot.plot(timebase, err_heun, color='blue', label='Heun')
pyplot.xlabel("Time in hours")
pyplot.ylabel("Absolute relative error")
pyplot.legend(loc='upper right')

pyplot.show()
ANSWER1 = """Heun's method is more accurate than Euler's as it uses another
method to predict the next point"""
