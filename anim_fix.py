import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D #, proj3d


def play(bodies, names, colors, sizes, path=True, legend=True, interval=20):
    
    dates = bodies[0].time
    
    #minxs = min([vec.x.min() for vec in bodies])
    #minys = min([vec.y.min() for vec in bodies])
    minzs = min([vec.z.min() for vec in bodies])
    #maxxs = max([vec.x.max() for vec in bodies])
    #maxys = max([vec.y.max() for vec in bodies])
    maxzs = max([vec.z.max() for vec in bodies])

    fig = plt.figure(figsize=plt.figaspect(0.5)*1.2)
    ax = Axes3D(fig) # taghir bejay khate payin
    #ax = fig.add_subplot(111, projection='3d')

    #ax.set_xlabel('X')
    #ax.set_ylabel('Y')
    #ax.set_zlabel('Z')
    #ax.tick_params(axis='x', labelsize=8)
    #ax.tick_params(axis='y', labelsize=8)
    #ax.tick_params(axis='z', labelsize=8)

    ax.set_zlim([8*minzs, 8*maxzs]) #  new
    
    ax.set_yticklabels([]) #new
    ax.set_xticklabels([]) #new
    ax.set_zticklabels([]) #new

    txt = ax.text(0, 0, 5*maxzs, ha='center', size='small', s='')
    #txt = ax.text(0, 0, 20886072841, ha='center', size='small', s='') #taghir be jaye payini
    #txt = ax.text(minxs, maxys, maxzs, '')
    txt2 = ax.text(0,0, 7*maxzs, ha='center', va='top', s='AstroDataScience.Net', alpha=0.5) # new
    

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
        date_str = dates[i].strftime(format='%d/%m/%Y') #new
        txt.set_text(date_str) #taghir
        ax.view_init(elev=10., azim=10) #new
        return lines + [txt] + [ax]#taghir


    #plt.locator_params(axis='x', nbins=7)
    #plt.locator_params(axis='y', nbins=7)
    #plt.locator_params(axis='z', nbins=7)

    if legend:
        plt.legend(loc='upper left')
    plt.grid(True)
    

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(dates), interval=interval,
                         blit=True, repeat=True)
    
    return anim
