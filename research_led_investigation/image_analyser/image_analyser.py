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

    # Arrays to store the individual RGB values
    image_r = numpy.zeros((size[0],size[1]), dtype=object)
    image_g = numpy.zeros((size[0],size[1]), dtype=object)
    image_b = numpy.zeros((size[0],size[1]), dtype=object)

    for i in range(size[0]):
        for j in range(size[1]):
            pixel = pix[i,j] # Pulling the RGBA data from the image
            # Converting 'sRGB' to greyscale using CIE 1931 Linear Luminance
            luminance = (0.2126 * pixel[0]) + (0.7152 * pixel[1]) + (0.0722 * pixel[2])
            image_array[i,j] = luminance # Stores value into matching coord in array

    #print image_array

    # 12 is the value we should use to 'block' out any excess light

    unique = numpy.size(image_array)

    print unique

    numpy.savetxt('image_array.txt', image_array, delimiter=',')

    return image_array

# Function to turn image into 'graph' histogram
def histogram(x):
    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over

    # Do we want horizontal or vertical intensity? The software has both - how
    # about I try and incorporate both somehow??

    for i in range?
    # Creating the a pyplot figure to plot the 'histogram'
    pyplot.figure()
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')

    pyplot.plot()

# Function to process image and measure the distances between intensity points
# Maybe using the values for the greyscale?

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    image_analyser.processor("image_1.tif")
