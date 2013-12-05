#------------------------------------------------------------------
# Kenji Miyajima
# OCNG689
# 2013-12-04
#---------------------------------------------------------------------
# Functions draw a simple default mtplotlib scatter graph, an improved
# version of it by reading color data from ColorBrewer website and
# changing fonts and design around a graph, and a simple prettyplotlib
# scatter graph. Finally save three graphs in one figure in directry.
# The functions require the python libraries: brewer2mpl (to get color
# set from website); prettyplotlib
#------------------------------------------------------------------

import matplotlib.pyplot as plt
import prettyplotlib as ppl
import brewer2mpl
import numpy as np

# Set the figure size
fig=plt.figure(figsize=(18,5))

# -------- Part 1: Simple matplot scatter graph --------
def default_scatter ():
    '''
    This function draws a simple default scatter graph
    '''
    # Set the random seed for consistency
    np.random.seed(12)
    ax = fig.add_subplot(1,3,1)

    # Show the whole color range
    for i in range(8):
        x = np.random.normal(loc=i, size=1000)
        y = np.random.normal(loc=i, size=1000)
        ax.scatter(x, y, label=str(i))

    ax.legend(loc=4,fontsize=11,scatterpoints=1)
    ax.set_title('A `scatter` graph example\n'
                 'showing default matplotlib `scatter`', fontsize=12)

#-------- Part 2: Using ColorBrewer color set ----------
def brewer_scatter_plot (name, num_color):
    '''
    1) This function is designed to read a color set from ColorBrewer website
       http://bl.ocks.org/mbostock/5577023)
    2) Tweaks some design.
    3) Returns the scatter graph

    Note:
        This function requires "brewer2mpl" library.
    '''
    # Retrieve the color set from the website
    color_set = brewer2mpl.get_map(name, 'qualitative', num_color).mpl_colors

    # Save a nice dark grey as a variable
    almost_black = '#262626'

    # Set the random seed for consistency
    np.random.seed(12)

    ax = fig.add_subplot(1,3,2)
    #fig, ax = plt.subplots(1)

    # Show the whole color range
    for i in range(num_color):
        x = np.random.normal(loc=i, size=1000)
        y = np.random.normal(loc=i, size=1000)
        color = color_set[i]
        ax.scatter(x, y, label=str(i), alpha=0.5, edgecolor=almost_black,
                   facecolor=color, linewidth=0.15)

    # Remove top and right axes lines ("spines")
    spines_to_remove = ['top', 'right']
    for spine in spines_to_remove:
        ax.spines[spine].set_visible(False)

    # Get rid of ticks. The position of the numbers is informative enough of
    # the position of the value.
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # For remaining spines, thin out their line and change the black to
    # a slightly off-black dark grey
    almost_black = '#262626'
    spines_to_keep = ['bottom', 'left']
    for spine in spines_to_keep:
        ax.spines[spine].set_linewidth(0.5)
        ax.spines[spine].set_color(almost_black)

    # Change the labels to the off-black
    ax.xaxis.label.set_color(almost_black)
    ax.yaxis.label.set_color(almost_black)

    # Change the axis title to off-black
    ax.title.set_color(almost_black)

    # Remove the line around the legend box, and instead fill it with a
    # light grey. Also only use one point for the scatterplot legend because
    # the user will get the idea after just one, they don't need three.
    light_grey = np.array([float(248)/float(255)]*3)
    legend = ax.legend(frameon=True,scatterpoints=1,loc=4,fontsize=11)
    rect = legend.get_frame()
    rect.set_facecolor(light_grey)
    rect.set_linewidth(0.0)

    # Change the legend label colors to almost black, too
    texts = legend.texts
    for t in texts:
        t.set_color(almost_black)

    ax.set_title('An improved matplotlib `scatter` graph\n'
                 'by ColorBrewer color set', fontsize=12)

# ---- Part 3: --------------------------------------------
# Using prettyplotlib to creating the same graph in part 2
# ---------------------------------------------------------
def ppl_scatter ():
    '''
    This function draws a simple prettyplotlib scatter graph
    that reproduces the graph created in part 2.

    Note:
        This function requires "prettyplotlib" library.
    '''
    np.random.seed(12)
    ax = fig.add_subplot(1,3,3)

    # Show the whole color range
    for i in range(8):
        x = np.random.normal(loc=i, size=1000)
        y = np.random.normal(loc=i, size=1000)
        ppl.scatter(ax, x, y, label=str(i))

    ppl.legend(ax,loc=4,fontsize=11)

    ax.set_title('A prettyplotlib `scatter` example\n'
                'showing default color cycle and scatter params',fontsize=12)

if __name__ == '__main__':
    '''
    This function calls three functions with color set name and its
    number of colors, and then plot the scatter graphs in random points.
    Finally save the figure in the directry.
    '''
    my_scatter = brewer_scatter_plot('Set2', 8)
    my_simple_scat = default_scatter ()
    my_ppl_scat = ppl_scatter ()
    plt.show()
    plt.savefig('comparing_scatter.png',dpi=300)
