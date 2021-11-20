import hypatie as hp
import matplotlib.pyplot as plt
import pickle

with open('data/SSB_1000_alltime.pickle', 'rb') as f:
    time, ls = pickle.load(f)

sun_pos, earth_pos, moon_pos, jwst_pos = ls

sun = hp.Body(name='Sun', pos=sun_pos, time=time)
earth = hp.Body(name='Earth', pos=earth_pos, time=time)
jwst = hp.Body(name='JWST', pos=jwst_pos, time=time)


bodies = [sun, earth, jwst]
names = ['Sun', 'Earth', 'JWST']
colors = ['y','b','r']
sizes = [40, 20, 3]

anim = hp.play(bodies, names, colors, sizes)
plt.show()

