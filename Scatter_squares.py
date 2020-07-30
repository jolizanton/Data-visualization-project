#Scatter

import matplotlib.pyplot as plt
plt.style.use('seaborn')
#input_values=[1,2,3,4,5]
x_values= range(1,1001)
y_values=[x**2 for x in x_values]
#squares=[1,4,9,16,25]
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,c=(0,0.8,0),s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,s=10)

ax.set_title("Square numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')