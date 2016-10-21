from __future__ import division
import numpy 
import matplotlib.pyplot as pyplot 

USER = "Jacky Cao"
USER_ID = "bbvw84"

def f(x):
 return x**2 #add proper indents to this, cannot really do on an ipad 

def g(x):
 return x**3 / 3

def integrate_simpson(x0, x11, n_panels):
 panel_width = (x1-x0) / n_panels
 sigma = 0 #total area
