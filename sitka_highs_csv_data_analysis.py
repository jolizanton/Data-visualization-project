import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    first_row=next(reader)

    print (header_row)
    print (first_row)
    for index, column_header in enumerate(header_row):
       print (index, column_header)

    #Get high temperatures
    dates,highs,lows=[],[],[]
    for row in reader:
        date= datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(date)
        high=int(row[header_row.index('TMAX')])
        highs.append(high)
        low=int(row[header_row.index('TMIN')])
        lows.append(low)
    print (highs)

#plot the high temperatures
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#format plot
plt.title(first_row[1], fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.ylim(20, 130)
plt.show()

