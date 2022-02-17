from libs.PyxelArt import *

for k in range(1,8) :
    colorier(5,k)
    if k < 5 :
        colorier(2,k)
    else :
        colorier(k-3,7)
colorier(3,1)
colorier(4,1)
colorier(3,4)
colorier(4,4)

ss()