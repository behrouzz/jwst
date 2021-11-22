import hypatie as hp
#import matplotlib.pyplot as plt
import pickle

t1 = '2021-12-18 12:49:10'
t2 = '2023-12-19 00:01:09'

# get positions with respect to Earth-Moon barycenter
earth = hp.Vector('399', t1, t2, center='500@3', step=1000)
moon = hp.Vector('301', t1, t2, center='500@3', step=1000)
jwst = hp.Vector('-170', t1, t2, center='500@3', step=1000)

ls = [earth.pos, moon.pos, jwst.pos]

with open('data/erath-moon_1000_alltime.pickle', 'wb') as f:
    pickle.dump([earth.time, ls], f)
    
