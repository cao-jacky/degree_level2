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

""" Made by Jacky Cao for the Fourier Transforms Research Led Investigation 2017 """

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

    return image_array

def grapher(x, horz, vert):
    """ Function which outputs intensity graphs for images in the horizontal
    and vertical directions, an intensity 'heat map' is also created and plotted
    on the same figure.

    This does not generally work for images created than 1280x1024px's - it
    creates quite an 'interesting' figure.

    An average of the intensities should be shown along with the individual
    intensities which sum them up.

    Input 'x' should be an image of format TIFF or PNG. 'horz' and 'vert'
    specifies if you want the horizontal and vertical intensity graphs or not -
    the inputs should be 'yes' or 'no'. """

    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over
    processed = processor(x)

    array_unique = numpy.unique(processed) # Finds all unique values in the greyscale array
    array_unique_max = numpy.amax(array_unique) # Finds the max unique value
    array_unique_min = numpy.amin(array_unique) # Finds the min unique value

    # Finds the location of the max unique values in the greyscale array
    cols, rows = numpy.where(processed == array_unique_max)

    fig = pyplot.figure()
    # Creating gridspec grid for the plots
    gs = gridspec.GridSpec(2, 2, width_ratios=[1,4], height_ratios=[4,1], wspace=0.0, hspace=0.0)

    if horz == "yes": # Only plots horizontal intensity graph if you specify so
        horizontal = pyplot.subplot(gs[3]) # Creating the a subplot figure for horizontal
        horizontal.set_xlabel("Distance (px)")
        horizontal.set_ylabel("Intensity")

        horizontal.set_xlim([0,size[0]]) # Ensures the figure is same size as heat map
        horizontal.set_ylim([0,255]) # Ensures the figure is same size as heat map

        #horizontal.yaxis.set_visible(False)

        unique_rows = numpy.unique(rows) # Finding all unique values of 'rows'
        # Max count horizontal comparing
        mc_h_comparing = [0,0] # List to store the counts of how many times the maximum value appears in a row

        h_list_1 = numpy.empty(size[0]) # An initial empty row so that additional rows can be added to this

        for i in range(size[1]):
            row_sliced = processed[:,i] # Slicing ith row out
            row_sliced = numpy.array(row_sliced.tolist()) # Converting row to list

            if i in unique_rows:
                # Number of times that the max value appears in the row
                row_max_count = numpy.sum(row_sliced == array_unique_max)
                mc_h_comparing.append(row_max_count) # Stores value in the 2 item list
                mc_h_comparing = mc_h_comparing[-2:] # Limits the list to just 2 items
                # Calculates the difference between the number of times that max value appears in a row
                de = mc_h_comparing[-1] - mc_h_comparing[0]

                if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be
                    h_list_2 = row_sliced
                    h_list_1 = numpy.vstack((h_list_1,h_list_2)) # Adds rows vertically
                    pyplot.plot(numpy.arange(size[0]), row_sliced, alpha=0.01)

        h_list_1 = numpy.delete(h_list_1, 0, 0) # Removes the initial numpy empty row
        h_list_1 = h_list_1.T # Transposing the array
        h_list_1 = numpy.average(h_list_1, axis=1) # Calculates the average for each column

        pyplot.plot(numpy.arange(size[0]), h_list_1)

    else:
        print "you have specified a no for a horizontal intensity graph"

    if vert == "yes": # Only plots vertical intensity graph if you specify so
        vertical = pyplot.subplot(gs[0])
        vertical.set_xlabel("Intensity")
        vertical.set_ylabel("Distance (px)")

        vertical.set_ylim([0,size[1]]) # Ensures the figure is same size as heat map
        vertical.set_xlim([0,255]) # Ensures the figure is same size as heat map

        #vertical.xaxis.set_visible(False)

        unique_cols = numpy.unique(cols) # Finding all unique values of 'cols'
        # Max count vertical comparing
        mc_v_comparing = [0,0] # List to store the counts of how many times the maximum value appears in a col

        v_list_1 = numpy.empty(size[1]) # An initial empty row
        v_list_1 = numpy.vstack(v_list_1) # Turning an empty row into an empty column

        for j in range(size[0]):
            column_sliced = processed[j,:] # Slicing jth column out
            column_sliced = numpy.array(column_sliced.tolist()) # Converting column to list

            if j in unique_cols:
                # Number of times that the max value appears in the column
                col_max_count = numpy.sum(column_sliced == array_unique_max)
                mc_v_comparing.append(col_max_count) # Stores value in the 2 item list
                mc_v_comparing = mc_v_comparing[-2:] # Limits the list to just 2 items
                # Calculates the difference between the number of times that max value appears in a row
                de = mc_v_comparing[-1] - mc_v_comparing[0]

                if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be changed
                    v_list_2 = numpy.vstack(column_sliced) # v_list_2 into a column
                    v_list_1 = numpy.hstack((v_list_1,v_list_2)) # Adds columns horizontally
                    pyplot.plot(numpy.flipud(column_sliced), numpy.arange(size[1]), alpha=0.01)
        v_list_1 = numpy.delete(v_list_1, 0, 1) # Removes the initial numpy empty row
        v_list_1 = v_list_1.T # Transposes the array
        v_list_1 = numpy.average(v_list_1, axis=0) # Calculates the average for each row

        pyplot.plot(numpy.flipud(v_list_1), numpy.arange(size[1]))
    else:
        print "you have specified a no for a vertical intensity graph"

    # Plotting intensity map
    xl, xu = 0, size[0] # x-limits
    yl, yu = 0, size[1] # y-limits

    processed_data = numpy.array(processed.tolist()).T # Create separate array for heat map, convert into list

    heat_map = pyplot.subplot(gs[1])
    heat_map_plot = pyplot.imshow(processed_data, extent=(xl, xu, yl, yu), aspect='auto') # imshow function to show a 'heatmap' of any image

    heat_map.xaxis.set_visible(False)
    heat_map.yaxis.set_visible(False)

    heat_map.set_xlim([0,size[0]])
    heat_map.set_ylim([0,size[1]])

    return {'hzn_data':h_list_1 , 'ver_data':v_list_1}
