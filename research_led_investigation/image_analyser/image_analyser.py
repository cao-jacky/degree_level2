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

    array_unique = numpy.unique(processed) # Finds all unique values in the greyscale array
    array_unique_max = numpy.amax(array_unique) # Finds the max unique value
    array_unique_min = numpy.amin(array_unique) # Finds the min unique value

    # Finds the location of the max unique values in the greyscale array
    cols, rows = numpy.where(processed == array_unique_max)

    if horz == "yes": # Only plots horizontal intensity graph if you specify so
        horizontal = pyplot.figure() # Creating the a pyplot figure to plot the 'histogram'

        unique_rows = numpy.unique(rows) # Finding all unique values of 'rows'
        max_count_comparing = [0,0] # List to store the counts of how many times the maximum value appears in a row

        for i in range(size[1]):
            row_sliced = processed[:,i] # Slicing ith row out
            row_sliced = numpy.array(row_sliced.tolist()) # Converting row to list

            if i in unique_rows:
                # Number of times that the max value appears in the row
                row_max_count = numpy.sum(row_sliced == array_unique_max)
                max_count_comparing.append(row_max_count) # Stores value in the 2 item list
                max_count_comparing = max_count_comparing[-2:] # Limits the list to just 2 items
                # Calculates the difference between the number of times that max value appears in a row
                de = max_count_comparing[-1] - max_count_comparing[0]

                if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be changed
                    pyplot.plot(numpy.arange(size[0]), row_sliced)

        #pyplot.plot(numpy.arange(size[0]), row_sliced)


    else:
        print "you have specified no for a horizontal intensity graph"

    if vert == "yes": # only plots vertical intensity graph if you specify so
        vertical = pyplot.figure()
        for j in range(size[0]):
            column_sliced = processed[j,:] # Horizontal histogram creation

            pyplot.plot(column_sliced, numpy.arange(size[1]))
    else:
        print "you have specified no for a vertical intensity graph"

    pyplot.show()

# Function to process image and measure the distances between intensity points
# Maybe using the values for the greyscale?

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    #image_analyser.histogram("image_1.tif", "yes", "no")
    image_analyser.histogram("double circles.tif", "yes", "no")
    #image_analyser.histogram("double circles gain 1.tif")
    #image_analyser.histogram("double circles gain 2.tif")
    #image_analyser.histogram("double circles q.tif")
    #image_analyser.histogram("single disk gain 1.tif", "yes", "no")
    #image_analyser.histogram("single disk gain 2.tif")
    #image_analyser.histogram("metal slit in real space.tif")
