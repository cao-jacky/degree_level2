 # Standard libraries being imported
from __future__ import division
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image # Importing Python Image Library
from operator import add

import numpy
import scipy.ndimage
import matplotlib.pyplot as pyplot
import matplotlib.colors

import grapher_data         # Module output the raw data for graphing
import fourier_transforms   # Module which has the Fourier transform/intensity functions
import maxima_locator       # Module to locate maximas

""" Made by Jacky Cao for the Optical Fourier Transforms Level 2 Research Led
Investigation 2017 at Durham University """

# Function to process image and turn into RGB values
def processor(x):
    """ Input 'x' should be a string name for the image of format TIFF or PNG -
    not JPEG.

    Output is an array corresponding to the image, each RGB pixel has been
    replaced with a singular grayscale value. """
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

    return image_array

def maxima_calculator(x):
    """ Calculates the distances between maxima"""

    # Import the data from maxima_locator function
    maxima_located = maxima_locator.maxima_locator(x, 'no')
    h_located = maxima_located['h_maximas'] # Calling definition for h_maximas
    v_located = maxima_located['v_maximas'] # Calling definition for v_maximas

    # Calculating distance between maximas
    h_spacing = (h_located[-1] - h_located[0]) / len(h_located) # Horizontally
    v_spacing = (v_located[-1] - v_located[0]) / len(v_located) # Vertically

    print "distance between horizontal maximas:", h_spacing, "pixels"
    print "distance between vertical maximas:", v_spacing, "pixels"

