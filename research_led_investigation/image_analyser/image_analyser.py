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

import grapher_data             # Module output the raw data for graphing
import fourier_transforms       # Module which has the Fourier transform/intensity functions
import maxima_locator           # Module to locate maximas
import chi_squared_calculator   # Module to calculate chi-squared

""" Made by Jacky Cao for the Optical Fourier Transforms Level 2 Research Led
Investigation 2017 at Durham University """

# Optionally set font to Computer Modern to avoid common missing font errors
matplotlib.rc('font', family='serif', serif='cm10')

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']

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

    horizontal.yaxis.tick_right()
    horizontal.yaxis.set_label_position('right')

    horizontal.tick_params(axis='y', which='major', labelsize=34)
    horizontal.tick_params(axis='x', labelsize=34)

    horizontal.set_xlabel(r'\textbf{Distance (px)}', fontsize=40)
    horizontal.set_ylabel(r'\textbf{Greyscale Intensity}', fontsize=34)

    horizontal.set_xlim([0,size[0]])    # Ensures the figure is same size as heat map
    horizontal.set_ylim([0,255])        # Ensures the figure is same size as heat map

    y_ticks = numpy.array((0, 200))     # Setting custom tick values
    custom_y_ticks = ['$0$','$200$']
    pyplot.yticks(y_ticks, custom_y_ticks)

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
    h_list_no = numpy.shape(h_list_1)               # Counting number of intense rows before averaging
    print h_list_no
    h_list_std = numpy.std(h_list_1, axis=1)        # Calculates standard deviation for each column
    h_list_1 = numpy.average(h_list_1, axis=1)      # Calculates the average for each column

    # Saving h_list_1 so that it can be used in MATLAB
    numpy.savetxt('saved_data/h_list_1.txt', h_list_1, delimiter=',')

    # Plotting theoretical intensity
    x = numpy.linspace(0,size[0],200)
    five_slits = (20 * fourier_transforms.five_slit(x)) + 10
    #pyplot.plot(x, five_slits)

    pyplot.plot(numpy.arange(size[0]), h_list_1, '-r')

    # Plotting horizontal maxima points for reference
    #for i in range(numpy.size(h_maxima_points)):
        #pyplot.scatter(h_maxima_points[i], h_list_1[h_maxima_points[i]])

    """ For the vertical direction """
    vertical = pyplot.subplot(gs[0])

    vertical.xaxis.tick_top()
    vertical.xaxis.set_label_position('top')

    vertical.tick_params(axis='x', which='major', labelsize=34)
    vertical.tick_params(axis='y', labelsize=34)

    vertical.set_xlabel(r'\textbf{Greyscale Intensity}', fontsize=34)
    vertical.set_ylabel(r'\textbf{Distance (px)}', fontsize=34)

    vertical.set_ylim([0,size[1]])  # Ensures the figure is same size as heat map
    vertical.set_xlim([0,255])      # Ensures the figure is same size as heat map

    x_ticks = numpy.array((0, 200))     # Setting custom tick values
    custom_x_ticks = ['$0$','$200$']
    pyplot.xticks(x_ticks, custom_x_ticks)

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
            # Calculates the difference between the number of times that max value appears in a column
            de = mc_v_comparing[-1] - mc_v_comparing[0]

            if de > 0 : # Plots intensity only for truly 'intense' rows, comparator value can be changed
                v_list_2 = numpy.vstack(column_sliced)          # v_list_2 into a column
                v_list_1 = numpy.hstack((v_list_1,v_list_2))    # Adds columns horizontally
                pyplot.plot(numpy.flipud(column_sliced), numpy.arange(size[1]), alpha=0.01, color = '0.1')

    v_list_1 = numpy.delete(v_list_1, 0, 1)         # Removes the initial numpy empty column
    v_list_1 = v_list_1.T                           # Transposes the array
    v_list_no = numpy.shape(v_list_1)               # Counting number of intense columns before averaging
    v_list_std = numpy.std(v_list_1, axis=0)        # Calculates standard deviation for each column
    v_list_1 = numpy.average(v_list_1, axis=0)      # Calculates the average for each column
    v_list_1 = numpy.flipud(v_list_1)               # Flip list upside down

    # Saving v_list_1 so that it can be used in MATLAB
    numpy.savetxt('saved_data/v_list_1.txt', v_list_1, delimiter=',')

    pyplot.plot(v_list_1, numpy.arange(size[1]), '-r')

    # Plotting vertical maxima points for reference
    #for j in range(numpy.size(v_maxima_points)):
        #pyplot.scatter(v_list_1[v_maxima_points[j]], v_maxima_points[j])

    # Plotting intensity map
    xl, xu = 0, size[0] # x-limits
    yl, yu = 0, size[1] # y-limits

    processed_data = numpy.array(processed.tolist()).T # Create separate array for heat map, convert into list

    heat_map = pyplot.subplot(gs[1])
    heat_map_plot = pyplot.imshow(processed_data, extent=(xl, xu, yl, yu), aspect='auto') # imshow function to show a 'heatmap' of any image

    heat_map.xaxis.set_visible(False), heat_map.yaxis.set_visible(False)
    heat_map.set_xlim([0,size[0]]), heat_map.set_ylim([0,size[1]])

    position=fig.add_axes([0.9,0.26,0.02,0.64])
    colourbar = pyplot.colorbar(heat_map_plot, orientation='vertical',cax=position)
    colourbar.ax.tick_params(labelsize=34)

    #pyplot.subplot(gs[2]) # Spare plot
    #pyplot.plot([0,0],[1,1])

    pyplot.savefig('analysed_image.pdf', bbox_inches='tight')

    """ Superimposing graphs ontop of each other, i.e. horizontal and vertical,
    or any of them with theory """
    # Superimposing both horizontal and vertical intensity graphs
    v_zeros = numpy.empty(size[0]-size[1]+16) # Adding extra zeros to align both graphs
    v_zeros[:] = numpy.NAN
    v_list_1 = numpy.hstack((v_zeros, v_list_1))

    superimpose = pyplot.figure()
    superimpose.canvas.set_window_title('Overlapped Intensity Graphs')
    pyplot.plot(numpy.arange(size[0]), h_list_1, '-r', label=r'\textbf{Horizontal Intensity}')
    pyplot.plot(numpy.arange(size[1]+(size[0]-size[1])+16), v_list_1.T, '-b', label=r'\textbf{Vertical Intensity}')

    #pyplot.axvspan(270, 1100, color='grey', alpha=0.05) # For the double airy disks, highlights area to compare

    # Plotting theoretical intensity
    x = numpy.linspace(0,size[0],size[0])   # Generates points
    x_round = numpy.round(x,decimals=0) # Rounds generated points to no decimal places
    x_round = x_round.astype(int)       # Turns them into integer values
    x_round[-1] = 1279                  # Changes 1280 value to 1279
    numpy.savetxt('saved_data/x_gen.txt',x_round,delimiter=',')

    s_h_list_1 = list(h_list_1[x_round])        # Shortened h_list_1
    numpy.savetxt('saved_data/s_h_list_1.txt',s_h_list_1,delimiter=',')
    s_h_list_std = list(h_list_std[x_round])    # Selects out the standard deviation values
    s_h_list_no = numpy.shape(s_h_list_1)       # Finds number of values in arrray

    five_slits = fourier_transforms.five_slit(x)
    #jinc = fourier_transforms.jinc(x)
    #jinc = numpy.vectorize(jinc)

    sinc = (1/20) * fourier_transforms.sinc(x)

    """ Chi-squared calculations """
    # sinc
    sinc_std_error = h_list_std/numpy.sqrt(h_list_no[1])
    for i in range(numpy.size(sinc_std_error)):
        if sinc_std_error[i] == 0:
            sinc_std_error[i] = 1
    numpy.savetxt('saved_data/sinc_std_error.txt', sinc_std_error, delimiter='-')
    sinc_cs = chi_squared_calculator.sinc(x,h_list_1,sinc_std_error)

    print sinc_cs

    # five_slits
    five_std_error = s_h_list_std/numpy.sqrt(h_list_no[1])
    for i in range(numpy.size(five_std_error)):
        if five_std_error[i] == 0:
            five_std_error[i] = 1
    numpy.savetxt('saved_data/five_std_error.txt', five_std_error, delimiter='-')
    five_cs = chi_squared_calculator.five_slit(x,s_h_list_1,five_std_error)

    print five_cs

    # jinc
    # Dealing with the jinc data
    jinc_data = numpy.loadtxt('saved_data/jinc.txt')                # Load the jinc theoretical data
    jinc_theo_data = numpy.loadtxt('saved_data/theo_domain.txt')    # Load the domain of the data
    jinc_theo_data = numpy.delete(jinc_theo_data,numpy.s_[157:200]) # Removes the greater than domain points
    jinc_round = numpy.round(jinc_theo_data,decimals=0)        # Rounds generated points to no decimal places
    jinc_round = jinc_round.astype(int)
    jinc_round[-1] = 1279
    numpy.savetxt('saved_data/jinc_round.txt', jinc_round, delimiter='-')

    #jinc_data = list(jinc_data[jinc_round])

    jinc_list = list(h_list_1[jinc_round])        # Shortened h_list_1
    numpy.savetxt('saved_data/jinc_list.txt',jinc_list,delimiter=',')
    jinc_list = list(h_list_std[jinc_round])    # Selects out the standard deviation values
    jinc_list_no = numpy.shape(jinc_list)       # Finds number of values in arrray
    print jinc_list_no

    jinc_std_error = jinc_list/numpy.sqrt(jinc_list_no)

    print numpy.shape(jinc_round),jinc_list_no, numpy.shape(jinc_std_error)
    for i in range(numpy.size(jinc_std_error)):
        if jinc_std_error[i] == 0:
            jinc_std_error[i] = 1
    numpy.savetxt('saved_data/jinc_std_error.txt', jinc_std_error, delimiter='-')
    jinc_cs = chi_squared_calculator.jinc(jinc_round,jinc_list,jinc_std_error)

    jinc_data_plot = numpy.delete(jinc_data,numpy.s_[157:200])

    print jinc_cs

    #pyplot.plot(x, sinc, '-g', label=r'\textbf{Theoretical Model}')
    #pyplot.plot(x, five_slits, '-g', label=r'\textbf{Theoretical Model}')
    #pyplot.plot(jinc_round, jinc_data_plot, '-g', label=r'\textbf{Theoretical Model}')

    pyplot.ylim(0,256) # Limits the size of the y-axis

    pyplot.tick_params(axis='y', labelsize=25)
    pyplot.tick_params(axis='x', labelsize=25)

    pyplot.xlabel(r'\textbf{Distance (px)}', fontsize=25)
    pyplot.ylabel(r'\textbf{Intensity (Wm$^{-2}$)}', fontsize=25)

    pyplot.legend(loc='upper right')

    pyplot.savefig('overlapped_intensity.pdf', bbox_inches='tight')

    #pyplot.show()

#Testing and running the code
if __name__ == '__main__':
    import image_analyser

    #image_analyser.grapher("images/week_2/single disk gain 2.tif")

    #image_analyser.grapher("images/week_3/Grating 1 #1.tif")
    #image_analyser.grapher("images/week_3/Grating 2 #1.tif")
    #image_analyser.grapher("images/week_3/Grating 3 #1.tif")

    image_analyser.grapher("images/week_5/single metal slit 2.tif")

    image_analyser.grapher("images/week_4/5 slit.tif")

    image_analyser.grapher("images/week_2/double circles gain 2.tif")

    #image_analyser.grapher("images/week_6/4.tif")
