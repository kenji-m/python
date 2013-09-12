# ========================================================================
#
# OCNG689.600
# Homework 1, Part 3: Class
# Created by: Kenji Miyajima
# Date: 2013-09-12
#
# ========================================================================
#
# A class that reads the Burl 1 historical wind data from burl1_2011.dat
# and output u-wind, v-wind, sea level pressure, and date. Wind components
# have been converted to north ward and east word wind vector.
#
# ========================================================================

import numpy as np
from datetime import datetime

class ReadBurl():
    
    def __init__(self, file_name):
        self.file_name = file_name
        f = open (self.file_name)
        
        dates     = []
        pressure  = []
        u_wind    = []
        v_wind    = []
        
        for line in f.readlines()[2:]:
            data   = line.split()
            year   = int (data[0])
            month  = int (data[1])
            day    = int (data[2])
            hour   = int (data[3])
            minute = int (data[4])
            
            dates.append ( datetime(year, month, day, hour, minute) )
            pressure.append ( float(data[12]) )
            u_wind.append ( -(float(data[6])) * np.sin(float(data[5])*np.pi/180) )
            v_wind.append ( -(float(data[6])) * np.cos(float(data[5])*np.pi/180) )

        dates = np.array (dates)
        pressure = np.array(pressure)
        u_wind = np.array(u_wind)
        v_wind = np.array(v_wind)
        
        self.dates = dates
        self.pressure = pressure
        self.u_wind = u_wind
        self.v_wind = v_wind
        
        
        data = {'dates': np.array(dates), 'pressure': np.array(pressure),
                'u-wind': np.array(u_wind), 'v-wind': np.array(v_wind)} 
                
        print data['dates']
        print data['pressure']
        print data['u-wind']
        print data['v-wind']

burl = ReadBurl('burl1_2011.dat')