import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime

birddata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birddata.bird_name)


for birdy in bird_names:
	ix = birddata.bird_name == birdy
	x, y = birddata.longitude[ix], birddata.latitude[ix]
	plt.plot(x,y,'-', label = birdy)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc='best')
plt.show()

timestamp = []
for k in range(len(birddata)):
	timestamp.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamp, index = birddata.index)

data = birddata[birddata.bird_name=='Eric']
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for i,t in enumerate(elapsed_days):
	if t < next_day:
		inds.append(i)
	else:
		daily_mean_speed.append(np.mean(data.speed_2d[inds]))
		next_day += 1
		inds = []

plt.figure(figsize=(10,10))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean Speed (m/s)")
plt.show()

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")

for name in bird_names:
	ix = birddata['bird_name'] == name
	x, y = birddata.longitude[ix], birddata.latitude[ix]
	ax.plot(x,y,'.', transform=ccrs.Geodetic(),label=name)


plt.legend(loc="upper left")


