import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/san_frans.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    first_row=next(reader)
    print (header_row)
    print (first_row)
    print (header_row.index('San Francisco Temperature [2 m elevation corrected]'))

    temp_s = []
    for row in reader:
        temp = float(row[header_row.index('San Francisco Temperature [2 m elevation corrected]')])
        temp_s.append(temp)
    print(temp_s)

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(temp_s, c='red')

# format plot
plt.title(header_row[1][:13], fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel(header_row[1][13:], fontsize=16)
plt.show()


