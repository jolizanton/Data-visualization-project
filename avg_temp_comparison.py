import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'

#File1
with open(filename_1) as f:
    reader_1=csv.reader(f)
    header_row_1=next(reader_1)
    first_row_1=next(reader_1)

    #Get
    dates_s,rainfall_s=[],[]
    for row in reader_1:
        date= datetime.strptime(row[2],'%Y-%m-%d')
        try:
            rainfall=float(row[header_row_1.index('PRCP')])
        except ValueError:
            print(f"Value missing for {date}")
        else:
            dates_s.append(date)
            rainfall_s.append(rainfall)

    print (f"Sitka :{rainfall_s}")

# File2
with open(filename_2) as f:
    reader_2 = csv.reader(f)
    header_row_2 = next(reader_2)
    first_row_2 = next(reader_2)

    # Get
    dates_d, rainfall_d = [], []
    for row in reader_2:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rainfall = float(row[header_row_2.index('PRCP')])
        except ValueError:
            print(f"Value missing for {date}")
        else:
            dates_d.append(date)
            rainfall_d.append(rainfall)

    print (f"DeathValley :{rainfall_d}")


#plot
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates_s,rainfall_s,c='red')
ax.plot(dates_d,rainfall_d,c='blue')

#format plot
plt.title("Rainfall comparison", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel(header_row_1[3],fontsize=16)
#plt.ylim(20, 130)
#plt.tick_params(axis='both', which='major',labelsize=16)
plt.show()


