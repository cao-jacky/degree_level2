
from __future__ import division
import numpy
import scipy.integrate
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Define all constants
r = 0.15 # Radius of cannonball in meters
rho_iron = 7874.00 # Density of iron in kg/m**3
g = 9.81 # Acceleration due to gravity in ms**-2
kappa = 0.47 # Drag coefficient of a sphere
rho_air = 1.23 # Density of air
t1 = 25.00 # End time for our ODE integration in s
v0 = 125.00 # Launch speed in ms**-1 
n_panels = 100 # The number of panels to use 

# Calculating mass and area of cannonball of radium r, of iron
area = numpy.pi * r**2 # Cross sectional area of the cannon ball in m**2
mass = rho_iron * (4 * numpy.pi * r**3)/3 # Mass of the cannonball in kg

def f((x, y, vx, vy), t):
	# Calculate the forces on the cannonball
	Fx_grav = ?? # Gravity, x-component 
	Fy_grav = ?? # Gravity, y-component 
	Fx_drag = ??? # Fluid resistance, x-component
	Fy_drag = ??? # Fluid resistance, y-component 
	d_x = ??? # dx/dt
	d_y = ??? # dy/dt
	d_vx = ??? # dvx/dt (acceleration)
	d_vy = ??? # dvy/dt 
	return numpy.array((d_x, d_y, d_vx, d_vy))
	
def solve_euler(x, t1, n_panels):
	# Allocate somewhere to store (x,y,vx,vy) at all time points
	history = numpy.zeros((n_panels, len(x))
	???

pyplot.figure()
timebase = numpy.arange(0, t1, t1/n_panels)

def trim_trajectory(values):
	# Process a trajectory to terminate when it goes below y=0
	for i in range(len(values)-1):
		x0, y0, vx0, vy0 = values[i]
		x1, y1, vx1, vy1 = values[i+1]
		if y0 < 0: return values[:i]
		return values
		
proj_range = [] # Range corresponding to each angle
the tags = range(5, 90, 5) # Angles to explore, in degrees
pyplot.subplot(211) # Full width, half height, on top

for theta in thetas:
	vx, vy = ???, ???
	initial_conditions = (0, 0, vx, vy)
	
	values_scipy = scipy.integrate.odeint(f, initial_conditions, timebase)
	values_euler = solve_euler(initial_conditions, t1, n_panels)
	values_scipy = trim_trajectory(values_scipy)
	values_euler = trim_trajectory(values_euler)
	# Calculate the range
	x_first, y_first, vx_first, vy_first = values_euler[0]
	x_final, y_final, vx_final, vy_final = values_euler[-1]
	rnge = ???
	proj_range.append(rnge)
	# Plot the odeint trajectory - grey line
	# Plot the Euler trajectory - blue dashed line
	
pyplot.subplot(212)
# Plot range vs theta
pyplot.show()
