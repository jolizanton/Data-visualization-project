import matplotlib.pyplot as plt
from random_walk import RandomWalk

#while True:
rw=RandomWalk(5000)
rw.fill_walk()

#fig,ax=plt.subplots(figsize=(15,9),dpi=128)
fig, ax = plt.subplots()
#point_numbers=range(rw.num_points)
ax.plot(rw.x_values,rw.y_values)

ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
    #plt.savefig('random_walk.png', bbox_inches='tight')

    #keep_running=input("want to make another rw?(y/n)")
    #if keep_running=='n':
        #break