import numpy as np
from datetime import datetime
import netCDF4
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt

def soda_temp_plot(file_name,t):
    # Read file
    file = file_name
    nc = netCDF4.Dataset(file)
    dates=netCDF4.num2date(nc.variables['TIME1'][:],'seconds since 1916-01-02 12:00:00')

    temp = nc.variables['TEMP']
    # Temperature for 4 depths
    temp_0 = temp[t,0,:,:]
    temp_1 = temp[t,1,:,:]
    temp_2 = temp[t,2,:,:]
    temp_3 = temp[t,3,:,:]

    lon = nc.variables['LON241_580'][:]
    lat = nc.variables['LAT142_161'][:]

    '''
    Concern: As an output figure shows, temperature ranges for each assigned
    color are different in four subplots. Absolute ranges can be assigned
    for each color?
    '''

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

    # 4x1 Subplot panel 2
    ax = fig.add_subplot(412)
    m1 = Basemap(llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            projection='mill',resolution = 'h',ax=ax)
    ny1 = temp_1.shape[0]; nx1 =temp_1.shape[1]
    lons1, lats1 = m1.makegrid(nx1, ny1)
    x1, y1 = m1(lons1, lats1)

    cs = m1.contourf(x1,y1,temp_1,cmap=cm.sstanom)

    # colorbar on bottom.
    cbar1 = m1.colorbar(cs,location='bottom', size="15%", pad='35%')
    m1.drawcoastlines()

    parallels = np.arange(-5.,5.,2.)
    m1.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

    meridians = np.arange(120.,300.,30.)
    m1.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

    cbar1.set_label('Temperature(deg.C)')
    ax.set_title('Sea Temperature at ' +str(dates[t])+ 'at depth of 15.07m')

    # 4x1 Subplot panel 3
    ax = fig.add_subplot(413)
    m2 = Basemap(llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            projection='mill',resolution = 'h',ax=ax)
    ny2 = temp_2.shape[0]; nx2 =temp_2.shape[1]
    lons2, lats2 = m2.makegrid(nx2, ny2)
    x2, y2 = m2(lons2, lats2)

    cs = m2.contourf(x2,y2,temp_2,cmap=cm.sstanom)

    # colorbar on bottom.
    cbar2 = m2.colorbar(cs,location='bottom', size="15%", pad='35%')
    m2.drawcoastlines()

    parallels = np.arange(-5.,5.,2.)
    m2.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

    meridians = np.arange(120.,300.,30.)
    m2.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

    cbar2.set_label('Temperature(deg.C)')
    ax.set_title('Sea Temperature at ' +str(dates[t])+ 'at depth of 25.28m')

    # 4x1 Subplot panel  4
    ax = fig.add_subplot(414)
    m3 = Basemap(llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            projection='mill',resolution = 'h',ax=ax)
    ny3 = temp_3.shape[0]; nx3 =temp_1.shape[1]
    lons3, lats3 = m3.makegrid(nx3, ny3)
    x3, y3 = m3(lons3, lats3)

    cs = m3.contourf(x3,y3,temp_3,cmap=cm.sstanom)

    # colorbar on bottom.
    cbar3 = m3.colorbar(cs,location='bottom', size="15%", pad='35%')
    m3.drawcoastlines()

    parallels = np.arange(-5.,5.,2.)
    m3.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

    meridians = np.arange(120.,300.,30.)
    m3.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

    cbar3.set_label('Temperature(deg.C)')
    ax.set_title('Sea Temperature at ' +str(dates[t])+ 'at depth of 35.76m')

    plt.show()

    plt.savefig('SODA_multilayered_temp.png', dpi = 300)

soda_temp_plot('SODA_2.3.1_01-01_python.cdf',2)
