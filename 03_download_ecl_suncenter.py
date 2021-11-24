import hypatie as hp
import pickle

t1 = '2021-12-18 12:49:10'
t2 = '2023-12-19 00:01:09'

# get positions with respect to the SSB
sun = hp.Vector('Sun', t1, t2, center='500@10', step=1000, ref_plane='ECLIPTIC')
earth = hp.Vector('399', t1, t2, center='500@10', step=1000, ref_plane='ECLIPTIC')
moon = hp.Vector('301', t1, t2, center='500@10', step=1000, ref_plane='ECLIPTIC')
jwst = hp.Vector('-170', t1, t2, center='500@10', step=1000, ref_plane='ECLIPTIC')


ls = [sun.pos, earth.pos, moon.pos, jwst.pos]

with open('data/SSB_1000_alltime_eclip_suncenter.pickle', 'wb') as f:
    pickle.dump([sun.time, ls], f)
    
