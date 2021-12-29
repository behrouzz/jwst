import pickle
import matplotlib.pyplot as plt
import hypatie as hp
from hypatie.animation import Body

t1 = '2021-12-25 12:49:10'
t2 = '2022-01-24 14:01:09'

with open('data_l2.pickle', 'rb') as f:
    t, pos = pickle.load(f)

earth_pos, moon_pos, jwst_pos, l2_pos= pos

earth = Body(name='Earth', pos=earth_pos, time=t)
moon = Body(name='Moon', pos=moon_pos, time=t)
jwst = Body(name='James Webb', pos=jwst_pos, time=t)
l2 = Body(name='L2', pos=l2_pos, time=t)

bodies = [earth, moon, jwst, l2]
names = ['Earth', 'Moon', 'James Webb', 'L2']
colors = ['b','g','r', 'k']
sizes = [20, 8, 3, 2]

anim = hp.play(bodies, names, colors, sizes)
plt.show()
