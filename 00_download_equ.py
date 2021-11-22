import hypatie as hp
#import matplotlib.pyplot as plt
import pickle

t1 = '2021-12-18 12:49:10'
t2 = '2023-12-19 00:01:09'

# get positions with respect to the SSB
sun = hp.Vector('Sun', t1, t2, center='500@0', step=1000)
earth = hp.Vector('399', t1, t2, center='500@0', step=1000)
moon = hp.Vector('301', t1, t2, center='500@0', step=1000)
jwst = hp.Vector('-170', t1, t2, center='500@0', step=1000)

"""
bodies = [sun, earth, moon, jwst]
names = ['Sun', 'Earth', 'Moon', 'JWST']
colors = ['y','b','g','r']
sizes = [40, 20, 8, 3]

# play the animation
anim = hp.play(bodies, names, colors, sizes)
plt.show()
"""
ls = [sun.pos, earth.pos, moon.pos, jwst.pos]

with open('data/SSB_1000_alltime.pickle', 'wb') as f:
    pickle.dump([sun.time, ls], f)
    
