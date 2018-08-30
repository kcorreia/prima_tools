

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


compound='3hexenol_60'




df=pd.read_csv(compound+'.csv',sep=',').fillna('')

df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)


df['Time&Date'] =  pd.to_datetime(df['Time&Date'])
#date_time_format='%Y/%m/%d %H:%M:%S.%f'
#df['Time&Date'] =  pd.to_datetime(df['Time&Date'], format=date_time_format)



df['Time (h)']=0.0
print '\tcreate hour vector'
tds=df['Time&Date']-df['Time&Date'][0]
df['Time (h)']=[round(td.days*24+td.seconds/3600.0,4) for td in tds]

# drop datapoints
#df=df.drop([106,107])


nrow = 12; ncol = 10;
fig, axs = plt.subplots(nrows=nrow, ncols=ncol)

for i,ax in enumerate(axs.reshape(-1)):
	x=df['Time (h)'].tolist()
	# +1 to ignore zero m/z peak
	y=df['mass'+str(i+1)]
	ax.plot(x,y,'.')
	#ax.fill_between(x,y,min(y))
	#ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
	# remove labels
	ax.set_yticklabels([])
	ax.set_xticklabels([])

plt.savefig(compound+'_mz_dynamics.png')



min_peak=1
max_peak=120

opacity=0.5
bar_width=0.50


max_peak_values=[np.log10(max(df['mass'+str(mz_value)].tolist())) for mz_value in range(min_peak,max_peak+1)]
max_peak_values=[-16 if np.isinf(log_value*-1)  else log_value for log_value in max_peak_values ]

x_axis=range(min_peak,max_peak+1)

fig, ax = plt.subplots(1,1)
for x,y in zip(x_axis,max_peak_values):
	#ax.fill_between(x_axis,max_peak_values,min(max_peak_values))
	ax.fill_between([x],[y],min(max_peak_values))



#plt.bar(x_axis, max_peak_value, bar_width,alpha=opacity,color='b',label='peaks')
plt.savefig(compound+'_maxpeak.png')



for i in [28,32,40,44,67]:
#for i in range(60,80):
	x=df['Time (h)'].tolist()
	# +1 to ignore zero m/z peak
	y=df['mass'+str(i)]
	fig, ax = plt.subplots(1,1)
	ax.plot(x,y,'.')
	plt.savefig(compound+'_peak'+str(i)+'_dynamics.png')



