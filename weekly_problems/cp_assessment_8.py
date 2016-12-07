from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER    = "Jacky Cao"
USER_ID = "bbvw84"

# Defining variables
steps = 100

def newton_raphson(z):
    for i in range(steps):
        z = z - (z**4 - 1) / (4*z**3)
    return z

def converger(z):
    #z = newton_raphson(z)
    arraying = numpy.zeros((steps**2,), dtype=numpy.float32)
    for i in range(steps):
        z = z - (z**4 - 1) / (4*z**3)

        for lx, l in enumerate(z):
            #print l
            #arraying[lx] = i
            valueing = (l**4 - 1)

            #arraying[lx] = valueing
            print valueing

            if numpy.angle(valueing) == 0:
                arraying[lx] = i
                #break
    print arraying
    return arraying


x_values = numpy.linspace(-10,10,steps)
y_values = numpy.linspace(-10,10,steps)
xx, yy = numpy.meshgrid(x_values, y_values)

# Converts the values returned from Newton Raphson into an image of step x step
# resolution
pic = numpy.reshape(newton_raphson(numpy.ravel(xx+yy*1j)),[steps,steps])

pic2 = numpy.reshape(converger(numpy.ravel(xx+yy*1j)),[steps,steps])


#arrayers = numpy.zeros((steps,steps), dtype=numpy.float32)
#arrayers[:] = (xx+yy*1j)**4 - 1

#print arrayers

# rename pic
pyplot.figure()
pyplot.subplot(221)
im = pyplot.imshow(numpy.angle(pic), cmap='Accent')
pyplot.colorbar(im, orientation='vertical')

pyplot.subplot(222)
pyplot.imshow(pic2)

pyplot.show()
