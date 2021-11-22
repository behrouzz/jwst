import hypatie as hp
import matplotlib.pyplot as plt
import pickle
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def play(bodies, names, colors, sizes, path=True):
    
    dates = bodies[0].time

    minzs = min([vec.z.min() for vec in bodies])
    maxzs = max([vec.z.max() for vec in bodies])

    fig = plt.figure(figsize=plt.figaspect(0.5)*1.2)
    ax = Axes3D(fig)
    #ax.set_zlim([8*minzs, 8*maxzs])
    # should be changed to be in real scale
    
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])

    #txt = ax.text(0, 0, 5*maxzs, ha='center', size='small', s='')
    #txt2 = ax.text(0,0, 7*maxzs, ha='center', va='top', s='AstroDataScience.Net', alpha=0.5)
    txt = ax.text(0, 0, 0.9*maxzs, ha='center', size='small', s='')
    txt2 = ax.text(0,0, 0.8*maxzs, ha='center', va='top', s='AstroDataScience.Net', alpha=0.5)
    

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
        txt.set_text(date_str)
        ax.view_init(elev=10., azim=(i+45)/5)
        return lines + [txt] + [ax]

    plt.legend(loc='upper left')
    plt.grid(True)
    

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(dates), interval=20,
                         blit=True, repeat=True)
    
    return anim


with open('data/erath-moon_1000_alltime.pickle', 'rb') as f:
    time, ls = pickle.load(f)

earth_pos, moon_pos, jwst_pos = ls

a1,a2 = 143,638
time = time[a1:a2]
earth_pos = earth_pos[a1:a2]
moon_pos = moon_pos[a1:a2]
jwst_pos = jwst_pos[a1:a2]

earth = hp.Body(name='Earth', pos=earth_pos, time=time)
moon = hp.Body(name='Moon', pos=moon_pos, time=time)
jwst = hp.Body(name='JWST', pos=jwst_pos, time=time)


bodies = [earth, moon, jwst]
names = ['Earth', 'Moon', 'JWST']
colors = ['b','g','r']
sizes = [20, 7, 3]

anim = play(bodies, names, colors, sizes)
plt.show()
#anim.save('test.avi')

