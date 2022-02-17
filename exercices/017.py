from libs.PyxelArt import *

b = 6
c = 7
d = 8
colorier(b,c)
colorier(c,b)
colorier(c,d)
colorier(d,c)
for k in range(1,9) :
    if k != 7 :
        colorier(k,k)
colorier(3,5)
for x in range(3) :
    for y in range(6,9) :
        a = y - x
        if a != 6 :
            colorier(x,y)

colorier(7,1)
colorier(6,2)
colorier(5,3)

ss()