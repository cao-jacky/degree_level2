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
            image_array[i,j] = pix[i,j] # Stores RGBA into matching coord in array

    # R
    for i in range(size[0]):
        for j in range(size[1]):
            pixel_data = pix[i,j]
            image_r[i,j] = pixel_data[0]

            if pixel_data[0] <= 12:
                image_r[i,j] = 0
                pixel_data[0] = 0

    # G
    for i in range(size[0]):
        for j in range(size[1]):
            pixel_data = pix[i,j]
            image_g[i,j] = pixel_data[1]

            if pixel_data[1] <= 12:
                image_g[i,j] = 0
                image_array[i,j][1] = 0

    # B
    for i in range(size[0]):
        for j in range(size[1]):
            pixel_data = pix[i,j]
            image_b[i,j] = pixel_data[2]

            if pixel_data[2] <= 12:
                image_b[i,j] = 0
                image_array[i,j][2] = 0

    # Min and max values for the RGB values
    min_r, max_r = numpy.amin(image_r), numpy.amax(image_r)
    min_g, max_g = numpy.amin(image_g), numpy.amax(image_g)
    min_b, max_b = numpy.amin(image_b), numpy.amax(image_b)

    # Finds all the values within the array
    unique = numpy.unique(image_r)

    print image_array

    numpy.savetxt('red.txt', image_r, delimiter=',')

    return image_array

# Function to turn image into 'graph' histogram
def histogram(x):
    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over

    # Creating the a pyplot figure to plot the 'histogram'
    #pyplot.figure(?,size[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #pyplot.plot()

# Function to process image and measure the distances between intensity points

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    image_analyser.processor("image_1.tif")
