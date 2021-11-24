import hypatie as hp
import matplotlib.pyplot as plt
import pickle
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from hypatie.transform import rotating_coords

def play(bodies, names, colors, sizes, path=True):
    
    dates = bodies[0].time

    minzs = min([vec.z.min() for vec in bodies])
    maxzs = max([vec.z.max() for vec in bodies])

    fig = plt.figure(figsize=plt.figaspect(0.5)*1.2)
    ax = Axes3D(fig)
    #ax.set_zlim([8*minzs, 8*maxzs])

    
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])
    

    lines = []

    alpha = 0.2 if path else 0

    for i in range(len(bodies)):
        ax.plot(bodies[i].x, bodies[i].y, bodies[i].z, colors[i], alpha=alpha)
        lines.append(ax.plot(bodies[i].x[0:2], bodies[i].y[0:2], bodies[i].z[0:2],
                             color=colors[i], marker='o', markersize=sizes[i],
                             label=names[i])[0])
    
    def init():
        for line in lines:
            line.set_xdata(np.array([]))
            line.set_ydata(np.array([]))
            line.set_3d_properties(np.array([]))
        return lines

    def animate(i):
        for j,line in enumerate(lines):
            line.set_xdata(bodies[j].x[i])
            line.set_ydata(bodies[j].y[i])
            line.set_3d_properties(bodies[j].z[i])
        date_str = dates[i].strftime(format='%d/%m/%Y')
        ax.view_init(elev=90., azim=160)
        return lines  + [ax]

    plt.legend(loc='upper left')
    plt.grid(True)

    ax.set_ylim(ax.get_xlim())
    ax.set_zlim(ax.get_xlim())

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(dates), interval=20,
                         blit=True, repeat=True)
    
    return anim

with open('data/SSB_1000_alltime_eclip_suncenter.pickle', 'rb') as f:
    time, ls = pickle.load(f)

sun_pos, earth_pos, moon_pos, jwst_pos = ls

time = time[143:642]
sun_pos = sun_pos[143:642]
earth_pos = earth_pos[143:642]
jwst_pos = jwst_pos[143:642]

#===============
OE = earth_pos
OJ = jwst_pos

EJ = OJ - OE
EX = 50 * EJ
OX = OE + EX

jwst_pos = OX
#===============

sun_pos = rotating_coords(sun_pos, 365.256363004, time)
earth_pos = rotating_coords(earth_pos, 365.256363004, time)
jwst_pos = rotating_coords(jwst_pos, 365.256363004, time)


sun = hp.Body('Sun', sun_pos, time)
earth = hp.Body('Earth', earth_pos, time)
jwst = hp.Body('Moon', jwst_pos, time)

bodies = [sun, earth, jwst]
names = ['Sun', 'Earth', 'jwst']
colors = ['y','b','r']
sizes = [20, 8, 3]

anim = play(bodies, names, colors, sizes)
plt.show()

