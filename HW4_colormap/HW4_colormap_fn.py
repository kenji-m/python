# =======================================================================
# OCNG689.600
# Homework 4: Colormap
# Created by: Kenji Miyajima
# Date: 2013-10-17
# -----------------------------------------------------------------------
#  This script have a function that read data from the website and then
#  create and return the colormap. An additional function run and plot
#  the colormap.
# =======================================================================

import numpy as np
import urllib as ulb
import matplotlib.pyplot as plt

def colormap (name):
    '''
    1) This function is design for reading the colormap data from the web:
       http://geography.uoregon.edu/datagraphics/
    2) Return the color dictionary and the number of colors
    '''

    # open text file from the web
    url = 'http://geography.uoregon.edu/datagraphics/color/'+name
    f = ulb.urlopen(url)

    # creating a empty list
    r = []; g = []; b = []

    # reading the RGB data from the website
    for line in f.readlines()[2:]:
        colors = line.split()
        r.append(float(colors[0]))
        g.append(float(colors[1]))
        b.append(float(colors[2]))

    cmap_len = len(r)
    reds = [((float(n)/(cmap_len-1)), r[n-1], r[n]) for n in range(cmap_len)]
    greens = [((float(n)/(cmap_len-1)), g[n-1], g[n]) for n in range(cmap_len)]
    blues = [((float(n)/(cmap_len-1)), b[n-1], b[n]) for n in range(cmap_len)]

    # creating dictionary for colors
    cdict = {'red':reds, 'green':greens, 'blue':blues}

    # return the colormap, dicsionary, and the number of colors
    my_cmap = plt.matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return my_cmap

if __name__ == '__main__':
    '''
    This function call colormap function with file name, and then
    plot the colormap data in random points. Finally save the figure
    in the directry
    '''
    cmap = colormap('BuDRd_18.txt')
    plt.title('Color map plot for BuDRd_18.txt', style ='italic')
    plt.pcolor(np.random.rand(20,20),cmap= cmap)
    plt.colorbar()
    plt.show()
    plt.savefig('my_color_map.pdf')
