from __future__ import division
import numpy
import scipy.integrate
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Define all constants
r 			= 0.15 # Radius of cannonball in meters
rho_iron 	= 7874.00 # Density of iron in kgm**-3
g 			= 9.81 # Acceleration due to gravity in ms**-2
kappa 		= 0.47 # Drag coefficient of a sphere
rho_air 	= 1.23 # Density of air
t1 			= 25.00 # End time for our ODE integration in s
v0 			= 125.00 # Launch speed in ms**-1
n_panels 	= 400 # Number of panels to use

# Calculating mass and area of an iron cannonball of radius r
area = numpy.pi * r**2 # Cross sectional area of the cannon ball in m**2
mass = rho_iron * (4 * numpy.pi * r**3)/3 # Mass of the cannonball in kg

def f((x, y, vx, vy), time):
	# Calculate the forces on the cannonball
	v_mag = ((vx**2) + (vy**2))**0.5
	Fx_grav = - mass * g * 0 # Gravity, x-component
	Fy_grav = - mass * g # Gravity, y-component
	Fx_drag = - kappa * rho_air * area * v_mag * vx # Fluid resistance, x-comp-
	Fy_drag = - kappa * rho_air * area * v_mag * vy # Fluid resistance, y-comp-
	d_x 	= vx # dx/dt (velocity)
	d_y 	= vy # dy/dt
	d_vx 	= (Fx_grav + Fx_drag) / mass # dvx/dt (acceleration)
	d_vy 	= (Fy_grav + Fy_drag) / mass # dvy/dt
	return numpy.array((d_x, d_y, d_vx, d_vy))

def solve_euler(X0, t1, n_panels):
	dt = t1 / n_panels # Width of a panel
 	X, t = X0, 0 # Initialise simulation parameters
	# Allocate array to store (x,y,vx,vy) at all time points
	history = numpy.zeros((n_panels, len(X0)), dtype=numpy.float32)
	# Integrate each panel
	for i in range(n_panels):
		history[i] = X # Record current values
		t = i * dt
		# Calculate next time step using Euler
		X = X + f(X, t)*dt
	return history

pyplot.figure()
timebase = numpy.arange(0, t1, t1/n_panels) # Timebase for odeint function

def trim_trajectory(values):
	# Process a trajectory to terminate when it goes below y=0
	for i in range(len(values)-1):
		x0, y0, vx0, vy0 = values[i]
		x1, y1, vx1, vy1 = values[i+1]
		if y0 < 0: return values[:i]
	return values

proj_range = [] # Range corresponding to each angle
thetas = range(5, 90, 5) # Angles to explore, in degrees
thetas = numpy.radians(thetas) # Converting those angles into radians

pyplot.subplot(211) # Full width, half height, on top

for theta in thetas:
	vx, vy = v0*numpy.cos(theta), v0*numpy.sin(theta)
	initial_conditions = (0, 0, vx, vy)

	values_scipy = scipy.integrate.odeint(f, initial_conditions, timebase)
	values_euler = solve_euler(initial_conditions, t1, n_panels)
	values_scipy = trim_trajectory(values_scipy)
	values_euler = trim_trajectory(values_euler)
	# Calculate the range
	x_first, y_first, vx_first, vy_first = values_scipy[0]
	x_final, y_final, vx_final, vy_final = values_scipy[-1]
	rnge = x_final - x_first
	proj_range.append(rnge)

	pyplot.xlabel("Range (m)"); pyplot.ylabel("Height (m)")
	# Plot the odeint trajectory
	pyplot.plot(values_scipy[:,0], values_scipy[:,1], color='grey')
	# Plot the Euler trajectory
	pyplot.plot(values_euler[:,0], values_euler[:,1], color='blue',
	linestyle='--')
	pyplot.title("Range of an iron cannonball")

pyplot.plot(0, 0, color='blue', label='Euler', linestyle='--')
pyplot.plot(0, 0, color='grey', label='odeint')
pyplot.legend(loc='upper right')

pyplot.subplot(212)
pyplot.xlabel("Angle (degrees)"); pyplot.ylabel("Range (m)")
# Plot range vs theta
pyplot.plot(numpy.degrees(thetas), proj_range, "-+")
pyplot.show()

ANSWER1 = """ For the maximum range under the specified conditions, the angle
from the horizontal is about 40 to 45 degrees. """
ANSWER2 = """ As the air density increases the angle at which maximum range is
achieved, decreases. """
