#--------------------------------------------------------------------------
# Kenji Miyajima
# OCNG689. Final Plotting No.1
# 2013-12-04
#--------------------------------------------------------------------------
# 1) Three functions draw a default mtplotlib pcolormesh color map,
# an improved version of it by reading color data from ColorBrewer website,
# and a simple prettyplotlib color map.
# 2) Put three color maps in one figure, and save it in directry.
# The functions require the python libraries: brewer2mpl (to get color
# set from website); prettyplotlib
#--------------------------------------------------------------------------

# Common imports
import matplotlib.pyplot as plt
import numpy as np
import prettyplotlib as ppl
from prettyplotlib import brewer2mpl

# Set figure size
fig = plt.figure(figsize=(16,4))

# ---- Part 1: Simple matplotlib pcolormesh color map ----
def default_cmap ():
    '''
    This function is designed for creating a simple default
    matplotlib color map.
    '''
    ax = fig.add_subplot(1,3,1)

    np.random.seed(10)

    p = ax.pcolormesh(np.random.randn(10,10))
    fig.colorbar(p)
    ax.set_title('Color map with\nmatplotlib default pcolormesh',fontsize=11.5)

# ---- Part 2: Using ColorBrewer color set ----
def col_map (name, num_color):
    '''
    1) This function is designed to read a color set from ColorBrewer website
       http://bl.ocks.org/mbostock/5577023
    2) Returns the color map

    Note:
        This function requires "brewer2mpl" library.
    '''
    # Get color data from
    color_set = brewer2mpl.get_map(name, 'diverging', num_color,
                                   reverse=True).mpl_colormap
    ax = fig.add_subplot(1,3,2)
    np.random.seed(10)

    ppl.pcolormesh (fig, ax, np.random.randn(10,10),cmap=color_set)
    ax.set_title('Improved color map\nwith ColorBrewer color set',fontsize=11.5)

# ---- Part 3: Using prettyplotli ----
def ppl_cmap ():
    '''
    This function is designed for creating a simple default prettyplotlib
    color map for reproducing a color map created in part 2.

    Note:
        This function requires "prettyplotlib" library.
    '''
    ax = fig.add_subplot(1,3,3)
    np.random.seed(10)
    ppl.pcolormesh(fig, ax, np.random.randn(10,10))
    ax.set_title('Color map with\nprettyplotlib default pcolormesh',fontsize=11.5)

if __name__ == '__main__':
    '''
    This function calls three functions with color set name and its
    number of colors, and then plot the color maps in random points.
    Finally save the figure in the directry.
    '''
    my_col_map = col_map('RdBu', 11)
    my_default_cmap = default_cmap()
    my_ppl_cmap = ppl_cmap()
    plt.show()
    plt.savefig('comparing_pcolormesh_cmap.png', dpi=300)
