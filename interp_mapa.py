import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits import basemap as bm

temp_file = nc.Dataset('air.mon.ltm.nc')

lati = temp_file.variables['lat'][:]
longi = temp_file.variables['lon'][:]
air = temp_file.variables['air'][:]

fig = plt.figure(figsize=(40,10))

map = Basemap(projection='mill', lat
