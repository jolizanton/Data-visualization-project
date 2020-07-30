import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print (header_row)
    for index, column_header in enumerate(header_row):
       print (index, column_header)

    #Get
    dates,rainfall_readings=[],[]
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)
        rainfall=float(row[3])
        rainfall_readings.append(rainfall)
    print (rainfall_readings)

#plot
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,rainfall_readings,c='green')

#format plot
plt.title("Sitka rainfall", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall",fontsize=16)
#plt.tick_params(axis='both', which='major',labelsize=16)
plt.show()


