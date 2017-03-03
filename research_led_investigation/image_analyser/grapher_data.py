 # Standard libraries being imported
from __future__ import division
from PIL import Image # Importing Python Image Library
from operator import add

import numpy
import image_analyser

""" Made by Jacky Cao for the Optical Fourier Transforms Level 2 Research Led
Investigation 2017 at Durham University """

def data(x):
    """ Function which outputs intensity averages for the horizontal and vertical
    direction.

    This function is a slimmed down version of the grapher function found in
    the image_analyser module. It does not have any of the plotting code within
    this.

    Input 'x' should be an image of format TIFF or PNG. """

    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over
    processed = image_analyser.processor(x)

    array_unique = numpy.unique(processed) # Finds all unique values in the greyscale array
    array_unique_max = numpy.amax(array_unique) # Finds the max unique value
    array_unique_min = numpy.amin(array_unique) # Finds the min unique value

    # Finds the location of the max unique values in the greyscale array
    cols, rows = numpy.where(processed == array_unique_max)

    """ For the horizontal direction """
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

    h_list_1 = numpy.delete(h_list_1, 0, 0) # Removes the initial numpy empty row
    h_list_1 = h_list_1.T # Transposing the array
    h_list_1 = numpy.average(h_list_1, axis=1) # Calculates the average for each column

    """ For the vertical direction """
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
    v_list_1 = numpy.delete(v_list_1, 0, 1) # Removes the initial numpy empty row
    v_list_1 = v_list_1.T # Transposes the array
    v_list_1 = numpy.average(v_list_1, axis=0) # Calculates the average for each row
    v_list_1 = numpy.flipud(v_list_1) # Flip list upside down

    return {'hzn_data':h_list_1 , 'ver_data':v_list_1}
