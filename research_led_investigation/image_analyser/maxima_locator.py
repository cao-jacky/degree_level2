from __future__ import division
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image # Importing Python Image Library
from operator import add

import numpy
import scipy.ndimage

import image_analyser
import grapher_data

def gradient_calculator(x1, x2, y1, y2):
    """ Simple gradient calculator to calculate gradient between points.

    Input is the coordinates for the two points you want to calculate gradient
    between.

    Output is the value of the gradient between those two points. """
    return (y2-y1)/(x2-x1)

# Function to process image and measure the distances between intensity points
def maxima_locator(x,text):
    """ Processes image and attempts to locate the positions of the intensity
    points on both horizontal and vertical intensity graphs.

    Input 'x' should be a string name for the image of format TIFF or PNG -
    not JPEG.

    Output is two arrays listing the locations of the supposed positions of
    maximas. """
    im = Image.open(x)
    size = im.size # Gets the width and height of the image to iterate over
    processed = image_analyser.processor(x)

    graph_data = grapher_data.data(x)
    hozn_data = graph_data['hzn_data']
    vert_data = graph_data['ver_data']

    # I want to calculate the gradient between points until it changes sign, if there is a sign change - that is where a maxima is at.

    # Initialise required lists, variables
    i, j = range(size[0])[0], range(size[1])[0]
    grad_h = 0
    grad_v = 0
    grad_h_array, grad_v_array = numpy.zeros(size[0]), numpy.zeros(size[1])

    h_maximas = [] # List for horizontal maximas
    v_maximas = [] # List for vertical maximas

    # Setting the boundary limits to find maxima in
    hl, hu = 400, 1000      # Horizontal lower and upper
    #hl, hu = 0, size[0]
    vl, vu = 0, size[1]     # Vertical lower and upper

    # For the horizontal intensity graph
    for i in range(numpy.size(hozn_data)):
        grad_h = gradient_calculator(i-1, i, hozn_data[i-1], hozn_data[i])
        if grad_h < 0:
            grad_h_array[i] = 1 # If the gradient is less than 0 (grad = negative), at that location, flag a "1"

    # For the vertical intensity graph
    for j in range(numpy.size(vert_data)):
        grad_v = gradient_calculator(j-1, j, vert_data[j-1], vert_data[j])
        if grad_v < 0:
            grad_v_array[j] = 1 # If the gradient is less than 0 (grad = negative), at that location, flag a "1"

    # Looping through the 0 and 1's array within a specified range
    for i in range(hl, hu): # Specified within the horizontal range
        # Checking for the sequence [0,1] - this indicates a maxima - too sensitive, there are multiple cases where this is just not true
        if grad_h_array[i] == 1 and grad_h_array[i-1] == 0:     # Checks if current value is 1 and if the one before that is 0
            if numpy.sum(grad_h_array[i:i+10]) == 10:           # Looks ahead and checks if there are 1's within the next how many elements
                h_maximas.append(i)                             # Stores the location of the maxima

    # For the vertical direction, same idea as above for horizontal
    for j in range(vl, vu):
        #print j
        if grad_v_array[j] == 0 and grad_v_array[j-1] == 1:     # Checks if current value is 0 and if the one before that is 1
            if numpy.sum(grad_v_array[j:j+10]) == 5:
                v_maximas.append(j)


    if text == 'yes':
        # Printing both maxima lists
        print "supposed vertical maxima points:", v_maximas
        print "supposed horizontal maxima points:", h_maximas

    # Removing any points that are not maximas
    # Horizontally
    #del h_maximas[9]
    # Vertically
    #del v_maximas[]

    if text == 'yes':
        print "cleaned up horizontal maxima points:", h_maximas
        print "cleaned up vertical maxima points:", v_maximas

    return {'h_maximas':h_maximas, 'v_maximas':v_maximas}
