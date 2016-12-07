from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
steps = 250

def newton_raphson(z):
    for i in range(1000):
        z = z - (z**4 - 1) / (4*z**3)
    return z

def newton_raphson_ey(z):
    for i in range(500):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        #print z, zLast
        #if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            #break
    return numpy.angle(z)

def newton_raphson2(z):
    for i in range(15):
        zLast = z
        z = z - (z**4 - 1) / (4*z**3)
        #print z, zLast
        if abs(numpy.absolute(z)-numpy.absolute(zLast)) < 1e-6:
            break
    return i

x_values = numpy.linspace(-1.5,1.5,steps)
y_values = numpy.linspace(-1.5,1.5,steps)
xx, yy = numpy.meshgrid(x_values, y_values)

# Converts the values returned from Newton Raphson into an image of step x step
# resolution
pic = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])

npts = 250; xmin = -1.5; xmax = 1.5
xs = numpy.linspace(xmin, xmax, npts)
tmp = numpy.zeros(npts, dtype=int)
zs = numpy.outer(tmp, tmp)  # A square array

for i in range(npts):
    for j in range(npts):
        z = xs[i]+ xs[j]*1j
        zs[i,j] = newton_raphson2(z)

npts2 = 300; xmin2 = -1.5; xmax2 = 1.5
xs2 = numpy.linspace(xmin2, xmax2, npts2)
tmp2 = numpy.zeros(npts2, dtype=int)
zs2 = numpy.outer(tmp2, tmp2)  # A square array

for i in range(npts2):
    for j in range(npts2):
        z2 = xs2[i]+ xs2[j]*1j
        zs2[i,j] = newton_raphson_ey(z2)

#pic2 = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])


#arrayers = numpy.zeros((steps,steps), dtype=numpy.float32)
#arrayers[:] = (xx+yy*1j)**4 - 1

#print arrayers

# rename pic
pyplot.figure()
pyplot.subplot(221)
im = pyplot.imshow(numpy.angle(pic), origin='lower')
#pyplot.colorbar(im, orientation='vertical')

pyplot.subplot(222)
pyplot.imshow(zs, origin='lower')

pyplot.subplot(223)
pyplot.imshow(zs2, origin='lower', cmap='Accent')

pyplot.show()
