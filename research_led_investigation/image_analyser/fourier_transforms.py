# Standard libraries being imported
from __future__ import division
from PIL import Image # Importing Python Image Library
from operator import add
from scipy.special import j1
from scipy.integrate import quad

import numpy

# Defining initial variables
D = ?
u, v =
omega = numpy.sqrt(u**2 + v**2)

def j(rho):
    return (1/(2*numpy.pi)) *

def fourier_transform(x, y):
    ft_fn = j(2*numpy.pi*j(rho))

def jinc(x):
    if x == 0.0:
        return 0.5
    return j1(x) / x

def cos(x):
    return numpy.cos(x)

def double_aperture(x1, x2):
    jinc = np.vectorize(jinc)
    return 2 * cos(x1) * ((numpy.pi * (D ** 2))/4) * jinc(x)

def intensity(x):
    x1 = numpy.pi *
    intensity_called = double_aperture(x1, x2) ** 2
    return intensity_called
