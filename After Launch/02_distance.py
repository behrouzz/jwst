import pickle
import matplotlib.pyplot as plt
import hypatie as hp
from hypatie.animation import Body

t1 = '2021-12-25 12:49:10'
t2 = '2022-01-24 14:01:09'

with open('data_l2.pickle', 'rb') as f:
    t, pos = pickle.load(f)

earth_pos, moon_pos, jwst_pos, l2_pos= pos

#==========================================
import numpy as np
from hypatie.transform import mag

Earth_Jwst = jwst_pos - earth_pos

# distance
d = np.array([mag(i) for i in Earth_Jwst])

dt = t[1] - t[0]
dt = dt.seconds + dt.microseconds*1e-6

dx = d[1:] - d[:-1]
v = (dx/1000) / dt


fig, ax = plt.subplots(2,1)
ax[0].plot(t, d/1000)
ax[0].set_ylabel('Distance to Earth center (km)')
ax[0].grid()
ax[1].plot(t[:-1], v)
ax[1].set_ylabel('Speed wrt Earth center (km/s)')
ax[1].grid()
plt.show()
