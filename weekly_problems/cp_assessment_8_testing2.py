# Import modules
import cmath as cm   # For complex numbers
import numpy as np
import matplotlib.pyplot as plt

# Define functions and global variables
def newton_raphson_step(z):
    """One iteration of the Newton-Raphson method."""
    return z - (z**3 - 1)/(3.0*z**2)

def newton_raphson(x_start, nits=20):
    x = x_start
    for i in range(nits):
        x = newton_raphson_step(x)
    return x

roots = [cm.exp(2.0*k*cm.pi*1j / 3.0) for k in range(3)]  # Known roots

def get_value(x,y):
    """Starting from the initial guess x + iy,
    apply the Newton-Raphson method.
    Returns 1,2,3 if corresponding roots are found; 0 otherwise."""
    val = 0
    eps = 1.0e-10
    z = newton_raphson(complex(x, y))
    for i in range(3):
        if abs(z - roots[i]) < eps:
            val = i+1
    return val

npts = 1000; xmin = -1.5; xmax = 1.5
xs = np.linspace(xmin, xmax, npts)
tmp = np.zeros(npts, dtype=int)
zs = np.outer(tmp, tmp)  # A square array
for i in range(npts):
    for j in range(npts):
        zs[i,j] = get_value(xs[i], xs[j])

fig = plt.gcf()
fig.set_size_inches(10,10)
plt.imshow(zs.T, origin='lower')
plt.show()
