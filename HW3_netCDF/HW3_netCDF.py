# =======================================================================
# OCNG689.600
# Homework 3: netCDF
# Created by: Kenji Miyajima
# Date: 2013-10-17
# -----------------------------------------------------------------------
# Script that creates:
#   Part1: A plan-view plot, in lat-lon, using Basemap from the netCDF file.
#   Part2: A timeseries using pandas in the netCDF file and plot the result.
# -----------------------------------------------------------------------
# Input:
#       Climate variables around Japan including:
#           Sea Surface Temperature
#           Time
#           Longitude
#           Latitude
# Output:
#       A plan-view plot on sea surface temperature using Basemap
#       A time series on sea surface temperature using pandas
# =======================================================================

# import packages
import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#==========================#
# Part 1: A plan-view plot #
#==========================#

# input data from netCDF file on website
data = nc.Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/Tohoku/NGSST')

sst = 0.15 * data.variables['st'][0,:] - 3.0
lon = data.variables['lon'][:]
lat = data.variables['lat'][:]
lon,lat = np.meshgrid(lon,lat)

m = Basemap(llcrnrlon=116,llcrnrlat=13,urcrnrlon=165,urcrnrlat=62,
            projection='merc',lon_0=0,resolution='c')
x,y = m(lon,lat)

# plot and show the result of mapping
cmap = plt.cm.RdBu_r
m.drawcoastlines(linewidth = 0.3)
m.drawcountries()
m.fillcontinents(color='#FAF8CC')
m.drawmeridians(np.arange(115,165,10),labels=[1,0,0,1],fontsize=10)
m.drawparallels(np.arange(15,60,10),labels=[1,0,0,1],fontsize=10)
plt.pcolormesh(x,y,sst, shading='flat',cmap=cmap)
cb = plt.colorbar()

# Label metadata
cb.set_label('Sea Surface Temperature (deg C)')
plt.title('SST Distribution around Japan \n'
            'July 2003 - November 2011',fontsize=12)
plt.show()

# Save the figure 1
plt.savefig('HW3_netCDF_Kenji.png', dpi = 600)

#==================================#
# Part 2: Time series using Pandas #
#==================================#

dates = data.variables['time']
st = 0.15 * data.variables['st'][:,10,20] -3.0
rng = pd.date_range('1/7/2003',periods=st.size, freq='D')
ts1 = pd.Series(st,index = rng)
t_series = pd.DataFrame(ts1)

# Plotting the timeseries for point index: 10, 20
t_series.plot(figsize=(10.0, 7.0),color='#0066cc', legend = False)
plt.title('Daily Time Series of Sea Surface Temperature at selected lon-lat\n'
            'July 1, 2003 to November 20, 2011 around Japan',fontsize =15)
plt.xlabel('Time (year)',fontsize =15)
plt.ylabel('Sea Surface Temperature (deg C)',fontsize =15)
plt.subplots_adjust(bottom=0.15,left=0.1)
plt.show()

# Save the figure 2
plt.savefig('HW3_pandas_Kenji.png')
