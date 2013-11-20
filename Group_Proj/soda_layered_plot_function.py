# Four layered temperature 2D plot function for SODA
# Kenji Miyajima
# 2013-11-20

import numpy as np
import netCDF4
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt

def soda_layered_plot(url,variable,llat, ulat, llon, rlon,time):

    nc = netCDF4.Dataset(url)
    t  = time
#    d  = depth
    var_0 = nc.variables[variable][t,0,:,:]
    var_1 = nc.variables[variable][t,1,:,:]
    var_2 = nc.variables[variable][t,2,:,:]
    var_3 = nc.variables[variable][t,3,:,:]
#Q: do we need define t,d in function
    lon = nc.variables['LON'][:]
    lat = nc.variables['LAT'][:]

    '''
    Theoretically subplotting part below should work, but I could not test on
    both local SODA file and URL. The slightly different version of the
    multi-layered function works well with the local SODA file, but URL could
    not be tested because of file size and the spec of my laptop.

    Concern: As an output figure shows, temperature ranges for each assigned
    color are different in four subplots. Absolute ranges can be assigned
    for each color?
    '''

    # create new figure
    fig = plt.figure()

    # 4x1 Subplot panel 1
    ax = fig.add_subplot(411)
    ax.add_axes([0.1,0.1,0.8,0.8])
    m0 = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    lons0, lats0 = np.meshgrid(lon, lat)
    x0,y0 = m0(lons0, lats0)

    # drawing the map
    m0.fillcontinents(color='gray',lake_color='gray')
    m0.drawcoastlines(linewidth = 0.4)
    m0.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m0.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m0.drawmapboundary()

    # plotting data on the map
    plt.contourf(x0,y0,var_0,cmap=cm.sstanom)
    cb0 = plt.colorbar(orientation='horizontal')
    cb0.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')

    # 4x1 Subplot panel 2
    ax = fig.add_subplot(412)
    ax.add_axes([0.1,0.1,0.8,0.8])
    m1 = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    lons1, lats1 = np.meshgrid(lon, lat)
    x1,y1 = m1(lons1, lats1)

    # drawing the map
    m1.fillcontinents(color='gray',lake_color='gray')
    m1.drawcoastlines(linewidth = 0.4)
    m1.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m1.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m1.drawmapboundary()

    # plotting data on the map
    plt.contourf(x1,y1,var_1,cmap=cm.sstanom)
    cb1 = plt.colorbar(orientation='horizontal')
    cb1.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')

    # 4x1 Subplot panel 3
    ax = fig.add_subplot(413)
    ax.add_axes([0.1,0.1,0.8,0.8])
    m2 = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    lons2, lats2 = np.meshgrid(lon, lat)
    x2,y2 = m0(lons2, lats2)

    # drawing the map
    m2.fillcontinents(color='gray',lake_color='gray')
    m2.drawcoastlines(linewidth = 0.4)
    m2.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m2.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m2.drawmapboundary()

    # plotting data on the map
    plt.contourf(x2,y2,var_2,cmap=cm.sstanom)
    cb2 = plt.colorbar(orientation='horizontal')
    cb2.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')

    # 4x1 Subplot panel 4
    ax = fig.add_subplot(414)
    ax.add_axes([0.1,0.1,0.8,0.8])
    m3 = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    lons3, lats3 = np.meshgrid(lon, lat)
    x3,y3 = m3(lons3, lats3)

    # drawing the map
    m3.fillcontinents(color='gray',lake_color='gray')
    m3.drawcoastlines(linewidth = 0.4)
    m3.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m3.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m3.drawmapboundary()

    # plotting data on the map
    plt.contourf(x0,y0,var_0,cmap=cm.sstanom)
    cb3 = plt.colorbar(orientation='horizontal')
    cb3.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')

'''
This code works for local soda file.

    # create new figure
    fig=plt.figure()

    # 4x1 Subplot panel 1
    ax = fig.add_subplot(411)
    m0 = Basemap(llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            projection='mill',resolution = 'h',ax=ax)
    ny0 = temp_0.shape[0]; nx0 =temp_0.shape[1]
    lons0, lats0 = m0.makegrid(nx0, ny0)
    x0, y0 = m0(lons0, lats0)

    cs = m0.contourf(x0,y0,temp_0,cmap=cm.sstanom)

    # colorbar on bottom.
    cbar0 = m0.colorbar(cs,location='bottom', size="15%", pad='35%')
    m0.drawcoastlines()

    parallels = np.arange(-5.,5.,2.)
    m0.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

    meridians = np.arange(120.,300.,30.)
    m0.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

    cbar0.set_label('Temperature(deg.C)')
    ax.set_title('Sea Temperature at ' +str(dates[t])+ 'at depth of 5.01m')
'''

'''
    # setting up data into basemap with given projection
    lons, lats = np.meshgrid(lon, lat)
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    m = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    x,y = m(lons, lats)

    # drawing the map
    m.fillcontinents(color='gray',lake_color='gray')
    m.drawcoastlines(linewidth = 0.4)
    m.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m.drawmapboundary()

    # plotting data on the map
    plt.contourf(x,y,var,cmap=cm.sstanom)
    cb = plt.colorbar(orientation='horizontal')
    cb.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')
    plt.show()
    #plt.savefig('SST_globeplot_Hw3.png')
## Do I need a title for the plot or a title for the whole plot?
'''


'''url = 'http://sodaserver.tamu.edu:80/opendap/TEMP/SODA_2.3.1_01-01_python.cdf'
variable = 'TEMP'
#nino 3.4 region
llat = -5.
####Q: range of latitude: 0-360, do we need a loop? transfore the latidue
ulat = 5.
llon = -170.
rlon = -120.'''
