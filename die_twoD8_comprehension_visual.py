from plotly.graph_objs import Bar,Layout
from plotly import offline

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

x_values=list(range(2,max_result+1))
data=[Bar(x=x_values,y=frequencies)]
x_axis_config={'title':'Result','dtick':1}
y_axis_config={'title':'Frequency of result'}
my_layout=Layout(title='Results of rolling two D8 10000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='two D8.html')
print (results)