from plotly.graph_objs import Bar,Layout
from plotly import offline

#import matplotlib.pyplot as plt
from random_walk import RandomWalk

#while True:

rw=RandomWalk(5000)
rw.fill_walk()
# Visualize the results

x_values=list(rw.x_values)
data=[Bar(x=x_values,y=rw.y_values)]

x_axis_config={'title':'rw','dtick':1}
y_axis_config={'title':'rw'}
my_layout=Layout(title='Random walk',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='Random walk_plotly.html')


    #keep_running=input("want to make another rw?(y/n)")
    #if keep_running=='n':
        #break

