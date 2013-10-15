# ============================
# OCNG689.600
# Homework 2, Part 2: Function
# Created by: Kenji Miyajima
# Date: 2013-10-15
# ============================

# import packages
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import urllib as ulb

def USGS_water_data (big_date, end_date, site_num):
    '''
    A function that retrieves the river discharge data from the USGS website
    and reads the station number, amount of discharge, and calculate
    the annual mean and the standard deviation of the discharge.

    Input:
        USGS URL for retrieving data
        Selected data from retrieved USGS data
    Output:
        Data sent to the plot_USGS_data function for plotting
    '''

    # Setting up the selected data
    start = str(date(1900,1,1))
    end   = str(date.today())
    siteno='01100000'

    # Open USGS website to download text data
    site = ulb.urlopen\
            ('http://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb'+\
            '&begin_date='+start+'&end_date='+end+'&site_no='+siteno)

    # Create empty lists
    dates   = []
    dateindex = []
    flow    = []
    avgflow = []
    stdflow = []

    # Read
    for line in site.readlines()[28:]:
        data = line.split ()
        dateindex = data[2]
        year  = int(dateindex.split('-')[0])
        month = int(dateindex.split('-')[1])
        day   = int(dateindex.split('-')[2])
        dates.append(date(year, month, day))
        flow.append(int(data[3]))

    site.close()

    # Convert lists into arrays
    dates = np.array (dates)
    flow  = np.array (flow)

    # Convert flow data into SI unit
    flow = flow / 35.315

    # Calculate annual mean and standrd deviation of streamflow for each day
    months = np.array ([d.month for d in dates])
    days   = np.array ([d.day for d in dates])

    for idx in dates:
        cal_flow = flow [(months==idx.month) & (days==idx.day)]
        avgflow.append (np.mean (cal_flow))
        stdflow.append (np.std (cal_flow))

    # Convert lists to arrays
    avgflow  = np.array(avgflow)
    stdflow = np.array(stdflow)

    # Select the time span for plotting
    plt_year    = np.array ([d.year for d in dates])
    idx         = np.where (plt_year >= 2011)
    plt_dates   = dates [idx]
    plt_flow    = flow [idx]
    plt_avgflow = avgflow [idx]
    plt_upstdv  = avgflow [idx] + stdflow [idx]
    plt_lowstdv = avgflow [idx] - stdflow [idx]

    plot_USGS_data(plt_year,idx,plt_dates,plt_flow,plt_avgflow,plt_upstdv,plt_lowstdv,siteno)

def plot_USGS_data(plt_year,idx,plt_dates,plt_flow,plt_avgflow,plt_upstdv,plt_lowstdv,siteno):
    '''
    A function that plots the USGS stream flow data from the USGS_water_data function.
    Input:
        Station data from the USGS_water_data function.
    Output:
        PDF file that plot the downloaded data for 2011-Present day:
            Daily stream flow
            Annual mean flow
            Annual standard deviation for the annual mean flow
    '''

    # Plot the results
    fig=plt.figure(figsize=(15,7))
    fig.autofmt_xdate()

    ax=fig.add_axes([0.1,0.1,0.8,0.8])
    ax.plot(plt_dates, plt_flow, 'k', label = "Daily Flow",  lw = 1.7)
    ax.plot(plt_dates, plt_avgflow, color = '#0066cc', label = "Annual Mean Flow", lw = 1.5)
    ax.plot(plt_dates, plt_upstdv, ':', color = '#3366ff', label = 'Upper Std. Dev.')
    ax.plot(plt_dates, plt_lowstdv, ':', color = '#3366ff', label = 'Lower Std. Dev.')
    ax.fill_between(plt_dates, plt_upstdv, plt_lowstdv, facecolor='#66ccff',alpha=0.3)

    # Add Metadata
    plt.title('Daily/Annual Mean/Std.Dev. Flow Timeseries\n'
                'Station No.'+siteno+': MERRIMACK RIVER BL CONCORD RIVER AT LOWELL, MA', size=18)
    plt.xlabel('Dates (mmm/yyyy)')
    plt.ylabel(r'Stream Flow Rate (m$^{3}$ s$^{-1}$)')
    ax.grid()
    ax.hold(True)

    # Add legend and maximize figure window
    ax.legend()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.show()

    # Save the figure as .pdf file
    plt.savefig('Kenji_Miyajima_HW2_Func.pdf', dpi=300)

    # Close plot
    plt.close()

# Initiate the function
USGS_water_data (2010, 2013, '01100000')
