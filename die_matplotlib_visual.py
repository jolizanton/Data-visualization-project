import matplotlib.pyplot as plt
from die import Die

die_1=Die(8)
die_2=Die(8)

results=[die_1.roll()+die_2.roll() for roll_number in range(10000)]

#Analyze the results
max_result=die_1.num_sides+die_2.num_sides
values=[value for value in range(2, max_result+1)]
frequencies=[results.count(value) for value in range(2, max_result+1)]

print (values)
print (frequencies)

#Visualize the results

fig, ax = plt.subplots()
x_values=range(2,max_result+1)
ax.plot(x_values,frequencies)

ax.scatter(x_values,frequencies, c='red', edgecolors='none', s=100)
plt.show()

