tmin = '2021-12-25 12:49:09.184'
tmax = '2022-01-24 14:01:09.184'

import hypatie as hp
import matplotlib.pyplot as plt

t1 = '2021-12-25 12:49:10'
t2 = '2022-01-24 14:01:09'

earth = hp.Vector('399', t1, t2, center='500@3', step=1000)
moon = hp.Vector('301', t1, t2, center='500@3', step=1000)
jwst = hp.Vector('-170', t1, t2, center='500@3', step=1000)
l2 = hp.Vector('SEMB-L2', t1, t2, center='500@3', step=1000)

bodies = [earth, moon, jwst, l2]
names = ['Earth', 'Moon', 'James Webb', 'L2']
colors = ['b','g','r', 'k']
sizes = [20, 8, 3, 1]

import pickle

with open('data_l2.pickle', 'wb') as f:
    pickle.dump([earth.time, [earth.pos, moon.pos, jwst.pos, l2.pos]], f)
