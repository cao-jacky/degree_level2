 # Standard libraries being imported
from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
# Importing Python Image Library
from PIL import Image

# What functions do I want?

# Function to process image and turn into RGB values
def processor(x):
    """ Input 'x' should be a string name for the image of format TIFF or PNG -
    not JPEG """
    im = Image.open(x)
    pix = im.load()
    size = im.size # Gets the width and height of the image to iterate over

    # Creating an array to store the RGBA values from the image and their coord
    image_array = numpy.zeros((size[0],size[1]), dtype=object)

    for i in range(size[0]):
        for j in range(size[1]):
            pixel = pix[i,j] # Pulling the RGBA data from the image
            # Converting 'sRGB' to greyscale using CIE 1931 Linear Luminance
            luminance = (0.2126 * pixel[0]) + (0.7152 * pixel[1]) + (0.0722 * pixel[2])
            image_array[i,j] = luminance # Stores value into matching coord in array

    numpy.savetxt('image_array.txt', image_array, delimiter=',')

    return image_array

# Function to turn image into 'graph' histogram
def histogram(x, horz, vert):
    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over
    processed = processor(x)

    first_row = processed[:,0]
    empty_row = numpy.zeros((1,size[1]))

    # Do we want horizontal or vertical intensity? The software has both - how
    # about I try and incorporate both somehow??

    if horz == "yes":
        # Creating the a pyplot figure to plot the 'histogram'
        horizontal = pyplot.figure()
        for i in range(size[1]):
        #for i in range(0, size[1], 2):
            row_sliced = processed[:,i] # Horizontal histogram creation
            if i < range(size[1]-1):
                newArray = processed[[i,i+1],:]
            #print newArray

            row_sum = numpy.sum(row_sliced)
            #print row_sum

            ## I want a function which checks consecutive elements for no change in
            ## it's greyscale value. If there is no value in the whole row, remove
            ## or ignore that row somehow - don't plot it?
            ##
            ## Then with the actual areas of high intensity we can average and
            ## use some form of 'integration time'?

            ## How about a loop which checks for the maximum and minimum value
            ## within the row? If a greater maximum value is found on the next row,
            ## dump the previous row? Or do not plot it?


            row_values = []
            average_values = []

            for k in range(size[0]):
                value = row_sliced[k] # Slicing out individual elements of row
                row_values.append(value) # Adding to the row_values list
                #row_average = numpy.average(numpy.asarray(row_values)) # Calculating average of a row
                #average_values.append(row_average) # Adding average to a list

            pyplot.plot(numpy.arange(size[0]), row_sliced)

        print numpy.unique(average_values)
    else:
        print "you have specified no for horizontal intensity graph"

        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')

    if vert == "yes":
        vertical = pyplot.figure()
        for j in range(size[0]):
            column_sliced = processed[j,:] # Horizontal histogram creation

            pyplot.plot(column_sliced, numpy.arange(size[1]))
    else:
        print "you have specified no for vertical intensity graph"

    pyplot.show()

# Function to process image and measure the distances between intensity points
# Maybe using the values for the greyscale?

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    image_analyser.histogram("image_1.tif", "yes", "no")
    #image_analyser.histogram("double circles.tif")
    #image_analyser.histogram("double circles gain 1.tif")
    #image_analyser.histogram("double circles gain 2.tif")
    #image_analyser.histogram("double circles q.tif")
    #image_analyser.histogram("single disk gain 1.tif")
    #image_analyser.histogram("single disk gain 2.tif")
    #image_analyser.histogram("metal slit in real space.tif")
