import hypatie as hp
import matplotlib.pyplot as plt
import pickle
from anim_rot import play


with open('data/SSB_1000_alltime_eclip.pickle', 'rb') as f:
    time, ls = pickle.load(f)

sun_pos, earth_pos, _, jwst_pos = ls

time = time[143:642]
sun_pos = sun_pos[143:642]
earth_pos = earth_pos[143:642]
jwst_pos = jwst_pos[143:642]

#===============
OE = earth_pos
OJ = jwst_pos

EJ = OJ - OE
EX = 10 * EJ
OX = OE + EX

jwst_pos = OX
#===============
sun = hp.Body(name='Sun', pos=sun_pos, time=time)
earth = hp.Body(name='Earth', pos=earth_pos, time=time)
jwst = hp.Body(name='JWST', pos=jwst_pos, time=time)


bodies = [sun, earth, jwst]
names = ['Sun', 'Earth', 'JWST']
colors = ['y','b','r']
sizes = [20, 7, 3]

anim = play(bodies, names, colors, sizes)
plt.show()