# Function to turn image into 'graph' histogram
def grapher(x):
    """ Function which outputs intensity graphs for images in the horizontal
    and vertical directions, an intensity 'heat map' is also created and plotted
    on the same figure.

    This does not generally work for images created than 1280x1024px's - it
    creates quite an 'interesting' figure.

    An average of the intensities should be shown along with the individual
    intensities which sum them up.

    Input 'x' should be an image of format TIFF or PNG.  """

    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over
    processed = processor(x)

    maxima_locator_s = maxima_locator.maxima_locator(x,'no')    # maxima_locator function summoned
    h_maxima_points = maxima_locator_s['h_maximas']             # Selecting h_maximas definition
    v_maxima_points = maxima_locator_s['v_maximas']             # Selecting v_maximas definition

    array_unique = numpy.unique(processed)          # Finds all unique values in the greyscale array
    array_unique_max = numpy.amax(array_unique)     # Finds the max unique value
    array_unique_min = numpy.amin(array_unique)     # Finds the min unique value

    # Finds the location of the max unique values in the greyscale array
    cols, rows = numpy.where(processed == array_unique_max)

    fig = pyplot.figure()
    fig.canvas.set_window_title('Image Analyser')
    # Creating gridspec grid for the plots
    gs = gridspec.GridSpec(2, 2, width_ratios=[1,4], height_ratios=[4,1], wspace=0.0, hspace=0.0)

    """ For the horizontal direction """
    horizontal = pyplot.subplot(gs[3])  # Creating the a subplot figure for horizontal

    horizontal.tick_params(axis='y', which='major', labelsize=9)

    horizontal.set_xlabel("Distance (px)")
    horizontal.set_ylabel("Intensity")

    horizontal.set_xlim([0,size[0]])    # Ensures the figure is same size as heat map
    horizontal.set_ylim([0,255])        # Ensures the figure is same size as heat map

    #horizontal.yaxis.set_visible(False)

    unique_rows = numpy.unique(rows)    # Finding all unique values of 'rows'
    # Max count horizontal comparing
    mc_h_comparing = [0,0]              # List to store the counts of how many times the maximum value appears in a row

    h_list_1 = numpy.empty(size[0])     # An initial empty row so that additional rows can be added to this

    for i in range(size[1]):
        row_sliced = processed[:,i]                         # Slicing ith row out
        row_sliced = numpy.array(row_sliced.tolist())       # Converting row to a list

        if i in unique_rows:
            # Number of times that the max value appears in the row
            row_max_count = numpy.sum(row_sliced == array_unique_max)
            mc_h_comparing.append(row_max_count)            # Stores value in the 2 item list
            mc_h_comparing = mc_h_comparing[-2:]            # Limits the list to just 2 items
            # Calculates the difference between the number of times that max value appears in a row
            de = mc_h_comparing[-1] - mc_h_comparing[0]

            if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be changed
                h_list_2 = row_sliced
                h_list_1 = numpy.vstack((h_list_1,h_list_2)) # Adds rows vertically
                pyplot.plot(numpy.arange(size[0]), row_sliced, alpha=0.01, color = '0.1')

    h_list_1 = numpy.delete(h_list_1, 0, 0)         # Removes the initial numpy empty row
    h_list_1 = h_list_1.T                           # Transposing the array
    h_list_1 = numpy.average(h_list_1, axis=1)      # Calculates the average for each column

    # Plotting theoretical intensity
    x = numpy.linspace(0,size[0],200)
    five_slits = (20 * fourier_transforms.five_slit(x)) + 10
    #pyplot.plot(x, five_slits)

    pyplot.plot(numpy.arange(size[0]), h_list_1, '-r')

    # Plotting horizontal maxima points for reference
    for i in range(numpy.size(h_maxima_points)):
        pyplot.scatter(h_maxima_points[i], h_list_1[h_maxima_points[i]])

    """ For the vertical direction """
    vertical = pyplot.subplot(gs[0])

    vertical.xaxis.tick_top()
    vertical.xaxis.set_label_position('top')
    vertical.tick_params(axis='x', which='major', labelsize=9)

    vertical.set_xlabel("Intensity")
    vertical.set_ylabel("Distance (px)")

    vertical.set_ylim([0,size[1]])  # Ensures the figure is same size as heat map
    vertical.set_xlim([0,255])      # Ensures the figure is same size as heat map

    #vertical.xaxis.set_visible(False)

    unique_cols = numpy.unique(cols)    # Finding all unique values of 'cols'
    # Max count vertical comparing
    mc_v_comparing = [0,0]              # List to store the counts of how many times the maximum value appears in a col

    v_list_1 = numpy.empty(size[1])     # An initial empty row
    v_list_1 = numpy.vstack(v_list_1)   # Turning an empty row into an empty column

    for j in range(size[0]):
        column_sliced = processed[j,:]  # Slicing jth column out
        column_sliced = numpy.array(column_sliced.tolist()) # Converting column to list

        if j in unique_cols:
            # Number of times that the max value appears in the column
            col_max_count = numpy.sum(column_sliced == array_unique_max)
            mc_v_comparing.append(col_max_count)    # Stores value in the 2 item list
            mc_v_comparing = mc_v_comparing[-2:]    # Limits the list to just 2 items
            # Calculates the difference between the number of times that max value appears in a row
            de = mc_v_comparing[-1] - mc_v_comparing[0]

            if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be changed
                v_list_2 = numpy.vstack(column_sliced)          # v_list_2 into a column
                v_list_1 = numpy.hstack((v_list_1,v_list_2))    # Adds columns horizontally
                pyplot.plot(numpy.flipud(column_sliced), numpy.arange(size[1]), alpha=0.01, color = '0.1')

    v_list_1 = numpy.delete(v_list_1, 0, 1)         # Removes the initial numpy empty row
    v_list_1 = v_list_1.T                           # Transposes the array
    v_list_1 = numpy.average(v_list_1, axis=0)      # Calculates the average for each row
    v_list_1 = numpy.flipud(v_list_1)               # Flip list upside down

    pyplot.plot(v_list_1, numpy.arange(size[1]), '-r')

    # Plotting vertical maxima points for reference
    for j in range(numpy.size(v_maxima_points)):
        pyplot.scatter(v_list_1[v_maxima_points[j]], v_maxima_points[j])

    # Plotting intensity map
    xl, xu = 0, size[0] # x-limits
    yl, yu = 0, size[1] # y-limits

    processed_data = numpy.array(processed.tolist()).T # Create separate array for heat map, convert into list

    heat_map = pyplot.subplot(gs[1])
    heat_map_plot = pyplot.imshow(processed_data, extent=(xl, xu, yl, yu), aspect='auto') # imshow function to show a 'heatmap' of any image

    heat_map.xaxis.set_visible(False), heat_map.yaxis.set_visible(False)
    heat_map.set_xlim([0,size[0]]), heat_map.set_ylim([0,size[1]])

    #cax = pyplot.subplot(gs[1])
    #pyplot.colorbar(heat_map_plot, cax=cax, orientation='vertical')

    #pyplot.subplot(gs[2]) # Spare plot
    #pyplot.plot([0,0],[1,1])

    """ For double circular apertures """
    # Superimposing both horizontal and vertical intensity graphs
    v_zeros = numpy.zeros(size[0]-size[1]+16) # Adding extra zeros to align both graphs
    v_list_1 = numpy.hstack((v_zeros, v_list_1))

    superimpose = pyplot.figure()
    superimpose.canvas.set_window_title('Overlapped Intensity Graphs')
    pyplot.plot(numpy.arange(size[0]), h_list_1, '-r', label='Horizontal Intensity')
    #pyplot.plot(numpy.arange(size[1]+(size[0]-size[1])+16), v_list_1.T, '-b', label='Vertical Intensity')

    # Plotting theoretical intensity
    x = numpy.linspace(0,size[0],200)
    #x = numpy.linspace(-1, 2, 25)
    #x = numpy.arange(0,size[0],1)
    five_slits = fourier_transforms.five_slit(x)
    #jinc = fourier_transforms.jinc(x)
    #jinc = numpy.vectorize(jinc)

    sinc = (1/20) * fourier_transforms.sinc(x)

    #pyplot.plot(x, five_slits, '-g', label='Theoretical Model')
    #pyplot.plot(x, jinc, '-g', label='Theoretical Model')
    pyplot.plot(x, sinc, '-g', label='Theoretical Model')

    pyplot.ylim(0,256) # Limits the size of the y-axis

    pyplot.xlabel("Distance (px)")
    pyplot.ylabel("Intensity")

    pyplot.legend(loc='upper right')

    pyplot.show()

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    #image_analyser.maxima_calculator("images/week_2/double circles gain 2.tif")
    #image_analyser.grapher("images/week_2/double circles gain 2.tif")

    #image_analyser.maxima_calculator("images/week_2/single disk gain 2.tif")
    #image_analyser.grapher("images/week_2/single disk gain 2.tif")

    #image_analyser.maxima_calculator("images/week_3/Grating 1 last but 2.tif")
    #image_analyser.grapher("images/week_3/Grating 1 last but 2.tif")

    #image_analyser.maxima_calculator("images/week_4/5 slit.tif")
    #image_analyser.grapher("images/week_4/5 slit.tif")

    #image_analyser.maxima_calculator("images/week_5/Sungle metal slit.tif")
    image_analyser.grapher("images/week_5/Sungle metal slit 2.tif")
    #image_analyser.grapher("images/week_5/5 slit focused.tif")
