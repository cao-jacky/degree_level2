from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
    return (x**2) * (numpy.sin(x))

def g(x): # Indefinite integral of f(x)
    return (2*x*numpy.sin(x)) - (x**2 - 2)*numpy.cos(x)

def integrate_simpson(x0, x1, n_panels):
    panel_width = (x1 - x0) / n_panels
    sigma = 0 # total area

    for ix in range(n_panels):
        l_edge = x0 + ix * panel_width # Finding the left edge of this panel
        m = l_edge + panel_width / 2 # Calculating midpoint value as required
        r_edge = l_edge + panel_width
        # Applying values to Simpson's Rule
        sigma += ((r_edge-l_edge)/6) * (f(l_edge) + (4*f(m)) + f(r_edge))

    return sigma

# Range of panel sizes to be evaluated and bounds to integrate over
PANEL_COUNTS = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
x0, x1 = 0, 2

y_data = []
ref = g(x1) - g(x0)

for n in PANEL_COUNTS:
    s = integrate_simpson(x0, x1, n)
    error = abs((s-ref)/ref)
    print error
    y_data.append(error)

pyplot.figure(figsize=(6,6))
pyplot.title("Error scaling with Simpson's rule")
# Plot with visible markers and a line ('-o') and a marker size of 10
pyplot.plot(PANEL_COUNTS, y_data, '-o', ms = 10)
pyplot.xlabel("Number of panels used")
pyplot.ylabel("Relative error in the numerical method")
pyplot.loglog()
pyplot.show()

ANSWER1 = '''If you increase the number of panels used, then the accuracy
increases as the total incremental value for area becomes closer and closer to
the true analytical value.'''
ANSWER2 = '''If the function x^2 was integrated the accuracy would decrease as
the function x^2 is in the Simpson's Rule expansion itself, so the area of
calculated with the Rule will be the same as if it was analytically calculated
so there would be no error.'''
