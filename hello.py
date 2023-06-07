import numpy as honey
l= [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
s=honey.array(l)
print(s)
v=honey.split(s,(1,2),axis=1)
print(v)