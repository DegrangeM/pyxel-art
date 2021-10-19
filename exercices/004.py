from libs.PyxelArt import *

a = 1


for loop in range(7) :
    colorier(a,0)
    colorier(a,8)
    colorier(0,a)
    colorier(8,a)
    a = a + 1

b = 2
c = 6
d = c - b

colorier(b,b)
colorier(c,c)
colorier(b,c)
colorier(c,b)
colorier(d,d)

ss()