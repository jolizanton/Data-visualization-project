from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die

die_1=Die(8)
die_2=Die(8)

results=[]
for roll_num in range(10000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#Analyze the results
values=[]
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    values.append(value)
    frequency=results.count(value)
    frequencies.append(frequency)
    print (f"Number {value} occured {frequency} times.")
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