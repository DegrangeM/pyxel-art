from libs.PyxelArt import *

for k in range(2,7) :
    colorier(k,8)
for k in range(4,9) :
    colorier(4,k)
for k in range(1,4) :
    colorier(k,k)
    j = 8 - k
    colorier(j,k)

ss()